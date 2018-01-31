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


##############################
# 1) Reshape a 1D array into 2D array with 1 column; Needed for sklearn inputs
# 2) Split data into input features (X) and output variables (y)
# 3) Split into train and test set (manually)
##############################

#%%
# 1)
import numpy as np
a1 = np.array([1,2,3,4,5])
a2 = np.transpose(a1)
print(a1)
print(a1.shape)
print(a2.shape) # The Transpose of a 1D array is still a 1D array

two_dimensional_array = a1.reshape(a1.shape[0],1)
print(two_dimensional_array)
print(two_dimensional_array.shape)

#%%
# 2)
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,10,11]})
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
print('Input: {}'.format(X))
print('Output: {}'.format(y))

#%%
# 3)
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,10,11]})
print(df.head())
train = df.iloc[:3,]
test = df.iloc[3:,]
print(train)
print(test)