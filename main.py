from readchar import readkey
from colorama import init, Fore, Back, Style
from termcolor import colored
from time import sleep, time
from random import choice

init(autoreset=True)

print('''
 _   _                      __ 
| \ | | __ ___      ____ _ / _|
|  \| |/ _` \ \ /\ / / _` | |_ 
| |\  | (_| |\ V  V / (_| |  _|
|_| \_|\__,_| \_/\_/ \__,_|_|
''')
print(f"Made by Nawaf in 2021, {colored('https://nawaf.cf', 'white', attrs=['underline'])}\n")

text = choice(open('text.txt', 'r').read().strip().split(','))

print('Ready?')
sleep(1)
print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)
print('Go!')

print()

print(colored(text, 'grey', attrs=['bold']), end='\r')

score = 0
fails = 0

start = time()

for i in text:
    char = readkey()
    print(f'{Back.GREEN if char == i else str(Back.RED)}{char}', end='')
    if char == i:
        score += 1
    else:
        fails += 1
        
print(f'\n\nYour score: {score}/{len(text)}')
print(f'{Style.RESET_ALL}You took {round(time() - start)}s')
    























