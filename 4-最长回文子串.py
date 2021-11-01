"""
"回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。)
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。


使用动态规划去填一张表格 竖表示左边界，横表示右边界
状态转移方程： dp[i][j] = {s[i] == s[j]} and (j-i<3 or dp[i+1][j-1])
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        #初始化表格
        dp = [[0]*length for _ in range(length)]
        # 赋值主对角线的值，当个字符是回文字符串，所以等于1
        for i in range(length):
            dp[i][i] = 1
        # 递推开始
        maxlength = 1
        begin = 0
        # 枚举子串长度
        for L in range(2, length+1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(length):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= length:
                    break
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    # 如果子串长度小于3,且s[i] == s[j] 为回文字符串 因为中间只有一个字符串
                    if j - i < 3:
                        dp[i][j] = 1
                    #  如果子串长度大于等于3,且s[i] == s[j]， 根据子串判断 左下角元素值
                    else:
                        dp[i][j] = dp[i+1][j-1]
                # 记录最长回文子串的起始位置
                # 只要 dp[i][L] == 1 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > maxlength:
                    maxlength = j - i + 1
                    begin = i
        return s[begin:begin+maxlength]




