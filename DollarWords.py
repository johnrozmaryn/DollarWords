# First, open up the file of words and make a big list to work from.
# I got the list from https://github.com/dwyl/english-words
f = open("words_alpha.txt")
contents = (f.readlines())
wordlist = []
for w in contents:
    wordlist.append(w.strip())
 
# Then, make a helper dictionary so we can easily look up the value 
# of each letter  
lettervals = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    pos = alphabet.find(letter)
    lettervals[letter] = pos + 1

# Function that returns a 'value' of each word, based on the 'value'
# of each letter
def calc_value(word):
    val = 0
    for letter in word:
        val += lettervals[letter]
    return val

# Now rip through the wordlist and calculate which are Dollar Words
dollarwords = []        
for word in wordlist:
    if calc_value(word) == 100:
        dollarwords.append(word)
print('I found ' + str(len(dollarwords)) + ' Dollar Words')        
print(dollarwords)
        
