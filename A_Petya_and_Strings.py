x_input = input().lower()
y_input = input().lower()

x_ord = 0
y_ord = 0
solve = 0

for i in range(len(x_input)):
    x_ord = ord(x_input[i])
    y_ord = ord(y_input[i])
    if x_ord > y_ord:
        solve = 1
        break
    elif y_ord > x_ord:
        solve = -1
        break
print(solve)
