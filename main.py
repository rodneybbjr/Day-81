
text_to_morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/'
}

special = {
        ' ': '',
        '/': '',
        '': '',
}


def to_morse(message):
    morse_dict = text_to_morse
    morse_code = [f'{morse_dict[char]}' for char in message]
    s = ' '
    return s.join(morse_code)


def to_text(morse_code):
    morse_dict = {v: k for k, v in text_to_morse.items()}
    morse_dict.update(special)
    s = ' '
    message = [''.join([f'{morse_dict[char]}'for char in word.split(' ')]) for word in morse_code.split('/')]
    return s.join(message)


def convert_text(choice, text):

    if choice == 'morse':
        result = to_morse(text)
        return print(result)
    elif choice == "text":
        result = to_text(text)
        return print(result)
    else:
        print("Not valid response. Please try again.")
        convert_text(choice, text)


is_running = True

while is_running:

    convert = input("Are you converting to: (text) or (morse) ").lower()

    if convert == 'exit':
        exit()
    else:
        text_to_convert = input("Enter the message you want to convert:\n").casefold()
        convert_text(convert, text_to_convert)







