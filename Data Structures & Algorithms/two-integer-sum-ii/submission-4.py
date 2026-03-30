class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        while l < len(numbers):
            r = l + 1
            while r < len(numbers):
                print("l: " + str(l) + " " + str(numbers[l]))
                print("r: " + str(r) + " " + str(numbers[r]))
                print("sum: " + str(numbers[l] + numbers[r]))
                if numbers[l] + numbers[r] == target:
                    return [l + 1,r + 1]
                r += 1
            l += 1
            