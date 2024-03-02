def birthdayCakeCandles(candles,n):
    # Write your code here
    count = 0
    max_hight = max(candles)
    for i in range(n):
        if candles[i]==max_hight:
            count +=1
            
    print(count)


candles_count = int(input("size: ").strip())

candles = list(map(int, input("list: ").rstrip().split()))

result = birthdayCakeCandles(candles,candles_count)
