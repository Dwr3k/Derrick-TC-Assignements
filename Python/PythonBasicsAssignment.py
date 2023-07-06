print("Hello World!")

print("/-------\\")
print("|       |")
print("|       |")
print("|       |")
print("|-------|")

name = "drem"
age = "12"

print("The line about the name " + name)
print(f"The line about the {age}")


for letter in "the phrase":
    print(letter)

for x in ["one", "two", "three"]:
    print(x)

twoD_list = [[1,2,3],[4,5,6],[7,8,9]]
print(twoD_list[0][2])
print(twoD_list[1][0])

for group in twoD_list:
    for item in group:
        print(item)

first = float(input("Enter first number "))
second = float(input("Enter second Number"))
print(first + second)

colour = input("Enter Colour ")
plural_noun = input("Enter plural Noun ")
celebrity = input("Enter Celebrity Name ")

print(f"Roses are {colour}")
print(f"Violets are {plural_noun}")
print(f"I really like {celebrity}")

tempList = ['a','b','c','d','e']
print(tempList[2:len(tempList)])
print(tempList[2:len(tempList):2])

tempList.append('g')
print(tempList)
print(tempList.pop())
print(tempList.index('b'))
tempList.append('a')
print(tempList.count('a'))
print(reversed(tempList))

coord = (1,2,3,4,5,6,7,8)
print(coord[4])


def better_calc():
    first = float(input("Enter first number"))
    operand = input("Enter operation: ")
    second = float(input("Enter second number"))

    if operand == '+':
        return first + second
    elif operand == '-':
        return first - second
    elif operand == '%':
        return first % second
    elif operand == '/':
        return first / second
    elif operand == '*':
        return first * second
    else:
        print("Invalid Operand Entered")


print(better_calc())

month_conversion = {"Jan": "January", "Feb": "February", "Mar": "March"}

print(month_conversion)
print(month_conversion.get("Ge", "Not REAL"))
print(month_conversion.get("Jan"))



def guessing_game():
    secret = "The Money"
    guesses = 0
    failed = False

    while not failed:
        guessed = input("Guess word ")
        guesses += 1

        if guessed == secret:
            print("You Win!")
            return
        if guesses == 5:
            failed = True
    print("You failed")


guessing_game()


def raise_power(base, raised):
    result = 1
    for i in range(raised):
        result *= base

    return result
from functools import reduce

#print(raise_power(3, 2))

odds = list(filter(lambda x: x%2==0, list(range(10))))
evens = list(map(lambda x: x+1, odds))
print(odds)
print(evens)
together = list(zip(odds,evens))
print(together)

lambFunc = lambda x, a: (x*2) + a
print(lambFunc(2,6))

tempList = [1,2,3,4,]
tempList = list(map(lambda x: x*3, tempList))
print(tempList)
print(reduce(lambda x,y: x * y, tempList))
tempList = list(filter(lambda x: x % 6 != 0, tempList))
print(tempList)

print(list(map(lambda x: x*x, [5,4,3])))
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort()
print(a)
a.sort(key=lambda x: x[1])
print(a)

wordList = [char for char in 'new List']
intList = [num*1.4 for num in range(1,10)]
nums = [num *2.3 for num in range(1,50) if num % 2 == 0]
print(wordList)
print(intList)
print(nums)

sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

test_dict = {key:value-3 for key,value in sample_dict.items()}
print(test_dict)

finalList = [x for x in 'abcdefghijklmnop']
finalList = finalList*2
finalList.append('w')
finalList.append('z')
finalList.sort()
print(finalList)

duplicates = list(set([x for x in finalList if finalList.count(x) > 1]))
duplicates.sort()
print(duplicates)