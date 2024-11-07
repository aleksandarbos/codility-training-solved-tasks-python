# Write a function that decodes a message from Morse code into English text.

# Input format:
# - A string containing Morse code characters ('.' and '-')
# - Words are separated by 3 spaces ('   ')
# - Letters within a word are separated by a single space (' ')
# - The input will only contain valid Morse code characters, spaces, and no other special characters

# Example:
# Input: ".... .   -.-- --- ..-"
# Output: "HI YOU"

# Constraints:
# - Input string length: 1 ≤ N ≤ 10000
# - Each Morse code character will be valid (corresponds to a letter A-Z or digit 0-9)
# - The decoded message will only contain uppercase letters, numbers, and spaces
# - Empty input string is not possible

# Performance requirements:
# Expected time complexity: O(N)
# Expected space complexity: O(N)
# where N is the length of the input string

MORSE_CODE = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',
    '.': 'E',     '..-.': 'F',  '--.': 'G',   '....': 'H',
    '..': 'I',    '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',   '.--.': 'P',
    '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',
    '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}


def solution(code: str) -> str:
    result: str = ""
    i = 0
    while i != -1:
        i = code.find(' ')
        if code[i:i+3] == '   ':  # new word
            result += MORSE_CODE[code[:i]] + " "
            i += 3
        elif i != -1:  # new letter
            result += MORSE_CODE[code[:i]]
            i += 1

        if i == -1:
            result += MORSE_CODE[code[:]]
        else:
            code = code[i:]
    return result


def solution2(code: str) -> str:
    words = code.split('   ')
    return " ".join("".join(MORSE_CODE[letter] for letter in word.split()) for word in words)


if __name__ == "__main__":
    def test_both(morse_input: str, expected: str):
        assert solution(
            morse_input) == expected, f"solution1 failed for input: {morse_input}"
        assert solution2(
            morse_input) == expected, f"solution2 failed for input: {morse_input}"
        print(f"✓ Test passed for: {morse_input} -> {expected}")

    # Now run all tests for both solutions
    test_both('.... ..', 'HI')
    test_both('.... ..   -.-- --- ..-', 'HI YOU')

    # Single letters
    test_both('.', 'E')
    test_both('..', 'I')

    # Single word with multiple letters
    test_both('.... . .-.. .-.. ---', 'HELLO')

    # Multiple words
    test_both('... --- ...', 'SOS')
    test_both('... --- ...   ... --- ...', 'SOS SOS')

    # Numbers
    test_both('.---- ..--- ...--', '123')

    # Mix of letters and numbers
    test_both('... --- ...   .---- ..--- ...--', 'SOS 123')

    # Longer message
    test_both('.... . .-.. .-.. ---   .-- --- .-. .-.. -..', 'HELLO WORLD')

    # Multiple spaces between words
    test_both('.-   -...   -.-.', 'A B C')

    print("\nAll tests passed for both solutions!")
