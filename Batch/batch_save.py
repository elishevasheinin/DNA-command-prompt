from Batch.batch_data import BatchData


class BatchSave:

    ''' Command: batchsave <@batch_name> [<batch_file>] '''
    def __init__(self, params):
        if params[0][0] != '@':
            raise Exception("Batch name must start with @")
        self.batch_name = params[0][1:]

        if len(params) > 1:
            self.file_name = params[1]
        else:
            self.file_name = self.batch_name + '.dnabatch'

        self.batch_data = BatchData()

    def process(self):
        batch_details = self.batch_data.get_batch_details_by_name(self.batch_name)
        with open(self.file_name, 'w') as file:
            for command in batch_details:
                if command == 'end':
                    break
                file.write(command + '\n')
        return "Batch {} saved".format(self.batch_name)
