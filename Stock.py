class Stock:
    average = 0
    doji_tolerance =1000
    def __init__(self,dataFrame):
        self.calculate_doji_treshhold()
    def calculate_doji_treshhold(self):
        tolerance =self.doji_tolerance
        result= self.average/tolerance
        return result
