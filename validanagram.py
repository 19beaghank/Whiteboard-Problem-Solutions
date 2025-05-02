class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

def main():
    s = "racecar"
    t = "carrace"
    sol = Solution()
    print(sol.isAnagram(s, t))

if __name__ == "__main__":
    main()