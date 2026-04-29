import re
from rdkit import Chem

def remove_atom_mapping(smiles: str) -> str:
    # from: https://github.com/rxn4chemistry/rxn-chemutils/blob/main/src/rxn/chemutils/utils.py, MIT
    """
    Remove the atom mapping of a reaction SMILES.

    The resulting SMILES strings will still contain brackets and it may be
    advisable to canonicalize them or clean them up as a postprocessing step.

    Args:
        smiles: SMILES string potentially containing mapping information.

    Returns:
        A SMILES string without atom mapping information.
    """

    # We look for ":" followed by digits before a "]" not coming after an "*"
    return re.sub(r"(?<=[^\*])(:\d+)]", "]", smiles)

def canonicalize_smiles(smiles: str) -> str:
    """
    Canonicalize SMILES.

    Args:
        smiles: SMILES string, potentially not canonical 

    Returns:
        A canonical SMILES string.
    """
    mol = Chem.MolFromSmiles(smiles)

    if mol is not None:
        return Chem.MolToSmiles(mol)

    return ''


def remove_atom_mapping_and_canonicalize_rxn_smiles(smiles: str) -> str:
    """
    Remove atom mapping and canonicalize reaction SMILES.

    Args:
        smiles: reaction SMILES string, potentially not canonical with atom mapping. 

    Returns:
        A canonical reaction SMILES string without atom mapping.
    """

    smiles_without_atom_mapping = remove_atom_mapping(smiles)
    
    rxn_parts = smiles_without_atom_mapping.split('>')

    can_rxn_parts = [canonicalize_smiles(smiles) for smiles in rxn_parts]

    return '>'.join(can_rxn_parts)

rxn_smiles_with_atom_mapping = '[CH3:17][S:14](=[O:15])(=[O:16])[N:11]1[CH2:10][CH2:9][N:8](Cc2ccccc2)[CH2:13][CH2:12]1.C1CCCCC1>[OH-].[OH-].[Pd+2].CCO>[CH3:17][S:14](=[O:15])(=[O:16])[N:11]1[CH2:10][CH2:9][NH:8][CH2:13][CH2:12]1'

print(f"RXN SMILES with atom mapping: {rxn_smiles_with_atom_mapping}")
print("*** Remove atom mapping ***")
rxn_smiles_without_atom_mapping = remove_atom_mapping_and_canonicalize_rxn_smiles(rxn_smiles_with_atom_mapping)
print(f"RXN SMILES without atom mapping: {rxn_smiles_without_atom_mapping}")
