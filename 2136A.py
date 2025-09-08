def check_match():
    a, b, c, d = map(int, input().split())

    # Check first half
    if a > 2 * b + 2 or b > 2 * a + 2:
        print("NO")
        return

    # Check second half
    a_prime = c - a
    b_prime = d - b

    if a_prime > 2 * b_prime + 2 or b_prime > 2 * a_prime + 2:
        print("NO")
        return

    print("YES")

t = int(input())
for _ in range(t):
    check_match()