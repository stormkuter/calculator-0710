class Calc:
    pass

    def getDivide(self, a, b):
        self.validation_of_divider(b)
        return a / b

    def validation_of_divider(self, b):
        if (b == 0):
            raise ValueError("Divider must not be zero")