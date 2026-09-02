class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                # из большего кода символа вычитаем меньший. Это будет индекс в списке к которому прибавим 1.
            res[tuple(count)].append(s) #ключом является кортеж (отпечаток) слова, так как в анаграммах одинаковые символы.
            # к этому ключу прибавляем слова
            print(res)
        return list(res.values())