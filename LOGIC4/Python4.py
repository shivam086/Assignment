"""
4. Given two integer arrays nums1 and nums2 , return an array of their intersection. Each
element in the result must appear as many times as it shows in both arrays and you may
return the result in any order.(Write a Function)

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

class Intersection:
    def intersectionOfArray(self, arr1: list, arr2: list):
        print("nums1: ", arr1)
        print("nums2: ", arr2)
        output_list = list()
        for each in arr1:
            if each in arr2:
                output_list.append(each)
                arr2.remove(each)
        return output_list


arr_length1 = int(input("Enter nums1 length: "))  # To input nums1 array length
nums1 = [int(input("Enter {0} integer for nums1: ".format(each+1))) for each in range(arr_length1)]  # To create list of integer for nums1 array
arr_length2 = int(input("Enter nums2 length: "))  # To input nums2 array length
nums2 = [int(input("Enter {0} integer for nums2: ".format(each+1))) for each in range(arr_length2)]  # To create list of integer for nums2 array
obj = Intersection()  # To create Intersection class instance
output_val = obj.intersectionOfArray(nums1, nums2)  # To call instance intersectionOfArray method
print("Intersection of nums1 and nums2 is: ", output_val)  # To print output value


'''
EXPLANATION:
-----------
1. First, I take two arrays nums1 and nums2
2. Use for loop on array nums1 and for each value of nums1, we check it into array nums2
3. If value exists in array nums2, we append this value into new list 'output_list' and remove this value from array nums2.
4. In last, we return the new list 'output_list' as the output
'''