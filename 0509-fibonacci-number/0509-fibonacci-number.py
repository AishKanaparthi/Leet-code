class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
#         if n<=1:
#             return n
        
#         def f(n):
            
#             if n>1:
#                 return f(n-1)+f(n-2)
#             else:
#                 return n
#         return f(n)
    
        