# :zap:  PersianNER :zap:

## :bookmark: introduction


Named Entity Recognition (NER) is a crucial task in text mining that involves classifying entities into different types such as person, location, organization, etc. NER can play a pivotal role as a pre-processing stage for various tasks, including question answering.
Traditionally, NER systems have been divided into two main categories: classic approach and statistical approach. In the classic approach, handcrafted rules are constructed to perform the NER task. However, more recently, there has been a growing interest in statistical approaches, driven by the advancements in deep neural networks.

[![-----------------------------------------------------]( 
https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)](https://github.com/ImMohammadHosseini/incremental-learning?tab=repositories)

## :bookmark: Problem
Given the wide variety of deep learning algorithms, choosing an appropriate algorithm for a problem is a significant part of the research in this area. Therefore, a part of the research in this field focuses on comparing different algorithms to identify the one that performs better in solving a problem. Since natural language processing is one of the important areas of artificial intelligence and deep learning, this project aims to compare various deep learning algorithms and RNN networks on a Persian dataset. The goal is to implement multiple models for an NER (Named Entity Recognition) project and determine the best architecture based on the accuracy of the designed models

[![-----------------------------------------------------]( 
https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)](https://github.com/ImMohammadHosseini/incremental-learning?tab=repositories)

## :bookmark: Experimental Settings


### :bookmark: Datasets
The dataset includes 250,015 tokens and 7,682 Persian sentences in total. It is available in 3 folds to be used in turn as training and test sets. Each file contains one token, along with its manually annotated named-entity tag, per line. Each sentence is separated with a newline. The NER tags are in IOB format.

According to the instructions provided to the annotators, NEs are categorized into six classes: person, organization (such as banks, ministries, embassies, teams, nationalities, networks and publishers), location (such as cities, villages, rivers, seas, gulfs, deserts and mountains), facility (such as schools, universities, research centers, airports, railways, bridges, roads, harbors, stations, hospitals, parks, zoos and cinemas), product (such as books, newspapers, TV shows, movies, airplanes, ships, cars, theories, laws, agreements and religions), and event (such as wars, earthquakes, national holidays, festivals and conferences); other are the remaining tokens.

### :bookmark: tokenization
tokenization step is a common stage in working with any type of textual data. In this step, human-readable text data is transformed into a set of numerical values, making it usable by machines. Without going through this stage, it is not possible to work with textual data in machine-based models effectively. There are ready-made libraries available to perform this step, but they were not utilized here. 

The process followed in this project is as follows: First, individual unique words in the textual data are identified (with repeated words removed). Then, each word is assigned a numerical value in a dictionary data structure. From this point on, the corresponding numerical value in the dictionary is used instead of the word itself in the computer. The same process is also applied to 13 groups of text labels. 

Afterwards, these assigned numbers to words are substituted in sentences, creating the variable 'x', which is used in various stages of the project. Similarly, the labels create the variable 'y'.

### :bookmark: pad sequence 

In neural network models, all input sequences need to be of the same length because input neurons are defined as a single number. Therefore, the length of all sentences in the text data should be equal. Sometimes, the input word is also important in the network, so in this case, the same length should be considered for the words as well.
The best approach to standardize the length of sentences is to experiment and plot a simple graph to approximate the length of the longest sentence. Then, using the function "sequence_pad", the length of all sentences is increased by adding zeros to match the length of the longest sentence. It is important to note that adding zeros to the sentences after converting words to numbers does not affect the learning process of the network because zero was initially considered for this purpose in the dictionary. This step needs to be implemented for both sentences and labels, which are both provided as lists based on the sentence.

[![-----------------------------------------------------]( 
https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)](https://github.com/ImMohammadHosseini/incremental-learning?tab=repositories)


### Citations

1- Hanieh Poostchi, Ehsan Zare Borzeshi, Mohammad Abdous, and Massimo Piccardi, "PersoNER: Persian Named-Entity Recognition," The 26th International Conference on Computational Linguistics (COLING 2016), pages 3381–3389, Osaka, Japan, 2016.

2- Hanieh Poostchi, Ehsan Zare Borzeshi, and Massimo Piccardi, "BiLSTM-CRF for Persian Named-Entity Recognition; ArmanPersoNERCorpus: the First Entity-Annotated Persian Dataset," The 11th Edition of the Language Resources and Evaluation Conference (LREC), Miyazaki, Japan, 7-12 May 2018, ISLRN 399-379-640-828-6, ISLRN 921-509-141-609-6.

