class Caluclator:

    def __init__(self, num_1, num_2) -> None:
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        result = self.num_1 + self.num_2
        print(result)
    
obj = Caluclator(23,34)
obj.add()