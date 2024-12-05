class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        ver1= list(map(int,version1.split('.')))
        ver2=list(map(int,version2.split('.')))
        
        maxCount=max(len(ver1),len(ver2))

        for i in range(maxCount):
            v1= ver1[i] if i<len(ver1) else 0
            v2= ver2[i] if i<len(ver2) else 0

            if v1<v2:
                return -1
            
            if v1>v2:
                return 1
        
        return 0
