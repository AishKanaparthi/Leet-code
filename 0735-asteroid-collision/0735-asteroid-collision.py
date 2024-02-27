class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                elif abs(asteroid) < stack[-1]:
                    break
                else:
                    stack.pop()

            else:
                stack.append(asteroid)

        return stack
