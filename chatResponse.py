from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from openai import OpenAI
import config
import json
from question_to_vector import convertUserQuestionToVector

from topicModelling import getTopics


def openaiSearch(im):
    client = OpenAI(api_key=config.getOpenAIKey())
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are an AI assistant in an data Science world. You should identify educational questions. \
                 This platform receives question and provides relevant answer. \
                 Respond with a JSON object that contains only one field, 'answser'. Don't include the word, answer:, before the actual sentence "},
            {"role": "user",
             "content": f"{im}?"}
        ]
    )
    answer = response.choices[0].message.content
    return answer

def query_pipeline(embed_question, topic):
    """
    This function is used to create the pipeline query based on the embedded question and topics found

    Args:
        embed_question (_vector_): result of convertUserQuestionToVector from question_to_vector.py
        topic (_string_): result of getTopics from topicModelling.py

    Returns:
        pipeline (_list_): return the pipeline which will be used in similaritySearch to retrieve answer
    """
    pipeline = [
        {
            '$vectorSearch': {
            'index': 'vector-search-question', 
                'path': 'embed_question', 
                'filter': {
                'topic_words': topic
                }, 
                'queryVector': embed_question, 
            'numCandidates': 100, 
            'limit': 1
            }
        }, {
            '$project': {
            '_id': 0, 
            'answer':1,
            'category':1,
            'score': {
                '$meta': 'vectorSearchScore'
            }
            }
        }
        ]
    return pipeline


def similaritySearch(collection, topic, im):
    
    embed_question = convertUserQuestionToVector(im)

    pipeline = query_pipeline(embed_question, topic)
    
    result = collection.aggregate(pipeline)

    if result['score'] < 0.7:
        answer = openaiSearch(im)
        return answer
    else:
        return result['answer']

    # get



def getResponse(userquestion):
    global tfidf, answers, X_tfidf

    topics = getTopics(userquestion)
    print(topics)
    collection = config.connect_mongoDB()
    similaritySearch(collection,topics,userquestion)




    # Classify which model this belongs to
    # Pass the question to question_to_vector
    # Pass the question and vector to similarity search
    answer = ""
    return ""






