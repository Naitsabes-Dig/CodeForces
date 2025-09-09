import sys

def calculate_flagstones(n, m, a):
    num_flagstones_n = (n + a - 1) // a
    num_flagstones_m = (m + a - 1) // a
    total_flagstones = num_flagstones_n * num_flagstones_m
    
    return total_flagstones

if __name__ == "__main__":
    try:
        n, m, a = map(int, sys.stdin.readline().split())
        result = calculate_flagstones(n, m, a)
        print(result)
        
    except ValueError:
        print("Invalid input. Please enter three positive integers separated by spaces.")
