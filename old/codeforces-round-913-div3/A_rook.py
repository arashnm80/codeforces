t = int(input())
letters = "abcdefgh"

for case in range(t):
    s = input()
    letter = s[0]
    number = s[1]

    for i in range(1, 9):
        if i != int(number):
            print(letter + str(i))

    for ch in letters:
        if ch != letter:
            print(ch + str(number))