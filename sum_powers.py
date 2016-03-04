user_input = raw_input("enter a float number: ")
b = float(user_input)
while b == 1.0:
    user_input = raw_input("enter a float number not equal to 1.0: ")
    b = float(user_input)

user_input = raw_input("enter a natural number: ")
n = int(user_input)

subt = 0
i = 0
while i <= n:
    subt += b**i
    i += 1

print subt
print (b**(n+1)-1)/(b-1)
