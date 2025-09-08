def solve():
    n, k = map(int, input().split())
    s = input()
    
    # Check for consecutive '1's of length k or more
    consecutive_ones = 0
    for char in s:
        if char == '1':
            consecutive_ones += 1
            if consecutive_ones >= k:
                print("NO")
                return
        else:
            consecutive_ones = 0
            
    print("YES")
    
    # Separate indices
    zeros_indices = []
    ones_indices = []
    for i in range(n):
        if s[i] == '0':
            zeros_indices.append(i)
        else:
            ones_indices.append(i)
            
    p = [0] * n
    
    # Assign largest numbers to '0' indices
    current_val = n
    for i in zeros_indices:
        p[i] = current_val
        current_val -= 1
        
    # Assign smallest numbers to '1' indices
    current_val = 1
    for i in ones_indices:
        p[i] = current_val
        current_val += 1
        
    print(*p)

t = int(input())
for _ in range(t):
    solve()