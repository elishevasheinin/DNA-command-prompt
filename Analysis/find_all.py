from Analysis.find import Find


class FindAll(Find):
    def __init__(self, params):
        super().__init__(params)

    def find_all(self):
        found_ind = []
        ind = self.sequence.find(self.sequence_to_find)
        while ind != -1:
            found_ind.append(ind)
            ind = self.sequence.find(self.sequence_to_find, ind + 1)
        return found_ind

    def process(self):
        if self.sequence_to_find not in self.sequence:
            return "seq:{} not in seq:{}".format(self.params[1], self.params[0])
        found_ind = self.find_all()
        return ",".join([str(elem) for elem in found_ind])
