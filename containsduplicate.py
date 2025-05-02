from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

def main():
    nums = [1, 2, 3, 3]
    sol = Solution()
    print(sol.hasDuplicate(nums))

if __name__ == "__main__":
    main()