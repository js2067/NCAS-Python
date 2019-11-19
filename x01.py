# Exercise 2.2
#gases = ['He', 'Ne', 'Ar', 'Kr']
#count = 0
#while count < 4:
#    for i in gases:
#        print (i)
#    count += 1

# Exercise 2.3

#if name == 'Lisa':
#    print ('plays saxophone')
#elif name == 'Bart':
#    print ('rides skateboard')
#else:
#    print (name) + ('lives in Springfield')

#Exercise 3.1
x = [1, 2, 3, 4, 5]

second = x[1:2]
second_to_last = x[3:4]
complete_list = x[0:5]
second_to_fourth = x[1:4]

print (str(second) + " " + str(second_to_last) + " " + str(complete_list) + " " + str(second_to_fourth))

#Exercise 3.2

y = list(range(11))
print (y)
y[0] = 10
print (y)
y.append(11)
print (y)
y.extend([12, 13, 14])
print (y)

# Exercise 3.3

forward = []
backward = []
values = ['a', 'b', 'c']
for i in values:
    forward.append(i)
    backward.insert(0, i)
print (forward)
print (backward)
forward_reversed = forward.reverse()
if forward_reversed == backward:
    print ("Lists are the same!")
else:
    print ("Lists are not the same!")

# Exercise 3.4



