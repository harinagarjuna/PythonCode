word = input("Enter a word")
loword = word.lower()
lword = len(loword)
vowels = 0
consonants = 0
for i in range(0,lword):
 if loword[i] == 'a' or loword[i] == 'e' or loword[i] == 'i' or loword[i] == 'o' or loword[i] == 'u' :
       print(loword[i],"is a VOWEL")
       vowels = vowels+1
 else :
       print(loword[i],"is a consonant")
       consonants = consonants+1

print("total vowels are",vowels,"\n","total consonants are",consonants)
