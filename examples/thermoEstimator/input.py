database(
    thermoLibraries = ['primaryThermoLibrary', 'GRI-Mech3.0']   
)

species(
    label='DIPK',
    multiplicity = 1,
    structure=SMILES("CC(C)C(=O)C(C)C"),
)
species(
    label='O2',
    multiplicity = 3,
    structure=SMILES("[O][O]"),
)
species(
    label='R_tert',
    multiplicity = 2,
    structure=SMILES("CC(C)C(=O)[C](C)C"),
)
species(
    label='R_pri',
    multiplicity = 2,
    structure=SMILES("CC(C)C(=O)C(C)[CH2]"),
)
species(
    label='Cineole',
    multiplicity = 1,
    structure=SMILES('CC12CCC(CC1)C(C)(C)O2'),
)

quantumMechanics(
    software='mopac',
    fileStore='QMfiles', # relative to where you run it? defaults to inside the output folder.
    scratchDirectory = None, # not currently used
    onlyCyclics = True,
    maxRadicalNumber = 0,
)
