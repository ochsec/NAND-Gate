class Nand:

    def __init__(self, input1: bool, input2: bool):
        self.input1 = input1
        self.input2 = input2

    def update(self, input1: bool, input2: bool):
        self.input1 = input1
        self.input2 = input2

    def output(self) -> bool:
        return not (self.input1 and self.input2)
    
    def __str__(self) -> str:
        return f'Nand({self.input1}, {self.input2})'
    
    def __repr__(self) -> str:
        return str(self)
