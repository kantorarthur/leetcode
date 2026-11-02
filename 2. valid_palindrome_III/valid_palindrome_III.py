def is_valid_palindrome(s: str, k: int) -> bool:
    
    if len(s) == 1:
        return True
    if k == 0:
        return is_palindrome(s, 0, len(s) - 1)

    mem = {}
    
    def DFS(s: str, left: int, right: int, k: int) -> bool:
        if (left, right, k) is mem:
            return mem[(i, j, k)]
        elif k == 0:
            return is_palindrome(s, left, right)
        else:
            while left < right:
                if s[left] != s[right]:
                    mem[(left, right, k)] = DFS(s, left + 1, right, k - 1) or DFS(s, left, right - 1, k - 1)
                    return mem[(left, right, k)]
                left += 1
                right -= 1

            mem[(left, right, k)] = True
        return mem[(left, right, k)]

    return DFS(s, 0, len(s) - 1, k)
        
            
#"abcdeca"    

def is_palindrome(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

