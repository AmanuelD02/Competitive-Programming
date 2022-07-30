class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        # print(path)
        for p in path:
            if p == "" or p == '.':
                continue
      
            
            if p == "..":
                if stack:
                    stack.pop()
            else:
                # print(p)
                stack.append(p)
        # print(stack)
        res = "/" + "/".join(stack)
        
        return res