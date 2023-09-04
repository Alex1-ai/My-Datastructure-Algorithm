import math


arr = []
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        print(tokens)
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")



print(arr)

print('temperature in the 1st week: ',arr[0:7])

aveTemp = sum(arr[0:7])/len(arr[0:7])
print("The average temperature in first week is ", aveTemp)
print("max:", max(arr[0:7]))






weather_arr = {}

with open('nyc_weather.csv') as f:
    for line in f:
        tokens = line.split(',')

        try:
            weather_arr[tokens[0]] = int(tokens[1])
        except:
            print("Invalid something went wrong")

print(weather_arr)
print('Jan 9 temperature:' , weather_arr['Jan 9'])
print('Jan 4 temperature:' , weather_arr['Jan 4'])