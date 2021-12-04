# read from input.txt
with open('day3/input.txt', 'r') as f:
    data = f.read()

# convert data to list of diagnostic reports
data = data.split('\n')

def bin_to_dec(bin):
    return int(bin, 2)

def str_to_bin(string):
    return '0b'+''.join(map(str, string))

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def copy_list_of_lists(lst):
    return [sublist[:] for sublist in lst]

def transpose_list_of_lists(lst):
    return list(map(list, zip(*lst)))

def remove_indexes(lst, indexes):
    for i in indexes[::-1]:
        lst.pop(i)
    return lst

def remove_indexes_from_list_of_lists(lst_of_lst, indexes):
    for i,lst in enumerate(lst_of_lst):
        lst_of_lst[i] = remove_indexes(lst, indexes)

def get_value_most_common(lst):
    return max(set(lst), key=lst.count)

def part1(data):
    bits = list(map(list, zip(*data)))
    list_most_common_bit = [int(max(set(lst), key=lst.count)) for lst in bits]
    gamma_rate_bin = list_most_common_bit
    epsilon_rate_bin = [1-e for e in list_most_common_bit]

    gamma_rate = bin_to_dec(str_to_bin(gamma_rate_bin))
    epsilon_rate = bin_to_dec(str_to_bin(epsilon_rate_bin))
    return gamma_rate*epsilon_rate

def part2(data):
    bits = transpose_list_of_lists(data)

    ogr_list_bits = copy_list_of_lists(bits)
    i = 0
    while i < len(ogr_list_bits):
        lst = ogr_list_bits[i]
        if len(lst) == 1:
            break

        value = get_value_most_common(lst)
        index_to_remove = [i for i, x in enumerate(lst) if x != value]
        remove_indexes_from_list_of_lists(ogr_list_bits, index_to_remove)
        
        i += 1

    ogr_bin = str_to_bin(flatten(ogr_list_bits))
    ogr = bin_to_dec(ogr_bin)

    C02sr_list_bits = copy_list_of_lists(bits)
    i = 0
    while i < len(C02sr_list_bits):
        lst = C02sr_list_bits[i]
        if len(lst) == 1:
            break

        value = get_value_most_common(lst)
        index_to_remove = [i for i, x in enumerate(lst) if x == value]
        remove_indexes_from_list_of_lists(C02sr_list_bits, index_to_remove)

        i += 1

    C02sr_bin = str_to_bin(flatten(C02sr_list_bits))
    C02sr = bin_to_dec(C02sr_bin)

    return C02sr*ogr

print(part1(data))
print(part2(data))