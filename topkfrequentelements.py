from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        return [item for item, _ in freq_counter.most_common(k)]

def main():
    nums = [0, 1, 1, 1, 2, 2, 3, 4, 4]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))

if __name__ == "__main__":
    main()