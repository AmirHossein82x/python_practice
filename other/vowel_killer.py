def vowel_killer(string):

    vowela_list = ['a', 'i', 'u', 'o', 'e']
    result = []

    for letter in string:
        if letter not in vowela_list:
            result.append(letter)

    print(''.join(result))

vowel_killer('hi my name is amir hossein')


