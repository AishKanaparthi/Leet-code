class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        return self.s.append(x)

    def pop(self) -> int:
        temp_stack = []
        
        # Move elements from main stack to temporary stack
        while self.s:
            temp_stack.append(self.s.pop())
        
        # Pop the front element from the temporary stack
        front_element = temp_stack.pop() if temp_stack else None
        
        # Move elements back to the main stack
        while temp_stack:
            self.s.append(temp_stack.pop())
        
        return front_element

    def peek(self) -> int:
        return self.s[0] if self.s else None

    def empty(self) -> bool:
        return not self.s


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()