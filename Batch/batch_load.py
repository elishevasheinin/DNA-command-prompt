from Batch.batch_data import BatchData


class BatchLoad:

    ''' Command: batchload <batch_file> [ : [<@batch_name>]] '''
    def __init__(self, params):
        self.file_name = params[0]
        if len(params) > 1:
            if params[1][0] != '@':
                raise Exception("Batch name must start with @")
            self.batch_name = params[1][1:]
        else:
            self.batch_name = self.file_name.split('.')[0]
        self.batch_data = BatchData()

    def process(self):
        batch_details = []
        with open(self.file_name, 'r') as file:
            command = file.readline()[:-1]
            while command:
                batch_details.append(command)
                command = file.readline()[:-1]

        # add batch name to the list of active batches
        self.batch_data.insert_batch(self.batch_name, batch_details)
        return "Loaded batch {} from {}".format(self.batch_name, self.file_name)
