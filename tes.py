starting_salary = float(input('Enter your starting salary:​ '))
r = 0.07

mini = starting_salary / 12
maxi = starting_salary * (1 + r/12) ** 12
midi = (maxi + mini) / 2.0
newmid = 0

while midi > 0.00:
    if midi < starting_salary:
        mini = midi
    else:
        maxi = midi

    midi = (maxi + mini) / 2.0
    newmid += 1
print('Best savings rate is', r)
print('Steps in Bisection Search ', newmid)


# cube = 27
# high = cube
# low = 0
# guess = (high + low) / 2.0
# epsilon = 0.01
# newgues = 0
#
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube:
#         low = guess
#     else:
#         high = guess
#
#     guess = (high + low) / 2.0
#     newgues += 1
#
# print('new guess is', newgues)
# print(guess,'is close to the target')

