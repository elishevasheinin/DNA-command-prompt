from Analysis.count import Count
from Analysis.len import Len
from command import Command
from Analysis.find import Find
from Analysis.find_all import FindAll


class Analysis(Command):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Analysis.__instance:
            Analysis.__instance = object.__new__(cls)
        return Analysis.__instance

    def __init__(self):
        super().__init__()
        self.commands = {
            'len': Len,
            'find': Find,
            'count': Count,
            'findall': FindAll
        }

    def command(self, cmd, params):
        self.check_string(params[0])
        self.cmd = self.commands[cmd](params)

    def execute(self):
        return self.cmd.process()
