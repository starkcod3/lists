if __name__ == '__main__':
    N = int(input())
    data = []
    for i in range(N):
        cmd = input().split(" ")
        method = cmd[0]
        if method == "print":
            print(data)
        else:
            eval(f"data.{method}({','.join(cmd[1:]) if len(cmd) > 1 else ''})")