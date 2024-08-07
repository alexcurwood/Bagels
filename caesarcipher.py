try:
    import pyperclip
except:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caeser Cipher')
print('THe Caesar cipher encrypts letters by shifting them over by a')
print('key numver. For example, a key of 2 means the letter A is')
print('encrypted into C.')
print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')

while True:
    maxKey = len(SYMBOLS) -1
    print('Please enter the key (0 to {})'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}'.format(mode))
message = input('> ')

message = message.upper()

translated =''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard'.format(mode))
except:
    pass

