numbers = list(input("enter the list"))
def count_frequencies(data_list):
# empty dictionary where list items get stored 
    frequency = {}
# loop to traverse all items in the data_list
    for item in data_list:
# if item in data_list is same in the frequency 
        if item in frequency:
            frequency[item] += 1
# else not if 
        else:
            frequency[item] = 1
# return the frequency of items for the function
    return frequency
# calling the function
result = count_frequencies(numbers)
# print the dictionary ams
print(result)