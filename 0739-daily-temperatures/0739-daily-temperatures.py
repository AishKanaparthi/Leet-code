class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack=[]
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackId = stack.pop()
                answer[stackId] = i- stackId
            stack.append((t,i))
        return answer
        
#         Optimse the solution
#         answer=[]
#         stack=[]
#         a='false'
#         for i in range(len(temperatures)):
#             stack.append(temperatures[i])
#             a= stack.pop()
#             for j in range(i,len(temperatures)):
#                 stack.append(temperatures[j])
#                 b= stack.pop()
#                 if(b>a):
#                     a='true'
#                     answer.append(j-i)
#                     break
#                 if(j== len(temperatures)-1 and a!="true"):
#                     answer.append(0)
                    
        
#         if(len(temperatures) - len(answer)>0):
#             for i in range(len(temperatures) - len(answer)):
#                 answer.append(0)
        
      
#         return answer
                
            
        