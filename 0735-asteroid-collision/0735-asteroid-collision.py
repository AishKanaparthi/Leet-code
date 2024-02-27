class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 < stack[-1]:
                if abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    break
                elif abs(asteroids[i]) < abs(stack[-1]):
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroids[i])

        return stack
