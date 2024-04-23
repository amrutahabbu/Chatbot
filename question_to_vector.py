#This file converts question inputs to vector and store in the database - MongoDB
import pickle


def convertCorpusToVector():
    return ""

def convertUserQuestionToVector(processed_question):
    """
    This function will load the tfidf_vectorizer and transform processed question to vector so it can be used for the pipeline to retrieve answer

    Args:
        processed_question (_string_): question after being processed like training data

    Returns:
        _list_: return list of numbers or arrays represent a vector of process question
    """
    
    # Load tfidf_vectorizer
    with open('model/tfidf_vectorizer.pkl', 'rb') as f:
        tfidf_vectorizer = pickle.load(f)

    print(processed_question)
    processed_question = "data science"
    # Use tfidf to vectorize processed question
    embed_question = tfidf_vectorizer.transform([processed_question]).toarray().tolist()[0]

    # return embed_question
    return embed_question