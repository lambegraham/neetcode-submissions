class Solution:
    def isPalindrome(self, s: str) -> bool:

        revString = ""

        for c in s:
            if c.isalnum():
                revString += c.lower()
        return revString == revString[::-1]