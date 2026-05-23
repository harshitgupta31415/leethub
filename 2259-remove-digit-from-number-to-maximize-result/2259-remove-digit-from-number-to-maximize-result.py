class Solution:
    def removeDigit(self, numbers: str, digit: str) -> str:
        mx=0
        for i in range(len(numbers)):
            if numbers[i]==digit:
                mx=max(mx,int(numbers[:i]+numbers[i+1:]))
        return str(mx)