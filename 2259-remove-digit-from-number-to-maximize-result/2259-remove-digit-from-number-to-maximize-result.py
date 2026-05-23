class Solution:
    def removeDigit(self, numbers: str, digit: str) -> str:
        last_index = -1
        for i in range(len(numbers)):
            if numbers[i] == digit:
                last_index = i
                if i + 1 < len(numbers) and numbers[i+1] > numbers[i]:
                    return numbers[:i] + numbers[i+1:]
        return numbers[:last_index] + numbers[last_index+1:]


        
        """
        mx=""
        for i in range(len(numbers)):
            if numbers[i]==digit:
                mx=max(mx,numbers[:i]+numbers[i+1:])
        return mx
        """