from sys import stdout
def solve(s, n):
    if n < 1 or type(n) == float : raise Exception("N should be positive integer")
    length = len(s)
    for row in range(n):
        for col in range(length//n):
            stdout.write(s[n*col + row])
        if row < length % n:
            stdout.write(s[(length//n)*col + row])
