def binaryToDna(lis, dna1, dna2):  # Wandelt Binärcode in 2 DNA-Stränge um
    for o in lis:
        if o == '0000':
            dna1.append("A")
            dna2.append("A")
        elif o == '0001':
            dna1.append("A")
            dna2.append("C")
        elif o == '0010':
            dna1.append("A")
            dna2.append("T")
        elif o == '0011':
            dna1.append("A")
            dna2.append("G")
        elif o == '0100':
            dna1.append("T")
            dna2.append("A")
        elif o == '0101':
            dna1.append("T")
            dna2.append("C")
        elif o == '0110':
            dna1.append("T")
            dna2.append("T")
        elif o == '0111':
            dna1.append("T")
            dna2.append("G")
        elif o == '1000':
            dna1.append("C")
            dna2.append("G")
        elif o == '1001':
            dna1.append("C")
            dna2.append("T")
        elif o == '1010':
            dna1.append("C")
            dna2.append("C")
        elif o == '1011':
            dna1.append("C")
            dna2.append("A")
        elif o == '1100':
            dna1.append("G")
            dna2.append("G")
        elif o == '1101':
            dna1.append("G")
            dna2.append("T")
        elif o == '1110':
            dna1.append("G")
            dna2.append("C")
        elif o == '1111':
            dna1.append("G")
            dna2.append("A")
    return dna1, dna2


def dnaToBinary(dna1, dna2):  # Wandelt DNA in Binärcode um
    bin = []
    for n, n2 in zip(dna1, dna2):
        if n == "A" and n2 == 'A':
            bin.append("0000")
        elif n == 'A' and n2 == 'C':
            bin.append("0001")
        elif n == 'A' and n2 == 'T':
            bin.append("0010")
        elif n == 'A' and n2 == 'G':
            bin.append("0011")
        elif n == 'T' and n2 == 'A':
            bin.append("0100")
        elif n == 'T' and n2 == 'C':
            bin.append("0101")
        elif n == 'T' and n2 == 'T':
            bin.append("0110")
        elif n == 'T' and n2 == 'G':
            bin.append("0111")
        elif n == 'C' and n2 == 'G':
            bin.append("1000")
        elif n == 'C' and n2 == 'T':
            bin.append("1001")
        elif n == 'C' and n2 == 'C':
            bin.append("1010")
        elif n == 'C' and n2 == 'A':
            bin.append("1011")
        elif n == 'G' and n2 == 'G':
            bin.append("1100")
        elif n == 'G' and n2 == 'T':
            bin.append("1101")
        elif n == 'G' and n2 == 'C':
            bin.append("1110")
        elif n == 'G' and n2 == 'A':
            bin.append("1111")
    return bin
