
def decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += decrypted_char
        else:
            result += char
    return result

def try_all_shifts(ciphertext):
    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Provided cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAONG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFGURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Try all shift values to find the original quote
try_all_shifts(cryptogram)
