def main():
    list1 = [input() for i in range(2)]
    target, pool = parse(list1)
    flag = "Yes" if judge(target, pool) else "No"
    print(flag)

def parse(list1):
    target = list1[0].split(" ")[1]
    pool = list1[1].split(" ")
    return target, pool

def judge(target, pool):
    return target in pool


if __name__ == "__main__":
    main()
