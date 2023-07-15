def count_vowel(sentence):
    vowel = 'aiueoAIUEO'
    number_of_vowels = 0
    for letter in sentence:
        if letter in vowel:
            number_of_vowels += 1
            
    return number_of_vowels

sentence = input("Masukkan kata atau kalimat: ")
number_of_vowels  = count_vowel(sentence)
print(f"Jumlah Huruf Vokal = {number_of_vowels} huruf")
