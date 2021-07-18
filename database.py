class Database:

    __instance = None
    __dna_sequences = []
    __dna_names = []

    def __new__(cls, *args, **kwargs):
        if not Database.__instance:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    def get_seq(self, seq_with_symbol):
        if seq_with_symbol[0] == '#':
            return self.get_seq_by_id(int(seq_with_symbol[1:]) - 1)
        return self.get_seq_by_name(seq_with_symbol[1:])

    def set_sequence(self, seq_id, new_seq):
        Database.__dna_sequences[seq_id - 1] = new_seq

    def get_dna_sequences(self):
        return Database.__dna_sequences

    def get_dna_names(self):
        return Database.__dna_names

    def get_new_id(self):
        return len(Database.__dna_sequences) + 1

    def get_seq_by_id(self, id):
        return Database.__dna_sequences[id - 1]

    def get_seq_by_name(self, name):
        id = Database.__dna_names.index(name)
        return Database.__dna_sequences[id]

    def get_seq_name(self, seq):
        id = Database.__dna_sequences.index(seq)
        return Database.__dna_names[id]

    def get_seq_id(self, seq):
        return Database.__dna_sequences.index(seq) + 1

    def insert_dna_seq(self, seq_name, dna_seq):
        Database.__dna_sequences.append(dna_seq)
        Database.__dna_names.append(seq_name)

    def delete_seq(self, seq_id):
        #in order to keep the sequences' id
        self.set_sequence(seq_id, 'Deleted')
        Database.__dna_names[seq_id - 1] = ''
