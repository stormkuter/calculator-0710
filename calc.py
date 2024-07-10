class Calc:
    def getZegop(self, num_1, num_2):
        return num_1 ** num_2
    
    def getSum(self, a, b):
        return a + b
      
    def getDivide(self, a, b):
        self.validation_of_divider(b)
        return a / b

    def validation_of_divider(self, b):
        if (b == 0):
            raise ValueError("Divider must not be zero")
            
    def getSum(self, a, b):
        return a + b
