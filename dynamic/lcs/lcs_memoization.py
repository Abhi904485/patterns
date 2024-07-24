def lcs(i, j, s1, s2, dp):
    if i == 0 or j == 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + lcs(i - 1, j - 1, s1, s2, dp)
        return dp[i][j]
    dp[i][j] = max(lcs(i, j - 1, s1, s2, dp), lcs(i - 1, j, s1, s2, dp))
    return dp[i][j]


def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """

    dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    return lcs(len(text1), len(text2), text1, text2, dp)


print(longestCommonSubsequence("abcde", "ace"))
