class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        l, r = 0, 1
        
        mem = set()
        cnt = 0
        for n in range(1, len(text) // 2 + 1): # O(n)
            while r + n <= len(text):  # O(n)
                if (text[l:l+n] == text[r:r+n] and text[l:l+n] not in mem): 
                    cnt += 1
                    mem.add(text[l:l+n])
                l += 1
                r += 1
            l = 0 
            r = n + 1
        return cnt
            
            
        
         
