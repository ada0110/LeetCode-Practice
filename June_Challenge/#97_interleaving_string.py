class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return 0
        matrix = [[0 for j in range(len(s1) + 1)] for i in range(len(s2) + 1)]
        matrix[0][0] = 1
        for i in range(1, len(matrix[0])):
            if s1[i - 1] == s3[i - 1] and matrix[0][i - 1] == 1:
                matrix[0][i] = 1
        for j in range(1, len(matrix)):
            if s2[j - 1] == s3[j - 1] and matrix[j - 1][0] == 1:
                matrix[j][0] = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if s3[i+j-1] == s1[j - 1] and s3[i+j-1] == s2[i - 1]:
                    if matrix[i - 1][j] == 1 or matrix[i][j-1] == 1:
                        matrix[i][j] = 1
                else:
                    if s3[i+j-1] == s1[j - 1]:
                        if matrix[i][j-1] == 1:
                            matrix[i][j] = 1
                    elif s3[i+j-1] == s2[i - 1]:
                        if matrix[i-1][j] == 1:
                            matrix[i][j] = 1
                    else:
                        matrix[i][j] = matrix[i][j]

        return matrix[-1][-1]