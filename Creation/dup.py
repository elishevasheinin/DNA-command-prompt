from DNA import DnaSequence
from command import Command


class Dup(Command):

    def __init__(self, params):
        super().__init__()
        seq_details = Command.get_seq_details(self, params[0])
        self.sequence = seq_details[0]
        dna_name = seq_details[2]

        if len(params) > 1:
            self.new_sequence_name = params[1]
        else:
            self.new_sequence_name = Command.get_new_name(self, dna_name)

    def process(self):
        dup_dna_seq = DnaSequence(self.sequence)
        return self.new_sequence_name, dup_dna_seq
