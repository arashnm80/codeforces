t = int(input())

ans = []

for case in range(t):
    s = input()
    
    lowers = []
    uppers = []

    for i in range(len(s)):
        if s[i].islower():
            if s[i] == "b":
                if len(lowers) > 0:
                    lowers.pop()
            else:
                lowers.append(i)
        else:
            if s[i] == "B":
                if len(uppers) > 0:
                    uppers.pop()
            else:
                uppers.append(i)

    line = ""
    combined = sorted(lowers + uppers)
    for i in combined:
        line += s[i]
    ans.append(line)

# print()
print("\n".join(ans))


#     j = 0
#     while j < len(s):
#         if s[j] == "b":
#             del s[j]
#             for i in range(j - 1, -1, -1):
#                 if s[i].islower():
#                     del s[i]
#                     j -= 1
#                     break

#         elif s[j] == "B":
#             del s[j]
#             for i in range(j - 1, -1, -1):
#                 if s[i].isupper():
#                     del s[i]
#                     j -= 1
#                     break
#         else:
#             j += 1
    
#     # print("".join(s))

#     item = "".join(s)
#     ans.append(item)

# print("\n".join(ans))
