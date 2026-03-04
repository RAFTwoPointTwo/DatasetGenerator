def show_data_set(data_set):
    for data in data_set:
        print("\n ------------------------------------------------------------------- \n")
        data_length = len(data)
        for index in range(data_length):
            if index == 0:
                print(f"\t {data[index]}", end=" , ")
            elif index == data_length - 1:
                print(data[index], end=" ")
            else:
                print(data[index], end=" , ")
    print("\n ------------------------------------------------------------------- \n")