class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1 # O(1), O(1)
        
        while left < right: # O(n), O(1)
            s[left], s[right] = s[right], s[left] # O(1), O(1)
            left += 1 # O(1), O(1)
            right -= 1
        
        # Time -> O(n) + O(1) = O(n)
        # Space -> O(1)