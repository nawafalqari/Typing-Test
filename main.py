from readchar import readkey
from colorama import init, Fore, Back, Style
from termcolor import colored
from time import sleep, time
from pyfiglet import figlet_format

init(autoreset=True)

print(f'\n{figlet_format("Nawaf")}')
print(f"Made by Nawaf in 2021, {colored('https://nawaf.cf', 'white', attrs=['underline'])}")

text = 'On the other hand, we denounce with righteous indignation'

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
