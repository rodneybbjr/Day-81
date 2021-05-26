

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
    """Takes in plain-text (message), returns string as morse-code."""
    morse_dict = text_to_morse
    morse_code = [f'{morse_dict[char]}' for char in message]
    return ' '.join(morse_code)


def to_text(morse_code):
    """Takes in morse_code, returns string as plain-text."""
    morse_dict = {v: k for k, v in text_to_morse.items()}
    morse_dict.update(special)
    message = [''.join([f'{morse_dict[char]}'for char in word.split(' ')]) for word in morse_code.split('/')]
    return ' '.join(message)


IS_RUNNING = True

while IS_RUNNING:

    choice = input("Are you converting to: (text) or (morse) or (e)xit ").lower()

    if choice in ('e', 'exit'):
        IS_RUNNING = False
    elif choice in ('morse', 'text'):
        text_to_convert = input("Enter the message you want to convert:\n").casefold()
        if choice == 'morse':
            print(to_morse(text_to_convert))
        elif choice == "text":
            print(to_text(text_to_convert))
