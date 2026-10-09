class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers left and right
        # compare the ends, if same move forward 
        # when different, three cases , 
            #delete left pointer and see if its palidrome
            #delete right pointer and see if its palindrome
            # when both deleted one by one and neither turns out to be a palindrome return false

        left = 0 
        right = len(s) - 1 

        while left < right:
            if s[left] != s[right]: 

                # check if substring is a palindrome 

                def pali(i,j):
                    while i < j:
                        if s[i] != s[j]:
                            return False

                        i += 1 
                        j -= 1 
                    return True


                return pali(left + 1, right) or pali(left, right - 1)

            left += 1 
            right -= 1 


        return True 
