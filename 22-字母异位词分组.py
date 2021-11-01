"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次。

 
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
import collections
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
collections.defaultdict()
dict = {}
for s in strs:
    key = ''.join(sorted(s))
    if key not in dict:
        dict[key] = []
    dict[key].append(s)
print(list(dict.values()))