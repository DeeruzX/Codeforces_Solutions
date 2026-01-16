main_input = input()
main_input = main_input.replace("+", "")
main_input = sorted(main_input)
 
if len(main_input) == 1:
    print(main_input[0])
else:
    print(f"{"+".join(main_input)}")
