import random

print('Quel est ton nom?')
name = input()

print('Salut ' + name + ' je pense à un nombre entier entre 1 et 10, essaye de le trouver. Tu as 5 essais.')

secret_number = random.randint(1, 10)

for guesses in range(1, 6):
    guess = int(input())

    if guess > secret_number:
        print('Moins')
    elif guess < secret_number:
        print('Plus')
    else:
        break #Si cette condition est remplie, le nombre mystère a été trouvé.

if guess == secret_number:
    print('Bravo ' + name + ' ! Tu as trouvé le nombre secret en ' + str(guesses) + ' essais.')
else:
    print('Dommage ' + name + ' ! Le nombre auquel je pensais était ' + str(secret_number) + '.')

