from DNA import DnaSequence
from command import Command


class Slice(Command):
    def __init__(self, params):
        super().__init__()
        self.params = params
        seq_details = Command.get_seq_details(self, self.params[0])
        self.sequence = seq_details[0]
        self.sequence_id = seq_details[1]
        self.sequence_name = seq_details[2]

        self.from_ind = self.check_num(params[1]) - 1
        self.to_ind = self.check_num(params[2]) - 1
        # if self.from_ind < 1 or self.to_ind >= len(self.sequence):
        #     raise IndexError("Index out of range")
        self.slice_seq = self.sequence[self.from_ind:self.to_ind]

        if len(params) > 3:
            self.new_sequence_name = params[4][1:]
            if self.new_sequence_name == '@':
                self.new_sequence_name = Command.get_new_name(self, self.sequence_name, 's')

    def check_num(self, word):
        if word.isnumeric():
            return int(word)
        raise Exception("You have to insert a number")

    def process(self):
        if len(self.params) > 3:
            slice_dna_seq = DnaSequence(self.slice_seq)
            slice_seq_id = self.db.get_new_id()
            self.db.insert_dna_seq(self.new_sequence_name, slice_dna_seq.get_dna_seq())
            return "[{}] {}: {}".format(slice_seq_id, self.new_sequence_name, slice_dna_seq)
        self.db.set_sequence(self.sequence_id, self.slice_seq)
        slice_dna_seq = self.db.get_seq_by_id(self.sequence_id)
        return "[{}] {}: {}".format(self.sequence_id, self.sequence_name, slice_dna_seq)
