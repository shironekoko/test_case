def alternatingCharacters(s):
    d=0
    sl=list(s)
    for i in range(0, len(sl)-1):
        if sl[i]==sl[i+1]:
            d+=1
    return d

def alternate(s):
    lens = [0]
    letters = list(set(list(s)))
    for letter1 in range(len(letters)):
        for letter2 in range(letter1 + 1, len(letters)):
            two = []
            for letter in s:
                if letter == letters[letter1]:
                    if two:
                        if two[-1] == letters[letter2]:
                            two.append(letter)
                        else:
                            two = []
                            break
                    else:
                        two.append(letter)
                elif letter == letters[letter2]:
                    if two:
                        if two[-1] == letters[letter1]:
                            two.append(letter)
                        else:
                            two = []
                            break
                    else:
                        two.append(letter)
            lens.append(len(two))
    return max(lens)

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

def funnyString(s):
    c = s[::-1] 
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(c[i]) - ord(c[i - 1])):
            return "Not Funny"
    return "Funny"
    
def gridChallenge(grid):
    for i in range(0,len(grid)):
        grid[i]=''.join(sorted(grid[i]))
    
    for col in range(0,len(grid[0])):
        anch=-999
        for row in range(0,len(grid)):
            if anch> ord(grid[row][col]) :
                return "NO"
            anch=ord(grid[row][col])
    
    return "YES"