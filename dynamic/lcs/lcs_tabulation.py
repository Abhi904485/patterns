def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """

    dp = [[None]*(len(text2)+1) for i in range(len(text1)+1)]
    for i in range(len(text1) + 1):
        for j in range(len(text2) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(text1)][len(text2)]


print(longestCommonSubsequence("ab", "ab"))
