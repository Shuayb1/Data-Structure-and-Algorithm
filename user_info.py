# def go(n):
#     if n==1:
#         return 1
#     else:
#         return n*go(n-1)
# print(go(4))
#
# def re(n):
#     pro = 1
#     for i in range(1,n+1):
# #         pro *= i
# #     return pro
# # re(4)
# def do(u):
#     assert type(u) != int, 'age is int'
# do()
#
# P = 10000
# n = 12
# r = 0.08
# t = int(input('No of years: '))
#
# A = P*(1 + (r/n))**(n*t)
# print(A)

# print((51%24)+14)


#LECTURE 1
#
# pi = 3.14159
# radius = 2.2
# radius = radius + 1
#
# area = pi*(radius**2)
# print(area)

#LECTURE2

# hi = "hello there"
# name = "ana"
# greet = hi + name
# print(greet)
# greeting = hi + " " + name
# print(greeting)
# silly = hi + (" " + name)*3
# print(silly)

# x = 1
# print(x)
# x_str = str(x)
# print("my fav number is", x, ".", "x=", x)
# print("my fav number is", x_str + "." + "x=" + x_str)
# print("my fav number is" + x_str + "." + "x=" + x_str)

# text = input("Type anything... ")
# print(5*text)
# num = int(input("Type a number... "))
# print(5*num)
#
# x = float(input('x is : '))
# y = float(input('y is : '))
# if x==y:
#     print('equal')
#     if y!=x:
#         print('unequal, x/y is %s'%x/y)
# elif x>y:
#     print('x bigger')
# elif x<y:
#     print('y is bigger')
# print('thanks')
#
# put = int(input('Whats nm: '))
# if put%2==0:
#     print('im even')
# else:
#     print('im odd')


#n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while n == "right" or n == "Right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\n\o/")



# n = 0
# while n < 5:
#     print(n)
#     n = n+1


# for n in range(5):
#     print(n)

# mysum = 0
# for i in range(10):
#    mysum += i
# print(mysum)
#
# mysum = 0
# for i in range(7, 10):
#    mysum += i
# print(mysum)
#
# mysum = 0
# for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        # mysum += 1
# print(mysum)

# count = 0
# flag = False
# inp = int(input('ur nmba: '))
# if inp < 0:
#     flag = True
# while count**2 < inp:
#     count += 1
# if count**2 == inp:
#     print('sqrt of ', inp, 'is', count)
# else:
#     print(inp, 'isnt  a perfct sqr')
#     if flag:
#         print('dd u mean', -inp,'?')

# count = 0
# check_neg =  False
# num = int(input('ur nmb: '))
# if num < 0:
#     check_neg = True
# while count**2 < num:
#     count += 1
# if count**2 == num:
#     print('swrrt of ', num, 'is', count)
# else:
#     print(num, 'isnt a pfctsq')
#     if check_neg:
#         print('dd u mran', -num,'?')

# LECTURE THREE
# s = "demo loops"
# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print('there is an i or u')
#
# for char in s:
#     if char == 'i' or char == 'u':
#         print('i or u there')


# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))
#
# for i in range(times):
#     print(word,'!!')

# cube = int(input('ent num: '))
# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print('not so')
# else:
#     if cube<0:
#         guess=-guess
#     print('ikkk')

# cube = int(input('number'))
# epsilon = 0.1
# guess = 0.0
# increment = 0.01
# num_guesses = 0
# look for close enough answer and make sure
# didn't accidentally skip the close enough bound
# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#    guess += increment
#    num_guesses += 1
# print('num_guesses =', num_guesses)
# if abs(guess**3 - cube) >= epsilon:
#    print('Failed on cube root of', cube, "with these parameters.")
# else:
#    print(guess, 'is close to the cube root of', cube)
#

# cube = 0.25
# epsilon = 0.01
# num_guesses = 0
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube:
#        # look only in upper half search space
#        low = guess
#     else:
#        # look only in lower half search space
#        high = guess
#    # next guess is halfway in search space
#     guess = (high + low)/2.0
#     num_guesses += 1
# print('num_guesses =', num_guesses)
# print(guess, 'is close to the cube root of', cube)

##LECTURE 4
#
# def even_return(i):
#     print('with return')
#     remain= i%2
#     return remain ==0
# print(even_return(int(input('num: '))))
#
# def simp(i):
#     de = i%2
#     return  de == 0
# print('\nlist 0-20 even or odd: ')
# for i in range(20):
#     if simp(i):
#         print(i, 'is even')
#     else:
#         print(i, 'is odd')
# print('\nGood Job')

# def bisection(x, ep):
#     low = 0.0
#     high = x
#     guess = (low + high) / 2.0
#     while (guess**3 - x) >= ep:
#                      # look only in upper half search space
#         if guess**3 < x:
#             low = guess
#             #        # look only in lower half search space
#         else:
#             high = guess
#             #    # next guess is halfway in search space
#         guess = (low + high) / 2.0
#     return guess
# x = 1
# while x <= 10000:
#     appro = bisection(x, 0.01)
#     print(appro, 'is close to cube of', x)
#     x *= 10

## EXAMPLE: functions as arguments
# def a():
#     print('is a')
#
# def b(y):
#     print('is b')
#     return y
#
# def c(z):
#     print('is c ')
#     return z
#
# print(a())
# print(5+b(2))
# print(c(a()))

## EXAMPLE: returning function objects
#
# def a():
#     def b(x,y):
#         return x+y
#     return b
# # the first part, f(), returns a function object
# # then apply that function with parameters 3 and 4
# c = a()(3,4)
# print(c)

## EXAMPLE: shows accessing variables outside scope
# def a(p):
#     x = 1
#     x += 1
#     print(x)
# x = 5
# a(x)
# print(x)
#
# def b(q):
#     pass
# x = 5
# b(x)
# print(x)

## EXAMPLE: hader scope example from slides
# def a(x):
#     # def b():
#     #     x = 'abc'
#     x = x+1
#     print('in a: x is ', x)
#     # b()
#     return x
# x=3
# c= a(x)

## EXAMPLE: complicated scope, test yourself!

# def a(x):
#     x += 1
#     print('in a: x, is ',x)
#     return x
# x = 3
# c = a(x)
# print('in main z,',c)
# print('in main x,',x)

# def a(x):
#     def b(y):
#         x = 1
#         x += 1
#         print('in b, x ix ', x)
#     x += 1
#     print('in a x is ', x)
#     b(x)
#     return x
# x = 3
# c = a(x)
# print('in main x is ', x)
# print('in main c is ', c)

#Lecture 5
# def cute(x,y):
#     q = x // y
#     r = x % y
#     return q,r
# (quo, rem) = cute(5,3)
# print(quo)
# print(rem)

## EXAMPLE: iterating over tuples
# def tup(tur):
#     num = ()
#     word = ()
#     for  i in tur:
#         num += (i[0],)
#         if i[1] not in word:
#             word += (i[1],)
#     minn = min(num)
#     maxx = max(num)
#     unik = len(word)
#     return minn,maxx,unik
#
# test = ((1,"a"),(2, "b"),
#         (1,"a"),(7,"b"))
# (a,b,c) = tup(test)
# print("a:",a,"b:",b,"c:",c)

# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()
# print(warm)
# print(sortedwarm)
#
# cool = ['grey', 'green', 'blue']
# sortedcool = sorted(cool)
# print(cool)
# print(sortedcool)

#  fibonanci
def fb(n):
    if n ==1:
        return 1
    elif n==2 :
        return 2
    else:
        return fb(n-1) + fb(n-2)
print(fb(12))




##Time compplexity, doing O'Notation
# import time
#
# def nice(d):
#     return d*9/5 + 32
# t0 = time.clock()
# nice(100000)
# t1 = time.clock() - t0
# print('t = ', t0, ':', t1, 's')

# def f(i,j):
#     print('with return')
#     rem = i%2
#     remi = rem+j
#     return rem == 0
#
# print(f(4,8))
# print(remi)