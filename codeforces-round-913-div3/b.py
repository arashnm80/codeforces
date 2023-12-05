import asyncio

async def process_case(s):
    s = list(s)

    j = 0
    while j < len(s):
        if s[j] == "b":
            del s[j]
            for i in range(j - 1, -1, -1):
                if s[i].islower():
                    del s[i]
                    j -= 1
                    break

        elif s[j] == "B":
            del s[j]
            for i in range(j - 1, -1, -1):
                if s[i].isupper():
                    del s[i]
                    j -= 1
                    break
        else:
            j += 1

    item = "".join(s)
    return item

async def main():
    t = int(input())
    cases = [input() for i in range(t)]

    tasks = [process_case(case) for case in cases]
    results = await asyncio.gather(*tasks)

    print("\n".join(results))

if __name__ == "__main__":
    asyncio.run(main())
