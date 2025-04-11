def sl(s):
    output = []
    for word in s.split():
        if word[0].lower() in "aeuio":
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

print(sl("Its a test"))
