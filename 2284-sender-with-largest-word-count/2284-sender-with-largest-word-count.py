class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        map = {}
        m=0
        ans=""
        for i in range(len(senders)):
            if senders[i] not in map:
                map[senders[i]] =  messages[i].count(' ')+1
            else:
                map[senders[i]]+= messages[i].count(' ')+1
            m=max(m,map[senders[i]])
        for i,k in map.items():
            if k==m:
                ans=max(ans,i)
        return ans