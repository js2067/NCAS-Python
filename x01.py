# Exercise 2.2
#gases = ['He', 'Ne', 'Ar', 'Kr']
#count = 0
#while count < 4:
#    for i in gases:
#        print(i)
#    count += 1

# Exercise 2.3

#if name == 'Lisa':
#    print('plays saxophone')
#elif name == 'Bart':
#    print('rides skateboard')
#else:
#    print(name) + ('lives in Springfield')

#Exercise 3.1
#x = [1, 2, 3, 4, 5]

#second = x[1]
#second_to_last = x[3]
#complete_list = x[0:5]
#second_to_fourth = x[1:4]

#print(str(second) + " " + str(second_to_last) + " " + str(complete_list) + " " + str(second_to_fourth))

#Exercise 3.2

#y = list(range(11))
#print(y)
#y[0] = 10
#print(y)
#y.append(11)
#print(y)
#y.extend([12, 13, 14])
#print(y)

# Exercise 3.3

#forward = []
#backward = []
#values = ['a', 'b', 'c']
#for i in values:
#    forward.append(i)
#    backward.insert(0, i)
#print(forward)
#print(backward)
#forward.reverse()

#if forward == backward:
#    print("Lists are the same!")
#else:
#    print("Lists are not the same!")

# Exercise 3.4

#countries = ['uk', 'usa', 'uk', 'uae']
#print(countries.count('uk'))

#-------------------------------

#Exercise 4.1

#t = (1,)
#print(t[0])
#y = list(range(100, 200))
#tuple_list = tuple(y)
#print (str(tuple_list[0]) + " " + str(tuple_list[99]))
       
#Exercise 4.2

#mylist = [23, 'hi', 2.4e-10]
#for (count, item) in enumerate(mylist):
#    print(count, item)
    
#Exercise 4.3

#first, middle, last = mylist
#print(str(first) + ' ' + str(middle) + ' ' + str(last))
#first, middle, last = middle, last, first
#print(str(first) + ' ' + str(middle) + ' ' + str(last))

#---------------------------------

#Exercise 5.1

#with open('weather.csv', 'r') as reader:
#    data = reader.read()
#    print(data)
    
#print(' ')

#Exercise 5.2

#with open('weather.csv', 'r') as reader:
#    while True:
#         line = reader.readline()
#         if not line:
#	      break
#	 print(line)
#    print('Its over')

#Exercise 5.3

#with open('weather.csv', 'r') as reader:
#    reader.readline()
#    rain = []
#    for line in reader:
#         print(line)
#         data = line.strip().split(",")[-1]
#         data = float(data)
#         rain.append(data)
#    for i in rain:
#         print(i)
         
#with open('myrain.txt', 'w') as writer:
#    for i in rain:
         
  


#---------------------------


#Exercise 6.1

#s = 'I love to write python'
#for char in s:
#    print(char)
    
#print(s[6])
#print(s[-1])
#print(len(s))
#print(s[0])
#print(s[0][0])
#print(s[0][0][0])

#print(' ') 

#Exercise 6.2

#s = 'I love to write Python'
#split_s = s.split()
#for word in split_s:
#    if word.count('i') > 0:
#         print(f"I found 'i' in {word}")

#print(' ')

#Exercise 6.3
#something = 'Completely Different'
#print(something.count('t'))
#print(something.find('plete'))
#print(something.split('e'))

#thing2 = something.replace('Different', 'Silly')
#print(thing2)
         
    

#----------------------------

#Exercise 7.1

#print(' ')
#a = [0,1,2]
#b = a
#print(f'{a} and {b}')
#b[0] = 'hello'
#print(f'{a} and {b}')
#a.append(3)
#print(f'{a} and {b}')

#print(' ')

#Exercise 7.2

#a = 'can I change'
#b = a
#print(f'{a} and {b}')
#b = 'different'
#print(f'{a} and {b}')

#print (' ')

#Exercise 7.3

#a = [0,1,2]
#import copy
#b = copy.deepcopy(a)
#print(f'{a} and {b}')
#b[0] = 'hello'
#print(f'{a} and {b}')


#--------------------------

#Exercise 8.1 

#print(' ')

#def double_it(number):
#    return number * 2
#print(double_it(2))
#print(double_it(2.5))
#print(double_it('two'))
#print(' ')


#Exercise 8.2 / 8.3

#def calc_hypo(a, b):
#    if type(a) not in (int, float) or type(b) not in (int, float):
#         print('Bad argument')
#         return False
#    elif a <= 0 or b <= 0:
#         print('Bad argument')
#         return False
#    else:
#         hypo = ((a*a) + (b*b))**0.5
#         return hypo
     
#print(calc_hypo(3, 4))
#print(calc_hypo(3.5, 4))
#print(calc_hypo('three', 4))



#-----------------------

#Exercise 9,1

import sys
from dancing.dance import boogie
moves = sys.argv

boogie(moves)


  







