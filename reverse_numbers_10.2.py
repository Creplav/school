'''
    This program takaes a list of integers and prints them out in reversed order
'''

numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_list_reversed(list):
    list.reverse()
    for i in list:
        print(i)

print_list_reversed(numberList)