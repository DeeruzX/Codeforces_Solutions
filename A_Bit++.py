test_num = int(input())
solve = 0
for _ in range(test_num):
    main_input = input()
    if "+" in main_input:
        solve += 1
    else:
        solve -= 1
print(solve)
