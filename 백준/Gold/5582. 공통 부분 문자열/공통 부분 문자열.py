import sys


def main(input=sys.stdin, output=sys.stdout):
    a = input.readline().strip()
    b = input.readline().strip()

    dp = [0 for _ in range(len(b) + 1)]

    ans = 0
    for i in range(1, len(a) + 1):
        carry = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                carry[j] = dp[j - 1] + 1
                ans = max(ans, carry[j])

        dp = carry

    output.write(f'{ans}')


if __name__ == '__main__':
    main()
