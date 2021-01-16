class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digit = list(str(N))
        check = len(digit)
        for i in range(len(digit) - 1, 0, -1):
            if digit[i] < digit[i - 1]:
                k = (int(digit[i - 1]) - 1)
                digit[i - 1] = str(k)
                check = i
        for i in range(check, len(digit)):
            digit[i] = '9'
        if digit[0] == '0':
            return int(''.join(digit[1:]))

        return int(''.join(digit))