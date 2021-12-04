#read from input.txt
with open('Day 3/input.txt', 'r') as f:
    data = f.read()

#convert data to list of diagnostic reports
data = data.split('\n')

# Part 1
bits = list(map(list, zip(*data)))
list_most_common_bit = [int(max(set(lst), key=lst.count)) for lst in bits]
gamma_rate_bin = list_most_common_bit
epsilon_rate_bin = [1-e for e in list_most_common_bit]

gamma_rate = int('0b'+''.join(map(str, gamma_rate_bin)), 2)
epsilon_rate = int('0b'+''.join(map(str, epsilon_rate_bin)), 2)
print(gamma_rate*epsilon_rate)

# Part 2
