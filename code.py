import string
import unicodedata

ALPHABET = string.ascii_lowercase
ALPHABET_SIZE = len(ALPHABET)


def remove_accents(text: str) -> str:
    """
    Remove acentos, preservando o restante do texto.
    Ex:
        á -> a
        ç -> c
        Ê -> E
    """
    normalized = unicodedata.normalize("NFD", text)

    return "".join(
        c
        for c in normalized
        if unicodedata.category(c) != "Mn"
    )


def fibonacci_sequence(length: int) -> list[int]:
    if length <= 0:
        return []

    if length == 1:
        return [1]

    sequence = [1, 1]

    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def caesar_fibonacci_encrypt(text: str) -> tuple[str, list[int]]:
    """
    Cifra de César usando deslocamentos da sequência de Fibonacci.

    - Mantém maiúsculas/minúsculas.
    - Remove apenas os acentos.
    - Mantém pontuação, espaços e números.
    """

    text = remove_accents(text)

    letter_count = sum(char.lower() in ALPHABET for char in text)

    fibonacci = fibonacci_sequence(letter_count)

    encrypted = []
    shifts = []

    fib_index = 0

    for char in text:

        lower = char.lower()

        if lower in ALPHABET:

            shift = fibonacci[fib_index] % ALPHABET_SIZE
            shifts.append(shift)

            original_index = ALPHABET.index(lower)
            encrypted_index = (original_index + shift) % ALPHABET_SIZE

            new_char = ALPHABET[encrypted_index]

            # Preserva maiúsculas
            if char.isupper():
                new_char = new_char.upper()

            encrypted.append(new_char)

            fib_index += 1

        else:
            encrypted.append(char)

    return "".join(encrypted), shifts


def main():

    text = """Lorem ipsum"""

    encrypted_text, shifts = caesar_fibonacci_encrypt(text)

    print("Original:")
    print(text)

    print("\nCriptografado:")
    print(encrypted_text)

    print("\nDeslocamentos:")
    print(shifts)


if __name__ == "__main__":
    main()