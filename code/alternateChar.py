def alternatingCharacters(s):
    d=0
    sl=list(s)
    for i in range(0, len(sl)-1):
        if sl[i]==sl[i+1]:
            d+=1
    return d