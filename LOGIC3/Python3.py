"""
3. Write a function that reverses a string. The input string is given as an array of characters
(Please Do not use the default function for the reverse)

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

""" METHOD-1 """

class Reverse:
    def reverseList(self, arr: list):  # Function to reverse the list of characters
        print("Input array is: ", arr)
        reverse_list = list()
        for index, each in enumerate(arr):
            reverse_list.insert(-(index+1), each)
        return reverse_list


arr_length = int(input("Enter length of array: "))  # To input array length
str_array = [input("Enter {0} string: ".format(each+1)) for each in range(arr_length)]  # To create array of character
obj = Reverse()  # To create Reverse class instance
output_val = obj.reverseList(str_array)  # To call instance reverseList method
print("Reverse array is: ", output_val)  # To print output value


'''
EXPLANATION:
-----------
1. First, I take array of characters
2. Use for loop on array 'arr' where enumerate function return the index and value on that index of each character
3. For each value, we insert this value into new list 'reverse_list' according to negative indexing like 
1st time index -1
2nd time index -2
3rd time index -3
etc...
(We insert arr 0th index value at last position in reverse_list, 1st index value at second last position in reverse_list and so on...)
4. In last, we return the new list 'reverse_list' as the output
'''


""" METHOD-2 """

class Reverse:
    def reverseList(self, arr: list):  # Function to reverse the list of characters
        print("Input array is: ", arr)
        reverse_list = arr[::-1]
        return reverse_list


arr_length = int(input("Enter length of array: "))  # To input array length
str_array = [input("Enter {0} string: ".format(each+1)) for each in range(arr_length)]  # To create array of character
obj = Reverse()  # To create Reverse class instance
output_val = obj.reverseList(str_array)  # To call instance reverseList method
print("Reverse array is: ", output_val)  # To print output value

'''
EXPLANATION:
-----------
1. First, I take array of characters
2. To reverse the array of charcters, we use slicing method.
4. In last, we return the list 'reverse_list' as the output
'''
