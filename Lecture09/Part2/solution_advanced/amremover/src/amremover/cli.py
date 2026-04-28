# sample usage: `amremover '[CH3:17][S:14](=[O:15])(=[O:16])[N:11]1[CH2:10][CH2:9][N:8](Cc2ccccc2)[CH2:13][CH2:12]1.C1CCCCC1>[OH-].[OH-].[Pd+2].CCO>[CH3:17][S:14](=[O:15])(=[O:16])[N:11]1[CH2:10][CH2:9][NH:8][CH2:13][CH2:12]1'`

import typer

from .utils import remove_atom_mapping_and_canonicalize_rxn_smiles

def run():
    typer.run(main)


def main(
    rxn_smiles: str = typer.Argument(..., help="Reaction SMILES with atom-mapping"),
    verbose: bool = typer.Option(False, "--verbose", help="Print additional verbose output.."),
    ):
    """Removes atom-mapping from reaction SMILES."""
    if verbose:
        print(f"RXN SMILES with atom mapping: {rxn_smiles}")
        print("*** Remove atom mapping ***")

    rxn_smiles_without_atom_mapping = remove_atom_mapping_and_canonicalize_rxn_smiles(rxn_smiles)

    print(rxn_smiles_without_atom_mapping)

if __name__ == "__main__":
    run()