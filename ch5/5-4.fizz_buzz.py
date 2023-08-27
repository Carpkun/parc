#3의 배수인 경우 "Fizz", 5의 배수인 경우 "Buzz", 3과 5의 배수 둘 다인 경우는 "FizzBuzz"라고 출력하는 게임

#Write your code below this row 👇

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)