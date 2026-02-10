from morse.mapping import MORSE

REVERSE_MORSE = {value: key for key, value in MORSE.items()}


def decode_word(morse_word):
    letters = []

    for symbol in morse_word.split():
        if symbol in REVERSE_MORSE:
            letters.append(REVERSE_MORSE[symbol])

    return "".join(letters)


def decode(morse_text):
    words = morse_text.split("|")
    decoded_words = []

    for word in words:
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)


if __name__ == "__main__":
    from morse.encoder import encode

    original_text = "abc ABC"
    morse = encode(original_text)
    decoded = decode(morse)

    print("Original: ", original_text.upper())
    print("Morse Code: ", morse)
    print("Decoded: ", decoded)
