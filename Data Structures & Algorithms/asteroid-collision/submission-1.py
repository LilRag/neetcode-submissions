class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            survived = True
            
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    survived = False 
                    break
                else:
                    survived = False
                    break
            if survived:
                stack.append(asteroid)
        return stack 