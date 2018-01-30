# Technical Questions

##############################
# Return counter of words in a sentence/Return most occuring word
##############################

# Version 1, Standard Control Flow
#%%
sentence = 'It was the best of times it was the worst of times it was also a happy time'
sentence_list = sentence.split() # Returns above sentence as a list now
wordfreq = []
for word in sentence_list:
  wordfreq.append(sentence_list.count(word.lower())) # .lower() method added so 'It' changes to 'it' when counted
list_comprehension = [[item1,item2] for item1,item2 in zip(sentence_list,wordfreq)]
print(list_comprehension) # Prints all words and frequencies
most_word = list(max(zip(wordfreq,sentence_list))) # Prints max word frequency as a list
print(most_word[::-1]) # Reverses order of most_word

#%%
# Version 2, Pythonic way using collections.Counter on a sentence
import collections
sentence = 'It was the best of times it was the worst of times it was also a happy time'
sentence_list = sentence.split()
most = collections.Counter(sentence_list).most_common()[0] # Counter Returns Dict, but .most_common() returns a list you can index
print(most) # Returns it as a tuple
print(list(most))
