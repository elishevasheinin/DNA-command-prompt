from Analysis.find_all import FindAll


class Count(FindAll):
    def __init__(self, params):
        super().__init__(params)

    def process(self):
        return len(self.find_all())
