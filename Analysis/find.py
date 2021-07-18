from command import Command


class Find(Command):
    def __init__(self, params):
        super().__init__()
        self.params = params
        seq_details = Command.get_seq_details(self, self.params[0])
        self.sequence = seq_details[0]
        if self.params[1][0] in ['#', '@']:
            seq_to_find_details = Command.get_seq_details(self, self.params[1])
            self.sequence_to_find = seq_to_find_details[0]
        else:
            self.sequence_to_find = params[1]

    def process(self):
        if self.sequence_to_find not in self.sequence:
            return "seq:{} not in seq:{}".format(self.params[1], self.params[0])
        return self.sequence.find(self.sequence_to_find)
