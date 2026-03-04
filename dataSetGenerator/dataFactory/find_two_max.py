import heapq

def find_two_max(datas):

    data_lengths = []

    for data in datas:
        data_lengths.append(len(data))

    if len(data_lengths) >= 2:
        max_lengths = heapq.nlargest(2 , data_lengths)
    else:
        item = list(data_lengths)[0]
        max_lengths = [item , item]

    max_1 = max_lengths[0]
    max_2 = max_lengths[1]

    max_data_1 = []
    max_data_2 = []
    data_left = []
    is_data_1_affected = False

    for data in datas:
        if len(data) == max_1 and not is_data_1_affected:
            max_data_1 = data
            is_data_1_affected = True
            continue
        if len(data) == max_2:
            max_data_2 = data
            continue

    for data in datas:
        if data != max_data_1 and data != max_data_2:
            data_left.append(data)

    return max_data_1 , max_data_2 , data_left
