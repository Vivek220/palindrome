class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        rev=0
        orig=x
        while(orig>0):
            rem=orig%10
            rev=rev*10+rem
            orig=orig//10
        return rev==x    
        
