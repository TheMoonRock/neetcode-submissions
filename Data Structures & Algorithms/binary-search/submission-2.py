class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search_recursive(arr, target, left, right):
            # Если границы поиска пересекаются, искомого значения в массиве нет
            if left > right:  
                return -1
            # Вычислить серединный индекс
            mid = left + (right - left) // 2 
            # Если серединное значение равно испомому, вернуть его индекс
            if arr[mid] == target: 
                return mid  
            # Если искомое значение больше серединного, искать дальше в правой половине
            elif arr[mid] < target: 
                return binary_search_recursive(arr, target, mid + 1, right)  
            # Если искомое значение меньше серединного, искать дальше в левой половине
            else: 
                return binary_search_recursive(arr, target, left, mid - 1)  

        # Запустить рекурсивную функцию
        result = binary_search_recursive(nums, target, 0, len(nums) - 1)
        return result