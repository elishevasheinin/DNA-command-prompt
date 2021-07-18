from Batch.batch_data import BatchData


class BatchShow:

    def __init__(self, batch_name):
        if batch_name[0][0] != '@':
            raise Exception("Batch name must start with @")
        self.batch_name = batch_name[0][1:]
        self.batch_data = BatchData()

    def process(self):
        batch_details = self.batch_data.get_batch_details_by_name(self.batch_name)
        return batch_details[:-1]
