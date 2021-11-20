def birthdayCakeCandles(candles):
    maxheightcandles=0
    for i in candles:
        if i>maxheightcandles:
            maxheightcandles=i
    HeightedCandleCount=0
    for i in range(len(candles)):
        if candles[i]==maxheightcandles:
            HeightedCandleCount+=1
    return HeightedCandleCount
print(birthdayCakeCandles([4,4,1,3,9,9,9,9,9]))