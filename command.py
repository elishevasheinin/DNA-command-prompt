from database import Database


class Command:

    def __init__(self):
        self.db = Database()

    def check_string(self, seq):
        if seq[0] != '@' and seq[0] != '#':
            raise Exception("Must start with @ or #")

    def get_seq_details(self, seq):
        if seq[0] == '@':
            seq_name = seq[1:]
            sequence = self.db.get_seq_by_name(seq_name)
            seq_id = self.db.get_seq_id(sequence)
        # elif seq[0] == '#':
        else:
            seq_id = int(seq[1:])
            sequence = self.db.get_seq_by_id(seq_id)
            seq_name = self.db.get_dna_names()[seq_id - 1]
        return sequence, seq_id, seq_name

    def get_new_name(self, seq, char=''):
        dna_names = self.db.get_dna_names()
        name = seq
        i = 1
        while name in dna_names:
            name = seq + '_{}{}'.format(char, i)
            i += 1
        return name
