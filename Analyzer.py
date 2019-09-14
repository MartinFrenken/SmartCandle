import plotly.graph_objects as ply
import pandas as pd
from datetime import datetime
from Color import Color
from Candle import Candle

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

closing_average = df['AAPL.Close'].mean()
print(closing_average)
candle_list = []
for index, row in df.iterrows():
    candle_index = index
    candle_close = row['AAPL.Close']
    candle_open = row['AAPL.Open']
    candle_high = row['AAPL.High']
    candle_low = row['AAPL.Low']
    candle = Candle(open=candle_open, high=candle_high, low=candle_low, close=candle_close, order=index,
                    average=closing_average)
    candle_list.append(candle)

def get_doji_count(candle_collection):
    doji_count = 0
    for i in candle_collection:
        if i.is_doji:
            doji_count += 1

    return doji_count

def get_red_doji_green_count(candle_collection):

    green_candle_after_previous_red_candles_and_doji_count=0
    red_candle_after_previous_red_candles_and_doji_count=0
    previous_red_doji_count =0
    doji_count =get_doji_count(candle_collection)
    for i in range(len(candle_collection)):
        if previous_candles_are_red(candle_collection,i) and candle_collection[i].is_doji:
            previous_red_doji_count +=1
            if next_candle_is_green(candle_collection,i):
                green_candle_after_previous_red_candles_and_doji_count+=1
            else:
                red_candle_after_previous_red_candles_and_doji_count += 1

    return ("Out of the "+str(doji_count) +" dojis "+ str(previous_red_doji_count) + " dojis had two red candles before occuring and out of those dojis "+ str(green_candle_after_previous_red_candles_and_doji_count)+ " had a green candle after occuring")

def previous_candles_are_red(candle_collection, candle_position):
    previous_red_candle_amount = 2

    if candle_position>previous_red_candle_amount:
        red_candle_amount = 0
        for j in range(previous_red_candle_amount):
            if candle_collection[candle_position - j].color == Color.RED:
                red_candle_amount+=1
        if red_candle_amount == previous_red_candle_amount:
            return True
    return False

def next_candle_is_green(candle_collection, candle_position):
    next_index =1
    collection_size =len(candle_collection)
    if candle_position+next_index <collection_size:
        if candle_collection[candle_position+next_index].color==Color.GREEN:
            return True
        return False

text = get_red_doji_green_count(candle_list)
print(text)
