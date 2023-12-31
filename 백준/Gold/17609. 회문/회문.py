import sys

def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def check(char):
    start = 0
    end = len(char) - 1
    remove = False

    while start < end:
        if char[start] == char[end]:
            start += 1
            end -= 1
        else:
            if not remove:
                if is_palindrome(char, start + 1, end):
                    return 1
                elif is_palindrome(char, start, end - 1):
                    return 1
                else:
                    return 2
            else:
                return 2

    return 0

T = int(sys.stdin.readline())

for i in range(T):
    char = sys.stdin.readline().strip()
    print(check(char))
