from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score
from utilities import load_small_dataset
import time
from sklearn.model_selection import cross_val_score


def main():
    """Start Timer"""
    start_time = time.time()
    print("Starting time...")

    # Load data
    df = load_small_dataset()

    # Split data
    x = df['text']
    y = df['sentiment']

    # Create a pipeline with a vectorizer and a classifier
    model = make_pipeline(
        CountVectorizer(),
        MultinomialNB()
    )

    # Perform cross-validation
    cv_scores = cross_val_score(model, x, y, cv=5, scoring='accuracy')
    print("Cross-Validation Scores:", cv_scores)
    print("Mean Accuracy:", cv_scores.mean())
    print("Standard Deviation of Accuracy:", cv_scores.std())

    # Train the model on the full dataset and evaluate
    x_test, x_train, y_test, y_train = train_test_split(x, y, test_size=0.2, random_state=42)
    model.fit(x_train, y_train)

    # Predict on the test set
    y_pred = model.predict(x_test)

    # Evaluate the model
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print("Classification Report:\n", classification_report(y_test, y_pred))

    """End Timer"""
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time:.2f} seconds")


if __name__ == '__main__':
    main()
