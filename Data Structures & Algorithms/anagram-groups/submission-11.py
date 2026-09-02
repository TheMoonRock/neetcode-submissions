class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def ord_sum(input_string):
            return sum(map(ord, input_string))

        def ord_sort(input_string):
            return sorted(map(ord, input_string))

        dict = {}
        for item in strs:
            key = ord_sum(item)
            if key in dict:
                if ord_sort(dict[key][0]) != ord_sort(item):
                    dict[key+500] = [item]
                    continue
                dict[key].append(item)
            else:
                dict[key] = [item]

        ana = list(dict.values())
        return ana

#У меня в dict[key] список слов.
# Нужно проверить на совпадение хотябы с одним