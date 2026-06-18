class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans=[]
        for i in path:
            if i != "":
                if i =="..":
                    if ans:
                        ans.pop()
                else:
                    if i != ".":
                        ans.append(i)
        res="/"
        if not ans:
            return res
        for i in ans:
            res+=i+"/"
        return res[:-1]
