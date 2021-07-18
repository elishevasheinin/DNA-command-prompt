from Batch.batch_creation import CreateBatch
from Commands_type.batch import Batch
from Batch.batch_data import BatchData
from Batch.run import Run
from invoker import Invoker


class CLI:
    def __init__(self):
        self.invoke = Invoker()

    def run(self):
        while True:
            print("> cmd >>>", end=' ')
            command = input().split()
            self.handle_command(command)

    def handle_command(self, command):
        if len(command) == 0:
            print("You did not enter enough variables")
            return
        command_word = command[0]
        command_args = command[1:]
        if command_word == 'batch':
            self.batch(command_word, command_args)
            return
        if command_word == 'run':
            cmd = Run(command_args[0])
            cmd.process()
            return
        self.invoke.command(command_word, command_args)
        print(self.invoke.execute())

    def batch(self, command_word, command_args):
        batch_name = command_args[0]
        batch = CreateBatch(self.invoke, batch_name)
        batch.run(command_word)
