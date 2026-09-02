class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for item in s:
            if item in dict1:
                dict1[item] += 1
            if item not in dict1:
                dict1[item] = 1
        for item in t:
            if item in dict2:
                dict2[item] += 1
            if item not in dict2:
                dict2[item] = 1
        return dict1 == dict2