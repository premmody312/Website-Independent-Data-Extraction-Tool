# Website-Independent-Data-Extraction-Tool
Website Independent Data Extraction is used to extract structured or unstructured data from any website


## Dependencies:

urllib	nltk	bs4	requests	

## Installing dependencies:

> pip install requests bs4 urllib nltk

## Screenshots:
![alt text](https://github.com/premmody312/Website-Independent-Data-Extraction-Tool/blob/master/Screenshots/Capture1.PNG)
___
![alt text](https://github.com/premmody312/Website-Independent-Data-Extraction-Tool/blob/master/Screenshots/Capture2.PNG)
___
![alt text](https://github.com/premmody312/Website-Independent-Data-Extraction-Tool/blob/master/Screenshots/Capture3.PNG)
___
![alt text](https://github.com/premmody312/Website-Independent-Data-Extraction-Tool/blob/master/Screenshots/Capture4.PNG)
___
![alt text](https://github.com/premmody312/Website-Independent-Data-Extraction-Tool/blob/master/Screenshots/Capture5.PNG)
___
![alt text](https://github.com/premmody312/Website-Independent-Data-Extraction-Tool/blob/master/Screenshots/Capture6.PNG)
___


## Algorithm:

### Text to Features (Feature Engineering on text data)

Part of speech tagging – Apart from the grammar relations, every word in a sentence is also associated with a part of speech (pos) tag (nouns, verbs, adjectives, adverbs etc). The pos tags defines the usage and function of a word in the sentence. H ere is a list of all possible pos-tags defined by Pennsylvania university. Following code using NLTK performs pos tagging annotation on input text. (it provides several implementations, the default one is perceptron tagger)


### Part of Speech tagging is used for many important purposes in NLP:

### A.Word sense disambiguation: 
Some language words have multiple meanings according to their usage. For example, in the two sentences below:
I. “Please book my flight for Delhi”
II. “I am going to read this book in the flight”
“Book” is used with different context, however the part of speech tag for both of the cases are different. In sentence I, the word “book” is used as v erb, while in II it is used as no un. (Lesk Algorithm is also us ed for similar purposes)

### B.Improving word-based features: 
A learning model could learn different contexts of a word when used word as the features, however if the part of speech tag is linked with them, the context is preserved, thus making strong features. For example:
Sentence -“book my flight, I will read this book”
Tokens – (“book”, 2), (“my”, 1), (“flight”, 1), (“I”, 1), (“will”, 1), (“read”, 1), (“this”, 1)
Tokens with POS – (“book_VB”, 1), (“my_PRP$”, 1), (“flight_NN”, 1), (“I_PRP”, 1), (“will_MD”, 1), (“read_VB”, 1), (“this_DT”, 1), (“book_NN”, 1)

### C. Normalization and Lemmatization:
POS tags are the basis of lemmatization process for converting a word to its base form (lemma).

### D. Efficient stopword removal : 
POS tags are also useful in efficient removal of stopwords.
For example, there are some tags which always define the low frequency / less important words of a language. For example: (IN – “within”, “upon”, “except”), (CD – “one”,”two”, “hundred”), (MD – “may”, “must” etc)

## Conclusion:
Thus we have extarcted data from any website url that is specified
