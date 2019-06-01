
x = int(input("Enter an integer please! "))
NumGuesses = 0
epsilon = 0.01
high = x
low = 0
ans = (high+low)/2

while abs(ans**2-x) >= epsilon:
    print("Low=%s Ans=%s Haigh=%s" % (low, ans, high))
    NumGuesses += 1

    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low)/2

print("Number of guesses is ", NumGuesses)
print(round(ans))
