test_num = int(input())

for _ in range(test_num):
      main_input = input()
      if len(main_input) > 10:
          print(f"{main_input[0]}{len(main_input)-2}{main_input[-1]}")
      else:
          print(main_input)
