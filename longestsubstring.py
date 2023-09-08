class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curMax = 0
        left = 0
        maxSubLen = 0
        chSet = []
        right = 0

        while right < len(s):
            while right < len(s) and s[right] not in chSet:
                chSet.append(s[right])
                curMax += 1
                right += 1

            # falls out of the while loop now pointing to a repeat character
            # or past the end (?)

            maxSubLen = max(maxSubLen, curMax)

            chSet.remove(s[left])
            left += 1
            curMax -= 1

        return maxSubLen
