user_input = raw_input("Temperature of Tea: ")
T_tea = int(user_input)

user_input = raw_input("Temperature of Room: ")
T_air = int(user_input)

user_input = raw_input("Number of Minutes: ")
num_minutes = int(user_input)
print "minute temperature"
k = 0.055

t = 0
temp = T_tea
while t < num_minutes:
    temp = temp - k*(temp-T_air)
    print "%4.1d     %4.2f" %(t, temp)
    t += 1
