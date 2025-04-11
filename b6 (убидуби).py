def ubbidubbi(word):
    output = []
    for letter in word:
       if letter in 'aeyuio':
        output.append(f'ub{letter}')
       else:
            output.append(letter)
    return "".join(output)


print(ubbidubbi("meow"))
