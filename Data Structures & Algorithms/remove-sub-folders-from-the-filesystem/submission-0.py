class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Use the hashset algorithn

        # initialize result to an empty array
        res = []
        folder_set = set(folder) # hashset for constant look up

        for f in folder: # iterate through each subfolder in folder list
            res.append(f) # append the folder to res
            # Scan through the path and check every prefix that ends just before a "/"
            for i in range(len(f)):
                if f[i] == "/" and f[:i] in folder_set:
                    res.pop()
                    break
        return res

            
