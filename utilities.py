import re
from dnaTools import binaryToDna

def flatten(t):  # Wandelt n-dimensionale Liste in (n-1)-dimensionale Liste um
    return [item for sublist in t for item in sublist]

def wiederholungEntfernung(dna):  # Entfernt Sequenzen von über 4 Nukleotiden hintereinander
    dna2 = []
    for strand in dna:
        strand = strand.replace("AAAA", "AATA")
        strand = strand.replace("TTTT", "TTAT")
        strand = strand.replace("CCCC", "CCGC")
        strand = strand.replace("GGGG", "GGCG")
        dna2.append(strand)
    return dna2


def shortening(dna):  # Teilt DNA-Stränge in mehrere Teile, falls die einzelnen Stränge über 50 bp lang sind
    dna2 = []
    dna = ''.join(dna)
    if len(dna) > 44:
        split = -((-len(dna)) // 2)
        d1, d2 = dna[:split], dna[split:]
        dna2.extend([shortening(d1), shortening(d2)])
    else:
        dna2.append(dna)
    return dna2


def addIndex(dna, strang):  # Fügt an Beginn und Ende von Strängen einen Index an
    if strang == "Lead":
        index = 4095
    else:
        index = 2045
    dna2 = []
    for s in dna:
        indexlis = re.findall('....', f'{index:012b}')  # Wandelt Index in Binärzahl um
        indexdna = [''.join(ele) for ele in (binaryToDna(indexlis, [], []))][0]
        s = indexdna + s + indexdna  # Wandelt Binärzahl in Nukleotide um und hängt diese an einzelne DNA-Strang
        dna2.append(s)
        index = index - 4
    return dna2
