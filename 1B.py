
import sys

def convert_to_excel(row_str, col_str):

    col_num = int(col_str)
    result = ""
    while col_num > 0:
        remainder = (col_num - 1) % 26
        result = chr(ord('A') + remainder) + result
        col_num = (col_num - 1) // 26
    return result + row_str

def convert_to_rxcy(coord):
    split_index = 0
    for i in range(len(coord)):
        if coord[i].isdigit():
            split_index = i
            break
    
    col_letters = coord[:split_index]
    row_str = coord[split_index:]
    
    col_num = 0
    for char in col_letters:
        col_num = col_num * 26 + (ord(char) - ord('A') + 1)
        
    return f"R{row_str}C{col_num}"

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        
        for _ in range(n):
            coord = sys.stdin.readline().strip()
            
            is_rxcy = False
            if coord.startswith('R') and len(coord) > 1 and coord[1].isdigit():
                if 'C' in coord[2:]:
                    is_rxcy = True
            
            if is_rxcy:
                parts = coord.split('C')
                row_str = parts[0][1:]
                col_str = parts[1]
                print(convert_to_excel(row_str, col_str))
            else:
                print(convert_to_rxcy(coord))
    except (ValueError, IndexError):
        print("Invalid input format.")

if __name__ == "__main__":
    solve()
