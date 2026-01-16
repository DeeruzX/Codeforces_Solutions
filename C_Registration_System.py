leng = int(input())
 
sing_in_checker = dict()
 
for _ in range(leng):
    main_input = str(input())
    if main_input not in sing_in_checker:
        sing_in_checker[main_input] = 1
        print("OK")
    else:
        sing_in_checker[main_input] += 1
        print(f"{main_input}{sing_in_checker[main_input]-1}")
