from command import Command
from Managment.delete import Del
from Managment.save import Save


class Managment(Command):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Managment.__instance:
            Managment.__instance = object.__new__(cls)
        return Managment.__instance

    def __init__(self):
        super().__init__()
        self.commands = {
            'del': Del,
            'save': Save
        }

    def command(self, cmd, params):
        self.check_string(params[0])
        self.cmd = self.commands[cmd](params)

    def execute(self):
        return self.cmd.process()
