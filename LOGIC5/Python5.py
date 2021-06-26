"""
5. Given a string s , return the longest palindromic substring in s .

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""


class Palindrome:
    def longestPalindrome(self, str_val: str):  # Function to get longest palindrome
        n = len(str_val)
        # All subStrings of length 1 are palindromes
        max_length = 1
        start = 0
        for i in range(n):
            for j in range(i, n):
                flag = 1
                for k in range(0, ((j - i) // 2) + 1):
                    if (str_val[i + k] != str_val[j - k]):
                        flag = 0
                if (flag != 0 and (j - i + 1) > max_length):
                    start = i
                    max_length = j - i + 1
        return start, max_length

    def subStr(self, str_val, low, high):
        emp_str = ""
        for i in range(low, high + 1):
            emp_str += str_val[i]
        return emp_str


str_val = input("Enter string value: ")  # To input string value
obj = Palindrome()  # To create Palindrome instance
start, max_length = obj.longestPalindrome(str_val)  # To call instance longestPalindrome method
output_val = obj.subStr(str_val, start, (start + max_length - 1))  # To call instance longestPalindrome method
print("Longest palindrome string is: ", output_val)  # To print output value


'''
EXPLANATION:
-----------
1. First, I take string value.
2. In this approach, we check each substring whether the substring is a palindrome or not.
  (a.) run three nested loops, the outer two loops pick all substrings one by one by fixing the corner characters
  (b.) the inner loop checks whether the picked substring is palindrome or not.
  
3. Finally, we get the longest palindrome sub string first and last index value.
4. Using subStr function. we can slice the input string into longest palindrome substring.
'''