# Semantic Similarity Analysis with spaCy

## Introduction
This script uses spaCy, a natural language processing library, to analyze semantic similarities between words and sentences.

## Code
The code in `semantic.py` does the following:
1. Loads the spaCy model ('en_core_web_md') to enable word vector comparisons.
2. Compares similarities between individual words ('cat', 'monkey', 'banana').
3. Compares similarities between each pair of words in a sequence.
4. Compares similarities between a reference sentence and other sentences.

## Findings and Observations
### Word Similarities
- The similarity between 'cat' and 'monkey': 0.5929930210113525
- The similarity between 'banana' and 'monkey': 0.4041501581668854
- The similarity between 'banana' and 'cat': 0.2235882580280304

### Sequence Similarities
- 'cat' and 'apple': 0.2036806046962738
- 'cat' and 'monkey': 0.5929930210113525
- 'cat' and 'banana': 0.2235882580280304
- ...

### Sentence Similarities
- "Where did my dog go" - Similarity: 0.630065230699739
- "Hello, there is my car" - Similarity: 0.8033180111627156
- "I've lost my car in my car" - Similarity: 0.6787541571030323
- ...

## Interesting Findings
- Word vector-based similarities reflect semantic relationships. For example, 'cat' and 'monkey' have a higher similarity than 'cat' and 'banana.'
- Sentence similarities capture semantic meaning, with higher similarities for sentences with similar topics or contexts.

## Example of My Own
Consider the words 'car,' 'bus,' and 'bicycle.' These words likely have higher similarities among themselves due to their common association with transportation.

Feel free to explore and modify the code for your specific use case!
