from itertools import product
from dataSetGenerator.dataFactory.find_two_max import find_two_max
from dataSetGenerator.dataFactory.take_random_field import take_random_field

def generate_data_set(data_seed):

    max_data_1 , max_data_2 , data_left = find_two_max(data_seed)

    data_set = list(map(list , product(max_data_1 , max_data_2)))

    len_iterator = len(data_set)
    for data_index in range(len_iterator):
        for block in data_left:
            data_set[data_index].append(take_random_field(block))

    return data_set