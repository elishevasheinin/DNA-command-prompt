from Batch.batch_data import BatchData


class BatchList:

    def __init__(self, params):
        self.batch_data = BatchData()

    def process(self):
        batch_list = []
        batches_names = self.batch_data.get_batches_names()
        for batch_name in batches_names:
            batch_list.append(batch_name)
        return batch_list
