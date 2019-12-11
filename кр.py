def retrieve(filename, morph=none, num=none):
    output=[]
    with open(frec_dict.csv, encoding='utf-8') as file:
        for line in file:
            word, morph, num = line.split('|')
            if morph is not none and morph = сущ or morph = гл or morph = прл:
                continue
            if num = none or num = ед or num = мн:
                continue
            output.append (word, morph, num)
    return output





def delete_consonant(my_str, how='all'):
    vowel_letters = 'аеёиоуыэюя'
    num = 0
    result_string = ''
    if how == 'vow':
        if letter in vowel_letters:
            result_string+=letter
            num+=1
    elif how=='all':
        result_string+=letter
        num+=1
    return (result_string, num)
