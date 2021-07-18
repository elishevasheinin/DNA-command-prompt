from Batch.batch_data import BatchData


class CreateBatch:

    def __init__(self, invoker, batch_name):
        self.invoke = invoker
        self.batch_name = batch_name

    def run(self, command_word):
        batch_data = BatchData()
        batch_details = []
        while command_word != 'end':
            print("> batch >>>", end=' ')
            command = input()
            if not command:
                print("You did not enter variables")
                continue
            batch_details.append(command)
            command_word = command.split()[0]

        #add batch name to the list of active batches
        batch_data.insert_batch(self.batch_name, batch_details)
