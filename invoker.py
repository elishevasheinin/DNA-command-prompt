from Commands_type.analysis import Analysis
from Commands_type.batch import Batch
from Commands_type.creator import Creator
from database import Database
from Commands_type.managment import Managment
from Commands_type.manipulator import Manipulator


class Invoker:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Invoker.__instance:
            Invoker.__instance = object.__new__(cls)
        return Invoker.__instance

    def __init__(self):
        self.commands = {
            'new': Creator,
            'load': Creator,
            'dup': Creator,
            'slice': Manipulator,
            'pair': Manipulator,
            'del': Managment,
            'save': Managment,
            'len': Analysis,
            'find': Analysis,
            'count': Analysis,
            'findall': Analysis,
            'batchlist': Batch,
            'batchshow': Batch,
            'batchsave': Batch,
            'batchload': Batch
        }
        self.db = Database()

    """command method"""

    def command(self, cmd, params):
        if cmd not in self.commands:
            raise ValueError("Command not found")
        self.cmd = self.commands[cmd]()
        self.cmd.command(cmd, params)

    """execute method"""

    def execute(self):
        return self.cmd.execute()
