codon_table = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
    "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",

    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",

    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",

    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}


class Codon(object):
    def __init__(self):
        self.sequence = None
        self.valid_check = None
        self.remainder = None
        self.valid_bases = ["A", "U", "G", "C"]
        self.amino_acids = []
        self.codons = []
        self.codon_table = codon_table

    # ユーザーからのインプットを受け付ける
    def sequence_input(self):
        self.sequence = input("塩基配列を入力してください: ").upper()
        return self.sequence

    # もしAUGC以外の数値が含まれている場合はエラーを返す
    def sequence_validation(self):
        for base in self.sequence:
            if base not in self.valid_bases:
                print("エラー: 塩基配列にはA, U, G, C以外の文字が含まれています。")
                self.valid_check = False
                break
        self.valid_check = True

    # インプットの文字数を3で割る。この後、割った時の余りによって条件分岐をする。
    def sequence_remainder(self):
        if not self.valid_check:
            print("エラー: 塩基配列にはA, U, G, C以外の文字が含まれています。")
            return
        else:
            self.remainder = len(self.sequence) % 3
        return self.remainder
    
    # 余りが0の場合: 文字列を3文字づつに区切る
    # 余りが1の場合: 最後の1文字を切り捨てて文字列を3文字づつに区切る
    # 余りが2の場合: 最後の2文字を切り捨てて文字列を3文字づつに区切る
    def sequence_chopper(self):
        if self.remainder == 0:
            self.codons = [self.sequence[i:i+3] for i in range(0, len(self.sequence), 3)]
        elif self.remainder == 1:
            self.codons = [self.sequence[i:i+3] for i in range(0, len(self.sequence)-1, 3)]
        elif self.remainder == 2:
            self.codons = [self.sequence[i:i+3] for i in range(0, len(self.sequence)-2, 3)]
        return self.codons


    # コドン表を参照してアミノ酸を返す
    def sequence_translator(self):
        self.amino_acids = []
        stop_codons = ["UAA", "UAG", "UGA"]
        start_found = False

        for codon in self.codons:

            if start_found == False:
                self.amino_acids.append("-")
                if codon == "AUG":
                    start_found = True
                    self.amino_acids.append(self.codon_table[codon])
                continue
            if codon in stop_codons:
                self.amino_acids.append("-")
                break
            else:
                self.amino_acids.append(self.codon_table[codon])

        self.amino_acids = "".join(self.amino_acids)
        return self.amino_acids
