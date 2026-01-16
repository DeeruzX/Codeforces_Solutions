y_pos = 0
x_pos = 0
 
for i in range(5):
    main_input = list(map(int, input().split()))
    if 1 in main_input:
        y_pos = i+1
        x_pos = main_input.index(1)+1
 
print(abs(3-y_pos)+abs(3-x_pos))
