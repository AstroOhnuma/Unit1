#Astro Ohnuma
#9/7/17
#stringanalysis.py - taking a sentence and reports how many words and characters the senteance has. Should also be able to search for a specific character and word and report how many times each occurs
sentence = (input('Enter a sentence: '))
character = (input('Enter a character to search for: '))
word = (input('Enter a word to search for: '))
print('Your sentence has',sentence.count(' ')+1,'words and',len(sentence),'characters and',len(sentence)-sentence.count(' '),'letters')
print('Your sentence has',sentence.count(word),'of the word',word)
print('Your sentence has',sentence.count(character),'of the character',character)

