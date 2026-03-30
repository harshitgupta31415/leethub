class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return sorted(s1[::2])==sorted(s2[::2]) and sorted(s1[1::2])==sorted(s2[1::2])
        """
        even1,even2,odd1,odd2="","","",""
        
        for i in range(0,len(s1),2):
            even1+=s1[i]
            even2+=s2[i]
        for i in range(1,len(s1),2):
            odd1+=s1[i]
            odd2+=s2[i]
        return sorted(even1)==sorted(even2) and sorted(odd1)==sorted(odd2)
        """