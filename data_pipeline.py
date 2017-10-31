class DataPipeline:

    def __init__(self, batch_size, max_memory):
        self.batch_size=batch_size
        self.max_memory=max_memory
        self.input_size = None
        self.num_gester = None

    def get_input_size(self):
        return self.input_size

    def get_output_size(self):
        return self.num_gester