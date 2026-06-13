class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n=0
        d={}
        val=[0]*(len(words))
        for i in "abcdefghijklmnopqrstuvwxyz":
            d[i]=weights[n]
            n+=1
        for i in range(len(words)):
            for j in words[i]:
                val[i]+=d[j]
        newd = {
    "26": "a", "25": "b", "24": "c", "23": "d", "22": "e", "21": "f",
    "20": "g", "19": "h", "18": "i", "17": "j", "16": "k", "15": "l",
    "14": "m", "13": "n", "12": "o", "11": "p", "10": "q", "9": "r",
    "8": "s", "7": "t", "6": "u", "5": "v", "4": "w", "3": "x",
    "2": "y", "1": "z"
}
        ans=""
        for i in val:
            ans+=newd[str(i%26 +1)]
        return ans