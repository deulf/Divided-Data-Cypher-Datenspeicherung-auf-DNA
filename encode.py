from reedsolo import RSCodec, ReedSolomonError
from dnaTools import binaryToDna
import utilities

def flattenDNA(dna, strang):
    dna = utilities.shortening(dna)
    while True:  # Wendet solange Funktion flatten an bis dna1 einfache Liste ist
        try:
            ''.join(dna)
            break
        except TypeError:
            dna = utilities.flatten(dna)
    dna = utilities.addIndex(dna, strang)
    # dna = utilities.wiederholungEntfernung(dna)
    return dna

def encode(file):
    with open(file) as f:  # Öffnet und speichert Inhalt der Textdatei in "file"
        file = f.read()
    file = bytes(file, "utf-8") # Das Programm funktioniert für alle Zeichenketten unter 75 Zeichen
    rsc = RSCodec(12)  # Setzt die Errorkorrerkturzahl in Höhe von 12
    n = rsc.encode(file)  # Verschlüsselt Inhalt von "file" mit Reed-Solomon Codes
    n = bin(int.from_bytes(n, 'big'))  # Wandelt String in Binärcode um
    chunks = utilities.re.findall('....', n)  # Teilt Binärcode in 4rer Blöcke
    dna1 = []
    dna2 = []
    binaryToDna(chunks, dna1, dna2)  # Binärcode wird in dna1 und dna2 als DNA-Sequenz geschrieben
    dna1 = flattenDNA(dna1,"Lead")  # Bearbeitet dna1 als Hauptstrang
    dna2 = flattenDNA(dna2,"Lagg")  # Bearbeitet dna2 als Nebenstrang
    dna = utilities.flatten([dna1, dna2])
    return dna
