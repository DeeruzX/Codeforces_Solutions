a, b = map(int, input().split())
solve = 0
while b >= a:
    a *= 3
    b *= 2
    solve += 1
 
print(solve)
