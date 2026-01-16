import os
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from bg_stopwords import BULGARIAN_STOPWORDS

SUMMARY_LENGTHS = {
    "short": 2,
    "medium": 4,
    "long": 6
}

# the folder where the documents, which are going to be summarized, are placed
DATA_FOLDER = "data"


def summarize(text, n_sentences):
    sentences = nltk.sent_tokenize(text)
    n_sentences = min(n_sentences, len(sentences))

    vectorizer = TfidfVectorizer(stop_words=BULGARIAN_STOPWORDS)
    tfidf_matrix = vectorizer.fit_transform(sentences)

    scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    top_indices = np.argsort(scores)[-n_sentences:]
    top_indices = sorted(top_indices)

    return " ".join([sentences[i] for i in top_indices])

# lists all documents in the directory where summarizations are going to be made
def list_documents():
    return [f for f in os.listdir(DATA_FOLDER) if f.endswith(".txt")]


def main():
    while True:
        documents = list_documents()

        if not documents:
            print("No documents found in the data folder.")
            return

        print("\nAvailable documents:")
        for i, doc in enumerate(documents, 1):
            print(f"{i}. {doc}")

        try:
            doc_choice = int(input("\nChoose document number: ")) - 1
            filename = documents[doc_choice]
        except (ValueError, IndexError):
            print("Invalid document selection.")
            continue

        length_choice = input(
            "Choose summary length (short / medium / long): "
        ).strip().lower()

        if length_choice not in SUMMARY_LENGTHS:
            print("Invalid summary length.")
            continue

        with open(os.path.join(DATA_FOLDER, filename), "r", encoding="utf-8") as file:
            text = file.read()

        summary = summarize(text, SUMMARY_LENGTHS[length_choice])

        print("\n========== SUMMARY ==========\n")
        print(summary)
        print("\n=============================\n")

        again = input("Summarize another document? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()