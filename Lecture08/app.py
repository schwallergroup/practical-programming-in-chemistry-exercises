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
import plotly.figure_factory as ff
from typing import Tuple, List

# Put functions here 
def generate_3D(smiles):
    "Generate 3D coordinates from smiles"
    pass # your code here!! 

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

def calculate_descriptors(smiles: str) -> Tuple[float, int, int, float]:
    "Calculate Lipinski descriptors: molecular weight, H-bond donors, H-bond acceptors, and LogP"
    pass # your code here!!
    return mw, hbd, hba, logp

def download_data():
    "Download the ChEMBL database"
    pass # your code here!!
    return df

def modify_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[str]]:
    "Modify the ChEMBL database to include Lipinski descriptors. Also get the Morgan fingerprints of each molecule."
    return df, fingerprints

def find_most_similar(fingerprints: List[str], ketcher_smiles: str, slider_val: int = 4) -> pd.DataFrame:
    "Find the most similar molecules to the one drawn in Ketcher."
    pass # your code here!!
    return df

# Put title and caption here

# Put slider here

with st.expander("Draw Molecule From Smiles (optional)"):
    molecule = st.text_input("**Smiles**", "CCO") # initially, molecule = ""CCO"
# Put ketcher here

# Display ketcher smiles here

# Put dataset download here

# 3D coordinates
col1, col2 = st.columns([1, 1])
with col1:
    # Add header, caption 
    # Generate 3D coordinates
    if molstring is not None:
        # Visualize 3D coordinates
    else:
        # Add error message


# Lipinski Descriptors
with col2: 
    # Add header, caption
    # Calculate Lipinski descriptors
    if mw is None:
        # Add error message
    else:
        # Create formatting for metrics
        metric_row1 = st.columns(2)
        metric_row2 = st.columns(2)
        tile1 = metric_row1[0].container(height = 120) # Put a container in the first row, first column
        tile1.metric() # Title, value, delta) # Add a metric to that container
        # repeat for tiles 2-4

        # Lipinski's Rule of Five
        if # your code here!!:
            st.success("Passes All of Lipinski's Rules", icon="✅")
        else:
            st.error("Does not pass Lipinski's Rule of Five", icon="🚨")

        # Lipinski's Rule of Five explanation
        st.markdown("Lipinski's rule of five is a rule of thumb to evaluate the druglikeness of a molecule.")
        st.markdown("Lipinski's Rules:  \n1. \# H-Bond donors < 5 \n 2. \# H-bond acceptors < 10\n 3. MW < 500 daltons \n4. LogP < 5.") 
        st.markdown("As with any rule, there are many exceptions")


# Display the top n most similar molecules

# Graph the distributions of molecular properties
# Add sensible header and caption
mw, hbd, hba, logp = calculate_descriptors(ketcher_smiles)
if mw == None:
    st.error('INVALID MOLECULE', icon="🚨")
else: 
    # Finish the followng
    st.subheader("Molecular weight")
    fig =  # your code here!!
    st.plotly_chart(fig, use_container_width=True)
