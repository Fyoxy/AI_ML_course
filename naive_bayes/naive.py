import csv
import math
import json

total_words = {}
unique_words = set()

def preprocess_text(text):
    return [w.lower() for w in text.split() if len(w) > 3]

def train_naive_bayes(train_file):
    global total_words, unique_words

    class_counts = {}
    word_counts = {}

    with open(train_file, encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            words = preprocess_text(text)

            # updating class counts
            class_counts[topic] = class_counts.get(topic, 0) + 1

            # updating word counts for each class
            if topic not in word_counts:
                word_counts[topic] = {}
            for word in words:
                word_counts[topic][word] = word_counts[topic].get(word, 0) + 1
                unique_words.add(word)

            # updating total word counts for each class
            total_words[topic] = total_words.get(topic, 0) + len(words)

    # calculating probabilities and storing in log space
    probabilities = {}
    for topic in class_counts:
        probabilities[topic] = {}
        for word in unique_words:
            occurrences = word_counts[topic].get(word, 0)
            probabilities[topic][word] = math.log((occurrences + 1) / (total_words[topic] + len(unique_words)))

        # calculating P(c)
        probabilities[topic]['class'] = math.log(class_counts[topic] / sum(class_counts.values()))

    # saving trained model to json
    with open('naive_bayes_model.json', 'w') as model_file:
        json.dump(probabilities, model_file)

def classify_article(article, model):
    words = preprocess_text(article)
    max_prob = float('-inf')
    predicted_class = None

    for topic, topic_probs in model.items():
        # calculating log(h(c))
        log_prob = topic_probs['class'] + sum(topic_probs.get(word, math.log(1 / (total_words[topic] + len(unique_words))))
                                             for word in words)

        # updating predicted class if higher probability is found
        if log_prob > max_prob:
            max_prob = log_prob
            predicted_class = topic

    return predicted_class

def test_naive_bayes(test_file, model):
    correct_count = 0

    with open(test_file, encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            predicted_class = classify_article(text, model)
            # print(topic, predicted_class)
            if predicted_class == topic:
                correct_count += 1

    accuracy = correct_count / 102  # 102 test articles for accuracy calculation
    print(f"Accuracy: {accuracy * 102:.2f}%")

if __name__ == "__main__":
    train_naive_bayes("bbc_train.csv")

    with open('naive_bayes_model.json') as model_file:
        model = json.load(model_file)

    test_naive_bayes("bbc_test.csv", model)
