# sum of a list

def sum_list(list):
    if len(list) > 1:
        return list[0] + sum_list(list[1:])
    else:
        return list[0]

if __name__ == "__main__":
    print(sum_list([5, 8, 9, 10, 6]))
