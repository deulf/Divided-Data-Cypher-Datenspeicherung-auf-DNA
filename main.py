import encode
import decode


def main():
    dna = encode.encode("fox.txt")
    print(dna)
    print(decode.decode(dna))


if __name__ == "__main__":
    main()
