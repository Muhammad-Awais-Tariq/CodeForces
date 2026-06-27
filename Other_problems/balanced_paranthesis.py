
full_string = input()
is_balanced = True
balance = 0
for letter in full_string:
    if balance < 0:
        is_balanced = False
        break
    if letter == "(":
        balance +=1
    elif letter == ")":
        balance -=1

if balance != 0:
    is_balanced = False

print("Balanced" if is_balanced else "Not balanced")