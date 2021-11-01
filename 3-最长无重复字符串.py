"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
滑动窗口
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        right = 0
        lenght = len(s)
        res = 0
        while(right < lenght):
            c = s[right]
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
            right += 1
            while(window[c] > 1):
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right-left)
        return res
# 一个数组a=[0,1,2,3,4]，a[-1]表示数组中最后一位，a[:-1]表示从第0位开始直到最后一位，a[::-1]表示倒序，从最后一位到第0位。
s = "abcabcbb"
a = Solution().lengthOfLongestSubstring(s= s)
print(a)