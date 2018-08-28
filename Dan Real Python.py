# #Joining dict together
# we  = {'ade':1}
# ye  = {'sade':2}
# ze  = {'shade':3}
#
# you = {**we, **ze, **ye}
# print(you)
#
# # Different ways to test multiple
# # flags at once in Python
# x,y,z = 4,0,2
# # if x == 4 or y == 4 or z == 4:
# #     print('wwe r here')
# if 0 in(x,y,z):
#     print('second print')
#
# # These only test for truthiness:
# # if x or y or z:
# #     print('rree me')
# if not any((x,y,z)):
#     print('we here')
# else:
#     print('ferri')

hold_it = []

def is_word_guessed(secret_word, letters_guessed):
    #
    # for letters in letters_guessed:
    #     while letters in secret_word:
    #         hold_it.join(letters)
    #         return  hold_it
    #     if letters in hold_it:
    #         hold_it.replace(letters, '_ ')
    #         return hold_it
    for letter in secret_word:
        if letter in letters_guessed:
            print(hold_it.insert(letter))

        else:
            print(hold_it.append('_ '))

secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(is_word_guessed(secret_word,letters_guessed))


