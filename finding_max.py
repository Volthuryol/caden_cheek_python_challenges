def find_max(num_list):
    try:
        max_num = num_list[0]

        for num in num_list:
            if num > max_num:
                max_num = num
        num_index = num_list.index(max_num)

        return print(f"{max_num} is your highest value it is at index {num_index}")
    except:
        print("Can't be an empty list")

find_max([4, 9, 1, 17, 2])

def find_max_while(list_num):
    try:
        max_num = list_num[0]
        count = 0
    
        while count < len(list_num):
            if max_num < list_num[count]:
                max_num = list_num[count]
            
            count += 1
            num_index = list_num.index(max_num)

        return print(f"{max_num} is your highest value it is at index {num_index}")
    except:
       return print("Must not be an empty list")
    
find_max_while([42])