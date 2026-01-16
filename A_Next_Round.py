leng, place = map(int, input().split())
solve = 0
main_input = list(map(int, input().split()))
pass_num = main_input[place-1]
 
for i in main_input:
    if i >= pass_num and i > 0:
        solve += 1
print(solve)
