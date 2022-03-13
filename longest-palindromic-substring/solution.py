class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        solution_matrix = []
        max_solution_len = 1

        # start and end indexes of the longest palindromic substring
        start = 0
        end = 0

        # initialize the matrix
        solution_matrix = [ [False for i in range(length)] for j in range(length)]

        # Substrings of lengt 1 are all palindromic
        for i in range(length):
            solution_matrix[i][i] = True

        # Check for substrings of length 2
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                solution_matrix[i][i + 1] = True
                max_solution_len = 2
                start = i
                end = i + 1
                

        # For i - j >= 2
        # If first and last chars are the same and the substring without them is still palindromic,
        # then make solution_matrix[i][i+x] = True
        # However, j is i + x here
        for x in range(2, length):
            for i in range(length - x):
                if s[i] == s[i + x] and solution_matrix[i + 1][i + x - 1]:
                    solution_matrix[i][i + x] = True

                    if x + 1 > max_solution_len:
                        max_solution_len = x + 1
                        start = i
                        end = i + x

        return s[start:end+1]




