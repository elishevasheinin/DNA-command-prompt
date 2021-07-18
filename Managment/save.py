from command import Command


class Save(Command):
    def __init__(self, params):
        super().__init__()
        self.params = params
        seq_details = Command.get_seq_details(self, self.params[0])
        self.sequence = seq_details[0]
        self.sequence_id = seq_details[1]
        self.sequence_name = seq_details[2]
        if len(self.params) == 2:
            self.file_name = self.params[1]
        else:
            self.file_name = self.sequence_name + '.rawdna'

    def process(self):
        with open(self.file_name, 'a') as file:
            file.write(self.sequence + '\n')
        return "Saved"
