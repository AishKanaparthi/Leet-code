class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        arr=set()
        for a in emails:
            b= a.split('@')
            local_name = b[0]
            domain_name= b[1]
            
            local_name= local_name.replace(".", "")
            local_name1= local_name.split('+')
            local_name= local_name1[0]
            final_name= local_name+"@" + domain_name
            
            if(final_name not in arr):
                arr.add(final_name)
            
        return len(arr)

            
        