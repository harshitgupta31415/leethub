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
                    if i is not ".":
                        ans.append(i)
        res="/"
        print(ans)
        if not ans:
            return res
        for i in ans:
            res+=i+"/"
        return res[:-1]
