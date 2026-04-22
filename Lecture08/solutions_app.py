import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Descriptors import ExactMolWt, MolLogP, NumHDonors, NumHAcceptors
from stmol import showmol
import py3Dmol
from pathlib import Path
import pandas as pd
import os
from streamlit_ketcher import st_ketcher
from rdkit.Chem import rdFingerprintGenerator
import numpy as np
import mols2grid
import streamlit.components.v1 as components
import plotly.express as px
import plotly.figure_factory as ff
from typing import Tuple, List

# Load data
@st.cache_data()
def download_data():
    "Download the ChEMBL database"
    current_file = Path(os.path.abspath(''))
    csv_file = current_file.parent / "Lecture05" / "chembl_drugs.csv"
    df = pd.read_csv(csv_file, sep= ";")
    return df

@st.cache_data()
def modify_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[str]]:
    "Modify the ChEMBL database to include Lipinski descriptors. Also get the Morgan fingerprints of each molecule."
    df = df.dropna(subset=['Smiles'])
    df['MW'], df['HBD'], df['HBA'], df['LogP'] = zip(*df['Smiles'].apply(calculate_descriptors))

    mfp = rdFingerprintGenerator.GetMorganGenerator(radius = 2, fpSize = 2048)
    fingerprints = df["Smiles"].apply(lambda x: mfp.GetFingerprint(Chem.MolFromSmiles(x)))
    return df, fingerprints

def calculate_descriptors(smiles: str) -> Tuple[float, int, int, float]:
    "Calculate Lipinski descriptors: molecular weight, H-bond donors, H-bond acceptors, and LogP"
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, None, None, None
    mw = ExactMolWt(mol)
    hbd = NumHDonors(mol)
    hba = NumHAcceptors(mol)
    logp = MolLogP(mol)
    return mw, hbd, hba, logp

def generate_3D(smiles):
    "Generate 3D coordinates from smiles"
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = 42
    AllChem.EmbedMolecule(mol)
    molstring= Chem.MolToMolBlock(mol)
    return molstring

def find_most_similar(fingerprints: List[str], ketcher_smiles: str, slider_val: int = 4) -> pd.DataFrame:
    mfp = rdFingerprintGenerator.GetMorganGenerator(radius = 2, fpSize = 2048)
    mol = Chem.MolFromSmiles(ketcher_smiles)
    if mol is None:
        return None
    ketcher_mol_fp = mfp.GetFingerprint(Chem.MolFromSmiles(ketcher_smiles))
    df["similarity"] = [round(Chem.DataStructs.TanimotoSimilarity(x, ketcher_mol_fp), 4) for x in fingerprints]
    return df.sort_values("similarity", ascending = False).head(slider_val)

# Visualize molecule 
def visualize_3D(molstring):
    "Visualize the molecule in 3D using stmol"
    w, h = 400, 400
    xyzview = py3Dmol.view(width=w,height=w)
    xyzview.addModel(molstring,'mol')
    xyzview.setStyle({'sphere':{'colorscheme':'cyanCarbon', 'scale':0.25}, 'stick':{'colorscheme':'cyanCarbon'}})
    xyzview.zoomTo()
    xyzview.spin()
    xyzview.setBackgroundColor('white')
    showmol(xyzview, height = w,width=w)


# APP
# Title
st.title('Are you drug like?!')
st.caption("Practical Proramming In Chemistry Week 11")
st.markdown("Draw a molecule and see how it stacks up against known drugs")

# Ketcher
# Optional draw from smiles
with st.expander("Draw Molecule From Smiles (optional)"):
    molecule = st.text_input("**Smiles**", "CCO")

# Ketcher
ketcher_smiles = st_ketcher(molecule, height=600) 

with st.expander("Smiles from Drawing"):
    st.markdown(ketcher_smiles) # Initialize a placeholder within the expander



# Download data, calculate descriptors and fingerprints
df = download_data()
df, fingerprints = modify_data(df)

# Sidebar
st.sidebar.markdown('# Options')
slider_val = st.sidebar.slider("Number of similar molecules", 0, 10, 4)

# 3D coordinates
col1, col2 = st.columns([1, 1])
with col1:
    st.header("3D")
    st.caption("Generate 3D coordinates for your molecule using rdkit's ETKDGv3 algorithm.")
    molstring = generate_3D(ketcher_smiles)
    if molstring is not None:
        visualize_3D(molstring)
    else:
        st.error('INVALID MOLECULE', icon="🚨")

# Lipinski stats
with col2: 
    st.header("Lipinski Stats")
    st.caption("How does your molecule compare to the average for FDA approved drugs?")
    mw, hbd, hba, logp = calculate_descriptors(ketcher_smiles)
    if mw is None:
        st.error('INVALID MOLECULE', icon="🚨")
    else:
        # Add metrics to compare our molecule to the average drug molecule
        metric_row1 = st.columns(2)
        metric_row2 = st.columns(2)
        tile1 = metric_row1[0].container(height = 120)
        tile1.metric("Molecular weight", round(mw, 2), round(mw - df["MW"].mean(), 2))
        tile2 = metric_row1[1].container(height = 120)
        tile2.metric("LogP", round(logp, 2), round(logp - df["LogP"].mean(), 2))
        tile3 = metric_row2[0].container(height = 120)
        tile3.metric("H-Bond Donors", hbd, round(hbd - df["HBD"].mean(), 2))
        tile4 = metric_row2[1].container(height = 120)
        tile4.metric("H-Bond Acceptors", hba, round(hba - df["HBA"].mean(), 2))

        # Lipinski's Rule of Five
        if mw < 500 and hbd < 5 and hba < 10 and logp < 5:
            st.success("Passes All of Lipinski's Rules", icon="✅")
        else:
            st.error("Does not pass Lipinski's Rule of Five", icon="🚨")

        # Lipinski's Rule of Five explanation
        st.markdown("Lipinski's rule of five is a rule of thumb to evaluate the oral availability of a molecule.")
        st.markdown("Lipinski's Rules:  \n1. \# H-Bond donors < 5 \n 2. \# H-bond acceptors < 10\n 3. MW < 500 daltons \n4. LogP < 5.") 
        st.markdown("As with any rule, there are many exceptions")

# Get the most similar molecules
st.header("Most similar drug molecules")
st.caption("Based on Tanimoto similarity of Morgan fingerprints")
most_similar_df = find_most_similar(fingerprints, ketcher_smiles, slider_val)
if most_similar_df is not None:
    if slider_val > 8: 
        height = 600 # Dynamically adjust height for visualization
    elif slider_val > 4:
        height = 500
    else:
        height = 300

    # use mols2grid to display our DataFrame with molecules
    raw_html = mols2grid.display(most_similar_df, subset = ["Name", "similarity"],
                                smiles_col = "Smiles")._repr_html_()
    components.html(raw_html, height = height)
else:
    st.error('INVALID MOLECULE', icon="🚨")


# Graph the distribution of molecular properties
st.header("Distribution of molecular properties")
st.caption("How does your molecule compare to FDA approved drugs?")
mw, hbd, hba, logp = calculate_descriptors(ketcher_smiles)
if mw == None:
    st.error('INVALID MOLECULE', icon="🚨")
else: 
    st.subheader("Molecular weight")
    fig = ff.create_distplot([df["MW"]], ["MW"], bin_size = 100)
    fig.add_vline(x = mw, line_dash="dash", line_color="lightgray", annotation_text="Your molecule")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("H-Bond Donors")
    fig = ff.create_distplot([df["HBD"]], ["HBD"], bin_size = 1)
    fig.add_vline(x = hbd, line_dash="dash", line_color="lightgray", annotation_text="Your molecule")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("H-Bond Acceptors")
    fig = ff.create_distplot([df["HBA"]], ["HBA"], bin_size = 1)
    fig.add_vline(x = hba, line_dash="dash", line_color="lightgray", annotation_text="Your molecule")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("LogP")
    fig = ff.create_distplot([df["LogP"]], ["LogP"], bin_size = 1)
    fig.add_vline(x = logp, line_dash="dash", line_color="lightgray", annotation_text="Your molecule")
    st.plotly_chart(fig, use_container_width=True)