#read from input.txt
with open('day1/input.txt', 'r') as f:
    data = f.read()

#convert data to list of ints
data = data.split('\n')
data = [int(i) for i in data if i]

#Part 1
#count the number of times the data value increases
increase = sum([i<j for i,j in zip(data,data[1:])])
print(increase)

#Part 2
#count the number of times the sum of 3 measurements in this sliding window increases 
sliding_window = 3
sw_data = [sum(data[i:i+3]) for i in range(len(data)-sliding_window+1)]
increase = sum([i<j for i,j in zip(sw_data,sw_data[1:])])
print(increase)