def caesarCipher(s, k):
    code = ""
    k = k % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    nalphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet[k:]
    alphabet += nalphabet[0:k]
    for a in range(len(s)):
        print(s[a])
        if s[a].isalpha():
            if s[a].isupper():
                code += alphabet[nalphabet.index(s[a].lower())].upper()
            else:
                code += alphabet[nalphabet.index(s[a])]
        else:
            code += s[a]
    return code
