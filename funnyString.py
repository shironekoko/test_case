def funnyString(s):
    # Write your code here
    c=''.join(reversed(list(s)))
    flag=True
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!= abs(ord(c[i])-ord(c[i-1])):
            flag=False
            
    if flag is True:
        return 'Funny'
    else:
        return 'Not Funny'