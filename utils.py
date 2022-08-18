import os
import sys
import cclib
import numpy as np




def check(file,check_string, count=False):
    
    """ 
    Checks if a the specified string is contained within a given file. If count is not specified only presence is checked, otherwise if count is an integer
    then the function checks that the string is contained for the given number of counts.

    Arguments:
    file (file): any text file
    check_string (str): Check if file contains this string
    count: Number of times to check for check_string. If False then just checks to see if string is present.
    
    Returns:
    True if check string is present and count=False. If count=n, then returns true if string is contained for that specified number of times. 
    False if check_string is not present or if not present for the specified number of counts.

    """  
    
    with open(file) as f:
        if not count:
            return check_string in f.read()
        else: 
            return  f.read().count(check_string)==count


def checkvibs(vibs,asint=False):
    """ 
    checks the vibrational frequencies of a DFT calculation to make sure that they are all
    positive and thus there are no imaginary frequencies.

    Arguments:
    vibs (cclib vibrational frequencies): vibrational requencies obtained from gaussian output file using cclib

    Returns:
    True if all frequencies are positive. False otherwise. 

    """
    if asint:
        return int(all(vibs > 0))
    else:
        return all(vibs > 0)
    

def no_to_symbol(no):
    
    no_to_symbol_dict={
    1:'H',
    6:'C',
    7:'N',
    8:'O',
    9:'F',
    15:'P',
    16:'S',
    17:'Cl',
    35:'Br',
    53:'I'    
    }
    
    assert no in no_to_symbol_dict, "ATOMIC NUMBER NOT IN CURRENT DICTIONARY"
    
    
    return no_to_symbol_dict[no]

def make_xyz_from_array(file, xyz, labels_array, include_charge=False,charge=0):
    """
    Makes an XYZ file from the final geometry of a gaussian calulcation in the form of an array.
    Along with an array of all the atom labels in the same order as the array of positions
    
    Arguments:
    xyz: Nx3 array where N is the number of atoms and 3 is for x,y and z coordinates
    
    """
    n,m=np.shape(xyz)
    writepath = os.path.join(os.getcwd(),f'{file}.xyz')
    mode = 'a' if os.path.exists(writepath) else 'w'
    
    with open(writepath, mode) as f:
        f.truncate(0)
        f.write(f'{len(labels_array)}\n')
        
        if include_charge:
            f.write(f'charge={charge}=\n')

        for i in range(n):
            f.write(f'{labels_array[i]}{xyz[i,0]:>17,.6f}{xyz[i,1]:>15,.6f}{xyz[i,2]:>15,.6f}\n')
        f.close()
    

def make_xyz_from_output(file):

    
    """
    Makes an XYZ file from the final geometry of a gaussian calulcation obtained from the output file.
    
    Arguments:
    Gaussian output text file from a geom and freq calculation
    
    """
    
    no_to_symbol_dict={
    1:'H',
    6:'C',
    7:'N',
    8:'O',
    9:'F',
    15:'P',
    16:'S',
    17:'Cl'    
    }
    
    
    temp_data=cclib.io.ccread(file)
    xyz=temp_data.atomcoords[-1,:,:]
    atnos=temp_data.atomnos
    atsymbs=[no_to_symbol_dict[x] for x in atnos]
    n,m=np.shape(xyz)
    
    filename=os.path.basename(os.path.normpath(file))
    split_file=filename.split('.')
    base_file=split_file[0]
    
    writepath = os.path.join(os.getcwd(),f'{base_file}_converged.xyz')
    mode = 'a' if os.path.exists(writepath) else 'w'

    with open(writepath, mode) as f:
        f.truncate(0)
        f.write(f'{len(atsymbs)}')
        f.write('\n\n')
        for i in range(n):
            f.write(f'{atsymbs[i]}{xyz[i,0]:>17,.6f}{xyz[i,1]:>15,.6f}{xyz[i,2]:>15,.6f}\n')
        f.close()
        
        
        
def GetCoordsFromMolBlock(mb):
    
    
    header_lines=4
    
    lines=mb.splitlines()
    n=int(lines[3].split()[0])
    end_line=header_lines+n
    
    xyz=np.zeros((n,4),dtype='object')
    for i,line in enumerate(lines[header_lines:end_line]):
        split_line=line.split()

        xyz[i,0]=split_line[3]
        xyz[i,1]=float(split_line[0])
        xyz[i,2]=float(split_line[1])
        xyz[i,3]=float(split_line[2])
        
    return xyz


def mol_with_atom_index(mol):
    for atom in mol.GetAtoms():
        atom.SetAtomMapNum(atom.GetIdx())
    return mol

