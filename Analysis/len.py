from command import Command


class Len(Command):

    def __init__(self, param):
        super().__init__()
        seq_details = Command.get_seq_details(self, param[0])
        self.sequence = seq_details[0]

    def process(self):
        return len(self.sequence)
