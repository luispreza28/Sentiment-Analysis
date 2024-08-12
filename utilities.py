from datasets import load_dataset
import pandas as pd


"""Download additional data for nltk"""
# nltk.download('all') ONLY RUN ONCE THEN COMMENT IT OUT


def load_small_dataset():
    # Load a small subset of the IMDb dataset
    dataset = load_dataset('imdb')

    print(dataset)

    # Convert to pandas DataFrame
    df_train = pd.DataFrame({
        'text': dataset['train']['text'],
        'sentiment': dataset['train']['label']
    })

    df_test = pd.DataFrame({
        'text': dataset['test']['text'],
        'sentiment': dataset['test']['label']
    })

    df = pd.concat([df_train, df_test], ignore_index=True)

    return df
