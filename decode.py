from reedsolo import RSCodec, ReedSolomonError
from dnaTools import dnaToBinary
from utilities import flatten


def decode(dna):
    dna3 = []
    for i in dna:  # Erstellt Liste aus [DNA, zugehörige DNA, Index] mit allen Strängen
        binnum = dnaToBinary(i[:3], "ATC")
        binnum = (int((''.join(binnum)), 2))
        for i2 in dna:
            binnum2 = dnaToBinary(i2[:3], "ATC")
            binnum2 = (int((''.join(binnum2)), 2))
            if binnum - 2816 == binnum2:  # Testet dna1 Index 1 und dna2 Index 1
                dna3.extend([[i, i2, binnum]])
                continue
            binnum2 = dnaToBinary(i2[-3:], "ATC")
            binnum2 = (int((''.join(binnum2)), 2))
            if binnum - 2816 == binnum2:  # Testet dna1 Index 1 und dna2 Index 2
                dna3.extend([[i, i2, binnum]])
                continue
            binnum = dnaToBinary(i[-3:], "ATC")
            binnum = (int((''.join(binnum)), 2))
            if binnum - 2816 == binnum2:  # Testet dna1 Index 2 und dna2 Index 2
                dna3.extend([[i, i2, binnum]])
                continue
            binnum2 = dnaToBinary(i2[:3], "ATC")
            binnum2 = (int((''.join(binnum2)), 2))
            if binnum - 2816 == binnum2:  # Testet dna1 Index 2 und dna2 Index 1
                dna3.extend([[i, i2, binnum]])
                continue
    dna3 = sorted(dna3, key=lambda i: i[2], reverse=True)  # Sortiert DNA-Stränge nach Index in richtige Reihenfolge
    bin = ["0b10"]  # Liste beginnt mit 0b10 damit Python Binärcode erkennt
    for i in dna3:  # Wandelt DNA-Stränge ohne Index in Binärcode um
        dna1 = i[0][3:-3]
        dna2 = i[1][3:-3]
        bin.append(dnaToBinary(dna1, dna2))
    bin.append("0")  # Fügt 0 an Binärcode an da dieser sonst nicht valide ist
    bin = flatten(bin)
    n = int((''.join(bin)), 2)  # Wandelt Liste von in Binär übersetzten DNA-Strang in Integer um
    output = n.to_bytes((n.bit_length() + 7) // 8, "big")
    rsc = RSCodec(12)
    output = (rsc.decode(output)[0]).decode()  # Entschlüsselt Reed-Solomon Codes von "output"
    return output
