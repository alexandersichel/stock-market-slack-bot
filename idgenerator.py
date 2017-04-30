class IDGenerator():
    def __init__(self):
        self.unique_id = 1
    def get_unique_id(self):
        self.unique_id +=1
        return self.unique_id

id_generator = IDGenerator()