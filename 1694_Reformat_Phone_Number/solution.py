class Solution:
    def reformatNumber(self, number: str) -> str:
        a=number.replace('-','').replace(' ','')
        ans=''
        for i in range(len(a)):
            ans+=a[i]
            if (i+1)%3==0  and len(a)-(i+1)>1:
                ans+='-'
        l=ans.split('-')
        t=''
        for i in range(len(l)):
            t+='-'
            if len(l[i])>3:
                t+=l[i][:2]+'-'+l[i][2:]
            else :
                t+=l[i]

            
        return t[1:]
