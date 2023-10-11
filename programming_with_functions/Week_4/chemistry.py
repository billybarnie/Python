from formula import parse_formula

def main():
    
    molecule = input("What molecule formula are you working with? ")
    grams = float(input("What is the mass in grams of the sample size? "))


    molecule_table = make_periodic_table()

    molecule = parse_formula(molecule, molecule_table)

    molar_mass = compute_molar_mass(molecule, molecule_table)

    proton = float(compute_proton(molecule, molecule_table))

    protons = proton * grams
    moles = grams / molar_mass

    print(f"{molar_mass:.5f} grams/mole")
    print(f"{moles:.5f} moles")
    print()
    print(f"The molecule formula has a base amount of {proton:.0f} protons")
    print(f"The sample size has {protons} protons")


def make_periodic_table():

    periodic_table_dict = {
    "Ac":	[89, "Actinium",	227],
    "Ag":	[47, "Silver",	107.8682],
    "Al":	[13, "Aluminum",	26.9815386],
    "Ar":	[18, "Argon",	39.948],
    "As":	[33, "Arsenic",	74.9216],
    "At":	[85, "Astatine",	210],
    "Au":	[79, "Gold",	196.966569],
    "B":	[5, "Boron",	10.811],
    "Ba":	[56, "Barium",	137.327],
    "Be":	[4, "Beryllium",	9.012182],
    "Bi":	[83, "Bismuth",	208.9804],
    "Br":	[35, "Bromine",	79.904],
    "C":	[6, "Carbon",	12.0107],
    "Ca":	[20, "Calcium",	40.078],
    "Cd":	[48, "Cadmium",	112.411],
    "Ce":	[58, "Cerium",	140.116],
    "Cl":	[17, "Chlorine",	35.453],
    "Co":	[27, "Cobalt",	58.933195],
    "Cr":	[24, "Chromium",	51.9961],
    "Cs":	[55, "Cesium",	132.9054519],
    "Cu":	[29, "Copper",	63.546],
    "Dy":	[66, "Dysprosium",	162.5],
    "Er":	[68, "Erbium",	167.259],
    "Eu":	[63, "Europium",	151.964],
    "F":	[9, "Fluorine",	18.9984032],
    "Fe":	[26, "Iron",	55.845],
    "Fr":	[87, "Francium",	223],
    "Ga":	[31, "Gallium",	69.723],
    "Gd":	[64, "Gadolinium",	157.25],
    "Ge":	[32, "Germanium",	72.64],
    "H":	[1, "Hydrogen",	1.00794],
    "He":	[2, "Helium",	4.002602],
    "Hf":	[72, "Hafnium",	178.49],
    "Hg":	[80, "Mercury",	200.59],
    "Ho":	[67, "Holmium",	164.93032],
    "I":	[53, "Iodine",	126.90447],
    "In":	[49, "Indium",	114.818],
    "Ir":	[77, "Iridium",	192.217],
    "K":	[19, "Potassium",	39.0983],
    "Kr":	[36, "Krypton",	83.798],
    "La":	[57, "Lanthanum",	138.90547],
    "Li":	[3, "Lithium",	6.941],
    "Lu":	[71, "Lutetium",	174.9668],
    "Mg":	[12, "Magnesium",	24.305],
    "Mn":	[25, "Manganese",	54.938045],
    "Mo":	[42, "Molybdenum",	95.96],
    "N":	[7, "Nitrogen",	14.0067],
    "Na":	[11, "Sodium",	22.98976928],
    "Nb":	[41, "Niobium",	92.90638],
    "Nd":	[60, "Neodymium",	144.242],
    "Ne":	[10, "Neon",	20.1797],
    "Ni":	[28, "Nickel",	58.6934],
    "Np":	[93, "Neptunium",	237],
    "O":	[8, "Oxygen",	15.9994],
    "Os":	[76, "Osmium",	190.23],
    "P":	[15, "Phosphorus",	30.973762],
    "Pa":	[91, "Protactinium",	231.03588],
    "Pb":	[82, "Lead",	207.2],
    "Pd":	[46, "Palladium",	106.42],
    "Pm":	[61, "Promethium",	145],
    "Po":	[84, "Polonium",	209],
    "Pr":	[59, "Praseodymium",	140.90765],
    "Pt":	[78, "Platinum",	195.084],
    "Pu":	[94, "Plutonium",	244],
    "Ra":	[88, "Radium",	226],
    "Rb":	[37, "Rubidium",	85.4678],
    "Re":	[75, "Rhenium",	186.207],
    "Rh":	[45, "Rhodium",	102.9055],
    "Rn":	[86, "Radon",	222],
    "Ru":	[44, "Ruthenium",	101.07],
    "S":	[16, "Sulfur",	32.065],
    "Sb":	[51, "Antimony",	121.76],
    "Sc":	[21, "Scandium",	44.955912],
    "Se":	[34, "Selenium",	78.96],
    "Si":	[14, "Silicon",	28.0855],
    "Sm":	[62, "Samarium",	150.36],
    "Sn":	[50, "Tin",	118.71],
    "Sr":	[38, "Strontium",	87.62],
    "Ta":	[73, "Tantalum",	180.94788],
    "Tb":	[65, "Terbium",	158.92535],
    "Tc":	[43, "Technetium",	98],
    "Te":	[52, "Tellurium",	127.6],
    "Th":	[90, "Thorium",	232.03806],
    "Ti":	[22, "Titanium",	47.867],
    "Tl":	[81, "Thallium",	204.3833],
    "Tm":	[69, "Thulium",	168.93421],
    "U":	[92, "Uranium",	238.02891],
    "V":	[23, "Vanadium",	50.9415],
    "W":	[74, "Tungsten",	183.84],
    "Xe":	[54, "Xenon",	131.293],
    "Y":	[39, "Yttrium",	88.90585],
    "Yb":	[70, "Ytterbium",	173.054],
    "Zn":	[30, "Zinc",	65.38],
    "Zr":	[40, "Zirconium",	91.224]
    }

    return periodic_table_dict

# Indexes for inner lists in the periodic table
PROTON_INDEX = 0
NAME_INDEX = 1
ATOMIC_MASS_INDEX = 2

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
    # Separate the inner list into symbol and quantity.
    atomic_mass = 0 

    for list in symbol_quantity_list:
        symbol = list[SYMBOL_INDEX]
        quantity = list[QUANTITY_INDEX]
        # Get the atomic mass for the symbol from the dictionary.
        for key, values in periodic_table_dict.items():
            if symbol == key:
                # Multiply the atomic mass by the quantity. 
                # # Add the product into the total molar mass.
                atomic_mass += values[ATOMIC_MASS_INDEX] * quantity

    # Return the total molar mass.
    return atomic_mass

def compute_proton(symbol_quantity_list, periodic_table_dict):
    proton = 0
        
    for list in symbol_quantity_list:
        symbol = list[SYMBOL_INDEX]
        quantity = list[QUANTITY_INDEX]

        for key, values in periodic_table_dict.items():
            if symbol == key:
                proton += values[PROTON_INDEX] * quantity

    return proton

if __name__ == "__main__":
    main()