from DNA import DnaSequence


class Load:

    def __init__(self, params):
        self.file = params[0]
        if len(self.file.split('.')) == 1:  # there is no suffix for the file
            self.file += '.rawdna'
        if len(params) > 1:
            self.sequence_name = params[1]
        else:
            self.sequence_name = self.file.split('.')[0]

    def process(self):
        with open(self.file, 'r') as file:
            sequence = file.read().replace('\n', '')
            dna_sequence = DnaSequence(sequence)
        return self.sequence_name, dna_sequence
