test_num = int(input())
 
solve = 0
 
for _ in range(test_num):
    m, a, b, c = map(int, input().split())
    solve += m - min(m, a)
    solve += m - min(m, b)
    solve -= min(solve, c)
    print((m*2)-solve)
    solve = 0
