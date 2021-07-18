from command import Command
from Manipulation.pair import Pair
from Manipulation.slice import Slice


class Manipulator(Command):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Manipulator.__instance:
            Manipulator.__instance = object.__new__(cls)
        return Manipulator.__instance

    def __init__(self):
        super().__init__()
        self.commands = {
            'slice': Slice,
            'pair': Pair
        }

    def command(self, cmd, params):
        self.check_string(params[0])
        self.cmd = self.commands[cmd](params)

    def execute(self):
        return self.cmd.process()
