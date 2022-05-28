# The string "SUNDIALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# S  D  L  H  I
# U  I  I  I  N
# N  A  S  R  G

# And then read line by line: "SDLHIUIIINNASRG"

# Write the code that will take a string and make this conversion given a number of rows. 

# Number of rows: 3
# Input: SUNDIALISHIRING
# Output: SDLHIUIIINNASRG

#SUNDIALISHIRI

#SDLHIUIIINNASRG

from sys import stdout
def solve(s, n):
    if n < 1 or type(n) == float : raise Exception("N should be positive integer")
    length = len(s)
    for row in range(n):
        for col in range(length//n):
            stdout.write(s[n*col + row])
        if row < length % n:
            stdout.write(s[(length//n)*col + row])

solve("SUNDIALISHIRING", 3)
#S I S I
#U A H N
#N L I G
#D I R

#SISIUAHNNLIGDIR
#print(solve("SUNDIALISHIRING", 3) == "SDLHIUIIINNASRG")
