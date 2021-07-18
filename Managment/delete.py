from command import Command


class Del(Command):
    def __init__(self, param):
        super().__init__()
        seq_details = Command.get_seq_details(self, param[0])
        self.sequence = seq_details[0]
        self.sequence_id = seq_details[1]
        self.sequence_name = seq_details[2]

    def process(self):
        if self.db.get_seq_by_id(self.sequence_id) == 'Deleted':
            return "Sequence already deleted"
        print('''Do yoy really want to delete {}: {}?
                Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'. 
                > confirm >>> '''.format(self.sequence_name, self.sequence))
        answer = input()
        # answer = answer.lower()
        # while answer != 'y' and answer != 'n':
        while answer not in ['y', 'Y', 'n', 'N']:
            print('''You have typed an invalid response. 
                    Please either confirm by 'y'/'Y', 
                    or cancel by 'n'/'N' \n
                    > confirm >>> ''')
            answer = input()
            # answer = answer.lower()
        # if answer == 'n':
        if answer in ['n', 'N']:
            return "The deletion was canceled"
        self.db.delete_seq(self.sequence_id)
        return "Deleted: [{}] {}: {}".format(self.sequence_id, self.sequence_name, self.sequence)
