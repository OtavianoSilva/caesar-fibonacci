import string

ALPHABET = string.ascii_lowercase
ALPHABET_SIZE = len(ALPHABET)


def fibonacci_sequence(length: int) -> list[int]:
    """
    Generate a Fibonacci sequence with the given length.
    The first two values are 1 and 1.
    """
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
    Encrypt text using a Caesar cipher whose shift follows
    the Fibonacci sequence.

    Only alphabetic characters are encrypted.
    Spaces and punctuation are preserved.
    """

    text = text.lower()

    letter_count = sum(char.isalpha() for char in text)
    fibonacci = fibonacci_sequence(letter_count)

    encrypted = []
    shifts = []

    fib_index = 0

    for char in text:

        if char.isalpha():

            shift = fibonacci[fib_index] % ALPHABET_SIZE
            shifts.append(shift)

            original_index = ALPHABET.index(char)
            encrypted_index = (original_index + shift) % ALPHABET_SIZE

            encrypted.append(ALPHABET[encrypted_index])

            fib_index += 1

        else:
            encrypted.append(char)

    return "".join(encrypted), shifts


def main():

    text = '''Tell me, Muse, of the man of many ways, who was driven
far journeys, after he had sacked Troy's sacred citadel.
Many were they whose cities he saw, whose minds he learned of,
many the pains he suffered in his spirit on the wide sea,
5 struggling for his own life and the homecoming of his companions.
Even so he could not save his companions, hard though
he strove to; they were destroyed by their own wild recklessness, fools,
who devoured the oxen of Helios, the Sun God, and he took away the day
of their homecoming. From some point'''

    encrypted_text, shifts = caesar_fibonacci_encrypt(text)

    print("Original text:")
    print(text)

    print("\nEncrypted text:")
    print(encrypted_text)

    print("\nFibonacci shifts:")
    print(shifts)


if __name__ == "__main__":
    main()