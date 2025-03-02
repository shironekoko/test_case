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