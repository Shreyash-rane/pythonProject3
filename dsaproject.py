# Program to print the largest common substring

import numpy as np


class LCS(object):
    def __init__(self, RowString, ColumnString):
        self.RowString = RowString
        self.ColumnString = ColumnString

    # For the printing the String
    def LCSString(self):
        # Getting Len of the Strings
        LenofFirst = len(self.RowString)
        LenofSecond = len(self.ColumnString)
        # Making List for appending table data
        L = [[0 for x in range(LenofSecond + 1)] for x in range(LenofFirst + 1)]

        for i in range(LenofFirst + 1):
            for j in range(LenofSecond + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif self.RowString[i - 1] == self.ColumnString[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        index = L[LenofFirst][LenofSecond]

        lcs_algo = [""] * (index + 1)
        lcs_algo[index] = ""

        i = LenofFirst
        j = LenofSecond
        while i > 0 and j > 0:

            if self.RowString[i - 1] == self.ColumnString[j - 1]:
                lcs_algo[index - 1] = self.RowString[i - 1]
                i -= 1
                j -= 1
                index -= 1

            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
            else:
                j -= 1

        # Printing the sub sequences
        print("FirstString : " + self.RowString + "\nSecondString : " + self.ColumnString)
        print("LCS: " + "".join(lcs_algo))
        print("This is the length of the String:", len("".join(lcs_algo)))
        Matrix = np.array(L)
        print(Matrix)


FirstString = input("Enter a First String:")
SecondString = input("Enter a Second String:")
obj = LCS(SecondString, FirstString)
obj.LCSString()