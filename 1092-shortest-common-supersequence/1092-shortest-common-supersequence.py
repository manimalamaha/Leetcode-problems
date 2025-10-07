class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        # DP table to store lengths of longest common subsequence (LCS)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Now, build the shortest common supersequence (SCS)
        i, j = m, n
        scs = []
        
        # Traverse the DP table from the bottom-right corner
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                scs.append(str1[i - 1])  # If characters are equal, add to SCS
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                scs.append(str1[i - 1])  # If moving up in DP table, add str1[i-1]
                i -= 1
            else:
                scs.append(str2[j - 1])  # If moving left in DP table, add str2[j-1]
                j -= 1
        
        # If there are remaining characters in str1 or str2, append them
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1
        
        # The result is in reverse order, so reverse the list and join it to form the string
        return ''.join(reversed(scs))