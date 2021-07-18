from Batch.batch_data import BatchData
from invoker import Invoker


class Run:

    def __init__(self, batch_name):
        if batch_name[0] != '@':
            raise Exception("Batch name must start with @")
        self.batch_name = batch_name[1:]
        self.batch_data = BatchData()

    def process(self):
        batch_commands = self.batch_data.get_batches()[self.batch_name]
        invoke = Invoker()
        for command in batch_commands:
            if command == 'end':
                break
            print(command)
            command_list = command.split()
            invoke.command(command_list[0], command_list[1:])
            print(invoke.execute())
