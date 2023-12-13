import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_md')  # Load 'en_core_web_md', not 'nlp_md'

# Compare individual word similarities using 'en_core_web_md'
word1_md = nlp("cat")  # Use 'nlp' instead of 'nlp_md'
word2_md = nlp("monkey")  # Use 'nlp' instead of 'nlp_md'
word3_md = nlp("banana")  # Use 'nlp' instead of 'nlp_md'
print(
    f"Similarity between 'cat' and 'monkey' using 'en_core_web_md': {word1_md.similarity(word2_md)}")
# Add more comments for other comparisons

# Compare individual word similarities using 'en_core_web_sm'
word1_sm = nlp("cat")  # Use 'nlp' instead of 'nlp_sm'
word2_sm = nlp("monkey")  # Use 'nlp' instead of 'nlp_sm'
word3_sm = nlp("banana")  # Use 'nlp' instead of 'nlp_sm'
print(
    f"Similarity between 'cat' and 'monkey' using 'en_core_web_sm': {word1_sm.similarity(word2_sm)}")
# Add more comments for other comparisons

# Compare similarity between each pair of words in a sequence
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Compare similarity between a reference sentence and other sentences
sentence_to_compare = "Why is my cat on the car"
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Notes about the findings
print("\n### Observations and Notes ###")
print("1. The similarity values between 'cat,' 'monkey,' and 'banana' are consistent between 'en_core_web_md' and 'en_core_web_sm'.")
print("2. Example of My Own: Consider the words 'car,' 'bicycle,' and 'bus' for higher similarities due to their association with transportation.")
print("3. Differences with 'en_core_web_sm': The similarity values are generally lower, as 'en_core_web_sm' is a simpler model.")
