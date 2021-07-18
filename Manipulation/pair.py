from DNA import DnaSequence
from command import Command


class Pair(Command):
    def __init__(self, params):
        super().__init__()
        self.params = params
        seq_details = Command.get_seq_details(self, self.params[0])
        self.sequence = seq_details[0]
        self.sequence_id = seq_details[1]
        self.sequence_name = seq_details[2]
        if len(self.params) > 1:
            self.new_sequence_name = self.params[2][1:]
            if self.new_sequence_name == '@':
                self.new_sequence_name = Command.get_new_name(self, self.sequence_name, 'p')

    def replace_chars(self):
        seq_in_list = list(self.sequence)
        for i in range(len(seq_in_list)):
            if seq_in_list[i] == 'A':
                seq_in_list[i] = 'T'
            elif seq_in_list[i] == 'C':
                seq_in_list[i] = 'G'
            elif seq_in_list[i] == 'G':
                seq_in_list[i] = 'C'
            elif seq_in_list[i] == 'T':
                seq_in_list[i] = 'A'
        self.sequence = "".join(seq_in_list)

    def process(self):
        self.replace_chars()
        if len(self.params) > 1:
            pair_dna_seq = DnaSequence(self.sequence)
            pair_seq_id = self.db.get_new_id()
            self.db.insert_dna_seq(self.new_sequence_name, pair_dna_seq.get_dna_seq())
            return "[{}] {}: {}".format(pair_seq_id, self.new_sequence_name, pair_dna_seq)
        self.db.set_sequence(self.sequence_id, self.sequence)
        pair_dna_seq = self.db.get_seq_by_id(self.sequence_id)
        return "[{}] {}: {}".format(self.sequence_id, self.sequence_name, pair_dna_seq)
