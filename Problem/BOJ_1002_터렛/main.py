from sys import stdin


def main():
    test_case = int(stdin.readline().rstrip())

    for _ in range(test_case):
        X1, Y1, R1, X2, Y2, R2 = map(int, stdin.readline().split())

        distance = ((X1 - X2) ** 2 + (Y1 - Y2) ** 2) ** 0.5

        # 1. 두 원이 동일할 경우 => -1
        if distance == 0 and R1 == R2:
            print(-1)
        # 2. 두 원이 두점에서 만날 경우 => 2
        elif abs(R1 - R2) < distance < R1 + R2:
            print(2)
        # 3. 두 원이 한점에서 만날 경우 => 1
        elif distance == R1 + R2 or distance == abs(R1 - R2):
            print(1)
        elif distance == 0 or abs(R1 - R2) > distance or R1 + R2 < distance:
            print(0)


if __name__ == "__main__":
    main()
