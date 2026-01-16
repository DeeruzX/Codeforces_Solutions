
test_num = int(input())
solve = 0
for _ in range(test_num):
    main_input = input()
    if main_input.count("1") >= 2:
        solve += 1
print(solve)
