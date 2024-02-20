# Naive Bayes classifier to guess the topic of news articles

This Naive Bayes classfier solution predicts the topics of news articles. During training, the program reads labeled news articles from "bbc_train.csv" and preprocesses the text by converting it to lowercase and removing short words. It then calculates the probabilities of each word given a class and the probability of each class. 

The probabilities are stored in log space to mitigate numerical issues. The trained model is saved in a JSON file. During testing on "bbc_test.csv," the program classifies each article by calculating the log probability of belonging to each class and selecting the class with the highest probability. 

The accuracy of the classifier is calculated by comparing the predicted topics with the actual topics in the test data. The test and training data was given, but I have added 2 news articles from 14.11.2023 to test.

The solution results in an accuracy of 97% with the current test and training data.

## How to execute
This should work with a default python3.9 installation.

Clone the project into your folder and in the corresponding project folder executing
```
python3 naive.py
```

**This has only been tested on**\
OS: Manjaro 23.0.0 Uranos\
Kernel: x86_64 Linux 5.15.128-1-MANJARO
