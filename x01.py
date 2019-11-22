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

#Exercise 9.3

#import sys
#from dancing.dance import boogie
#moves = sys.argv

#boogie(moves)


 #----------------------- 

#Exercise 10.1

#print(' ')
#a = set ([0, 1, 2, 3, 4, 5])
#b = set ([2, 4, 6, 8])

#print(a.union(b))
#print(a.intersection(b))

#print(' ')

#Exercise 10.2

#band = ['mel', 'geri', 'victoria', 'mel', 'emma']
#counts = { }
#for member in band:
#    if member not in counts:
#         counts[member] = 1
#    else:
#         counts[member] += 1
         
#    print(f'{member} is given on {counts[member]} occassion')

#print(' ')

#Exercise 10.3

#d = {'maggie': 'uk', 'ronnie': 'usa'}
#print(d.items())
#print(d.keys())    
#print(d.values())
#print(d.get('maggie'

#--------------------------------- NumPY Arrays

#import numpy as np

#Exercise 1.1

#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a1 = np.array([x], dtype = np.int32)
#a2 = np.array([x], dtype = np.float64)

#print(f'{a1} {a1.dtype}')
#print(f'{a2} {a2.dtype}')

#print(' ')

#Exercise 1.2
#zeros = np.zeros((2,3,4))
#print(zeros)
#ones = np.ones((2,3,4))
#print(ones)
#one_to_alot = np.arange((1000))
#print(one_to_alot)

#print(' ')

#Exercise 1.3
#a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
#print(a[1])
#print(a[1:4])

#print(' ')

#a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], 
#	      [1, 22, 4, 0.1, 5.3, -9],
#	      [3, 1, 2.1, 21, 1.1, -2]])

#print(a[:, 3])
#print(a[1:4, 0:4])
#print(a[1:, 2])

#--------------------------
      
#Exercise 2.1

#import numpy as np

#arr = np.array([range(4), range(10, 14)])
#print(np.shape(arr))
#print(np.size(arr))
#print(np.max(arr))
#print(np.min(arr))

#print (' ')

#Exercise 2.2

#print(np.reshape(arr, (2,2,2)))
#print(np.transpose(arr))
#print(np.ravel(arr))
#b = arr.astype(np.float64)
#print(b)


#---------------------

#Exercise 3.1

#import numpy as np

#print(' ')

#a = np.array([range(4), range(10, 14)])
#b = np.array([2, -1, 1, 0])
#print(a * b)
#b1 = b * 100
#b2 = b * 100.0
#print(b1)
#print(b2)
#print(b1 == b2)

#print(' ')

#Exercise 3.2

#arr = np.array([range(10)])

#print(arr < 3)

#condition = np.logical_or(arr < 3, arr > 8)
#logic = np.where(condition, arr * 5, arr - 5)
#print(logic)

#print(' ')

#Exercise 3.3

#def Total(u, v):
#    TotalMagnitude = ((u**2) + (v**2)) ** 0.5
#    condition = np.logical(TotalMagnitude > 0.1)
#    result =  np.where(condition, TotalMagnitude, 0.1)
#    print(result)
    
#u = np.array([[4, 5, 6], [2, 3, 4]])
#v = np.array([[2, 2, 2], [1, 1, 1]])
#print(Total(u, v)

#u = np.array([[4, 5, 0.01], [2, 3, 4]])
#v = np.array([[2, 2, 0.03], [1, 1, 1]])
#print(Total(u, v))

#---------------------------------

#import numpy as np
#import numpy.ma as MA

#Exercise 4.1

#print(' ')

#marr = MA.masked_array(range(10),fill_value = -999)
#print(marr)
#marr[2] = MA.masked
#print(marr)
#print(marr.mask)

#narr = MA.masked_where(marr > 6, marr)
#print(narr)
#print(narr.fill_value)

#print (' ')


#Exercise 4.2

#m1 = MA.masked_array(range(1, 9))
#print(m1)
#m2 = np.reshape(m1, (2,4))
#print(m2)
#m3 = MA.masked_where(marr < 7, marr)
#print(m3 * 100)
		     
#---------------------------- Matplotlib

import matplotlib.pyplot as plt
import matplotlib

#Exercise 1.1

#plt.plot(range(10))
#plt.pause(1)
      
#Exercise 1.2 / 1.3

#time = [0, 1, 2, 3, 4, 5, 6]
#CO2_conc = [250, 265, 272, 260, 300, 320, 389]
#temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

#plt.plot(time, CO2_conc, color = 'blue', ls = '--')
#plt.plot(time, temp, color = 'red', ls = '--')
#plt.title('Variation in CO2 levels over time')
#plt.ylabel('CO2 concentration / ppm')
#plt.xlabel('Time / decade')
#plt.savefig('Exercise1.png')
#plt.show()

#Exercise 2.1

#fig, ax1 = plt.subplots()
#time = range(7)
#CO2_conc = [250, 265, 272, 260, 300, 320, 389]
#temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

#ax1.plot(time, CO2_conc, color = 'red')
#ax1.set_ylabel('[CO2]', color = 'red')
#ax2 = ax1.twinx()
#ax2.plot(time, temp)
#ax2.set_ylabel('Temp / degC')
#ax1.set_xlabel('Time / decade')
#plt.show()

#Exercise 2.2

#fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

#plt.subplot(1, 3, 1)
#x = (range(0, 10, 1))
#plt.plot(x)
#plt.subplot(1, 3, 2)
#y = (range(10, 0, -1))
#plt.plot(y)
#plt.subplot(1, 3, 3)
#z = ([4] * 10)
#plt.plot(z)

#fig.tight_layout()
#plt.show()

#-----------------

#from datetime import datetime
#import serial
#import io

#ser = serial.Serial(
#  port = '/dev/ttyUSB0',
#  baudrate = 9600,
#  bytesize = serial.EIGHTBITS,
#  stopbits = serial.STOPBITS_ONE,
#  parity = serial.PARITY_NONE
#)

#outfile ='./temperature_readouts.tsv'

#dt = datetime.now()

#print(dt.strftime('%A, %B %d, %Y'))

#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding = 'ascii', newline = '\r')
#sio._CHUNK_SIZE = 1
		       
#with open(outfile, 'a') as f: 
#    while ser.isOpen():
#         temp_recorded = sio.readline()
#         dt = datetime.now()
#         f.write(dt.strftime('%Y-%m-%d %H:%M:%S \n' + temp_recorded + '\n'))
#         f.flush()

#ser.close()

#-----------------------------------

#infile = 'temperature_readouts.tsv'
#outfile = 'sensor-data.nc'
#from csv import reader

#def temp_kelvin(temp):
#    value = temp.strip("+").strip("C").lstrip("O")
#    return float(value) + 273.15
  
#times = []
#temps = []

#with open(infile, 'rt') as tsvfile:
#    tsvreader = reader(tsvfile, delimiter = '\t')
#    for row in tsvreader:
#         print(row)
#         times.append(row[0])
#         temps.append(temp_kelvin(row[1]))
	 




