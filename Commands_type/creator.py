from Creation.dup import Dup
from Creation.load import Load
from Creation.new import New
# import Creation
from database import Database


class Creator:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Creator.__instance:
            Creator.__instance = object.__new__(cls)
        return Creator.__instance

    def __init__(self):
        self.commands = {
            'new': New,
            'load': Load,
            'dup': Dup
        }
        self.db = Database()

    def check_and_fix_string(self, seq):
        if seq[0] != '@':
            raise Exception("String must start with @")
        seq = seq[1:]
        return seq

    def command(self, cmd, params):
        if len(params) > 1:
            params[1] = self.check_and_fix_string(params[1])
        self.cmd = self.commands[cmd](params)

    def execute(self):
        new_seq_details = self.cmd.process()
        # insert new_seq_details into database
        dna_id = self.db.get_new_id()
        name = new_seq_details[0]
        seq = new_seq_details[1]
        self.insert_new_dna_sequence_into_db(name, seq)
        if len(seq) > 40:
            seq = seq.get_dna_seq()[:32] + '...' + seq.get_dna_seq()[-3:]
        return "[{}] {}: {}".format(dna_id, name, seq)

    def insert_new_dna_sequence_into_db(self, name, seq):
        self.db.insert_dna_seq(name, seq.get_dna_seq())
