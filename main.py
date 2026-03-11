from functions import Codon

if __name__ == "__main__":
    codon = Codon()
    codon.sequence_input()
    codon.sequence_validation()
    codon.sequence_remainder()
    codon.sequence_chopper()
    codon.sequence_translator()

    print("コドン: ", codon.codons)
    print("アミノ酸: ", codon.amino_acids)