import sys
input = sys.stdin.readline

def solve():
    borze_code = input().strip()
    output = ""
    i = 0
    while i < len(borze_code):
        if borze_code[i] == ".":
            output += "0" 
            i +=1
        elif borze_code[i:i+2] == "-.":
            output += "1"
            i += 2 
        else:
            output += "2"
            i += 2 
    print(output)

if __name__ == "__main__":
    solve()