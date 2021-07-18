class DnaSequence:
    def __init__(self, dna_str):
        if type(dna_str) != str:
            raise TypeError("You have to insert string")
        if not self.check_validation(dna_str):
            raise ValueError("The string should be with letters A, C, G, or T")
        self.__dna_seq = dna_str

    def get_dna_seq(self):
        return self.__dna_seq

    def insert(self, val, ind):
        if type(ind) != int:
            raise TypeError
        if ind >= len(self.__dna_seq):
            raise IndexError("Index out of range")
        self.__dna_seq = self.__dna_seq[:ind] + val + self.__dna_seq[ind:]

    def assignment(self, new_str): #=
        if type(new_str) == str:
            if not self.check_validation(new_str):
                raise ValueError("The string should be with letters A, C, G, or T")
            self.__dna_seq = new_str
        elif type(new_str) is DnaSequence:
            self.__dna_seq = new_str.get_dna_seq
        else:
            raise TypeError("You have to insert string")

    def __str__(self): #print
        return self.__dna_seq

    def __eq__(self, other): #==
        if type(other) == DnaSequence:
            return self.__dna_seq == other.get_dna_seq
        elif type(other) == str:
            if not self.check_validation(other.get_dna_seq):
                raise ValueError("The string should be with letters A, C, G, or T")
            return self.__dna_seq == other
        else:
            raise TypeError

    def __ne__(self, other): #!=
        if type(other) == DnaSequence:
            return self.__dna_seq != other.get_dna_seq
        elif type(other) == str:
            return self.__dna_seq != other
        else:
            raise TypeError

    def __getitem__(self, item): #[]
        if type(item) != int:
            raise TypeError
        if item >= len(self.__dna_seq):
            raise IndexError("Index out of range")
        return self.__dna_seq[item]

    def __setitem__(self, key, value): #[]
        if type(key) != int:
            raise TypeError
        if key >= len(self.__dna_seq):
            raise IndexError("Index out of range")
        if type(value) != str:
            raise TypeError("You have to insert string")
        if not self.check_validation(value):
            raise ValueError("The string should be with letters A, C, G, or T")
        self.__dna_seq[key] = value

    def __len__(self): #len
        return len(self.__dna_seq)

    def check_validation(self, str):
        return all([char in ['A', 'G', 'C', 'T'] for char in str])
