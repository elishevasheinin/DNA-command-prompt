class BatchData:

    __instance = None
    __batches = {} # {b_name: [commands]} #
    __num_of_batches = 0

    def __new__(cls, *args, **kwargs):
        if not BatchData.__instance:
            BatchData.__instance = object.__new__(cls)
        return BatchData.__instance

    def get_batches_names(self):
        batches_names = []
        for batch in BatchData.__batches:
            batches_names.append(batch)
        return batches_names

    def get_batches(self):
        return BatchData.__batches

    def get_batch_details_by_name(self, batch_name):
        return BatchData.__batches[batch_name]

    def insert_batch(self, batch_name, batch_details):
        BatchData.__batches[batch_name] = batch_details
