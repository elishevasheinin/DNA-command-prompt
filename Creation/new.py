from DNA import DnaSequence


class New:
    __num_of_unnamed_new_sequences = 0

    def __init__(self, params):
        self.sequence = params[0]
        if len(params) > 1:
            self.sequence_name = params[1]
        else:
            New.__num_of_unnamed_new_sequences += 1
            self.sequence_name = 'seq{}'.format(New.__num_of_unnamed_new_sequences)

    def process(self):
        dna_seq = DnaSequence(self.sequence)
        return self.sequence_name, dna_seq
