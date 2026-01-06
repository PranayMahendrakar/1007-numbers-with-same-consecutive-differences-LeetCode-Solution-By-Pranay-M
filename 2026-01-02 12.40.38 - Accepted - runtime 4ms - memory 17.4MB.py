class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))
        
        result = []
        
        def dfs(num, length):
            if length == n:
                result.append(num)
                return
            
            last_digit = num % 10
            next_digits = set()
            
            if last_digit + k <= 9:
                next_digits.add(last_digit + k)
            if last_digit - k >= 0:
                next_digits.add(last_digit - k)
            
            for d in next_digits:
                dfs(num * 10 + d, length + 1)
        
        # Start with digits 1-9 (no leading zeros)
        for i in range(1, 10):
            dfs(i, 1)
        
        return result