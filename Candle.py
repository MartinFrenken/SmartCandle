from Color import Color


class Candle:
    open = 0
    high = 0
    low = 0
    close = 0
    order = 0
    index = 0
    average =0
    is_doji=False
    color = Color.GRAY
    def __init__(self):
        pass

    def __init__(self, open, high, low, close, order, average):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.order = order
        self.average =average
        #todo : replace average with stock class
        self.calculate_doji_value()
        self.calculate_color_value()

    def calculate_doji_value(self):
        delta= self.calculate_open_close_delta()
        treshhold = self.calculate_doji_treshhold()
        if abs(delta)>treshhold:
            self.is_doji=False
        else:
            self.is_doji=True

    def calculate_color_value(self):
        if self.open > self.close:
            self.color = Color.RED
        else:
            self.color = Color.GREEN

    def set_index(self, value):
        self.index = value

    def calculate_open_close_delta(self):
        return self.open-self.close

    def calculate_doji_treshhold(self):
        tolerance =1000
        result= self.average/tolerance
        return result

