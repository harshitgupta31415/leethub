class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count=Counter(s)
        l=[]
        smallest_odd=""
        for i in "abcdefghijklmnopqrstuvwxyz":
            l+=[i*(count[i]//2)]
            if not smallest_odd and count[i]%2==1:
                smallest_odd=i
        return "".join(l) + smallest_odd + "".join(l)[::-1]