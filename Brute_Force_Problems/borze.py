import sys
input = sys.stdin.readline

"""
Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

Input
The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).

Output
Output the decoded ternary number. It can have leading zeroes.

Examples

Input
.-.--

Output
012

Input
--.

Output
20

Input
-..-.--

Output
1012

"""

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