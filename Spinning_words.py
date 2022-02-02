import random

def spin_words(sentence):
    #nacitam si do listu slova z retazca
    words = sentence.split(' ')
     #vyberiem nahodne jedno az vsetky slova a tieto slova si pretocim
    order = random.randint(0, len(words))
    print(len(words))
    print(random.randint(0,9))
    return words


def reverse_words(s):
    words = s.split(' ')
    reverse = words[::-1]
    reverse_list = ' '.join(reverse)
    return reverse_list


vysledok = spin_words('ahoj velky svet')
