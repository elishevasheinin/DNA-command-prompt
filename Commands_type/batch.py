from Batch.batch_data import BatchData
from Batch.batch_list import BatchList
from Batch.batch_load import BatchLoad
from Batch.batch_save import BatchSave
from Batch.batch_show import BatchShow


class Batch:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Batch.__instance:
            Batch.__instance = object.__new__(cls)
        return Batch.__instance

    def __init__(self):
        self.commands = {
            'batchlist': BatchList,
            'batchshow': BatchShow,
            'batchsave': BatchSave,
            'batchload': BatchLoad
        }
        self.batch_data = BatchData()

    def command(self, cmd, params):
        self.cmd = self.commands[cmd](params)

    def execute(self):
        return self.cmd.process()

