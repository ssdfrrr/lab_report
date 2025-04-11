def l():
    word = input("Введите слово: ")
    if word[0] in "aeuio":
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]} ay'
print(l() )
