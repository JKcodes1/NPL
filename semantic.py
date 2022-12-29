# Imports spacy and loads medium module
import spacy
nlp = spacy.load('en_core_web_md')

# This tokenizes string and prints similarities between words
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("\n")

# This prints similarity between chosen words
print("other type of similarity check")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

# Below declares sentence to compare and list of other sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# This compares sentence to the list of sentences and prints similarity
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
print("\n")

# This tokenizes string and prins similarity between all words
tokens = nlp('table chair dog flower ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


"""
Banana and apple have more similarity to each other 
than monkey and cat have. Banana and monkey have less similarity than 
monkey and cat or banana to apple. 
Cat and apple have only one word over 0.4 similarity,
Whilst monkey and banana have two 
"""

"""
Own example: Table, chair, flower, dog.
Table and flower have most similarity 0.38 
I suspect this is because you would put flowers on the table, 
next one is table and chair as they are both furniture. 
Thre isn't much similarity between other words.
"""

"""
When running the example file with small model en_core_web_sm 
I received error message UserWarning: [W007].
This message says it cannot be used for similarity 
as it doesn't contain word vectors and suggests using bigger model.
"""
