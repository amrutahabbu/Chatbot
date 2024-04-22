from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from openai import OpenAI
import config
import json

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




def similaritySearch(im,topics):

    # vectorizer = saved from input
    #tfidf = saved from input


    Y_vec = vectorizer.transform(im)
    Y_tfidf = tfidf.fit_transform(Y_vec)
    cos_sim = np.rad2deg(np.arccos(max(cosine_similarity(Y_tfidf, X_tfidf)[0])))
    if cos_sim > 60:
        answer = openaiSearch(im)
        return answer
    else:
        return answers[np.argmax(cosine_similarity(Y_tfidf, X_tfidf)[0])]

    # get



def getResponse(userquestion):
    global tfidf, answers, X_tfidf

    topics = getTopics(userquestion)
    similaritySearch(userquestion,topics)




    # Classify which model this belongs to
    # Pass the question to question_to_vector
    # Pass the question and vector to similarity search
    answer = ""
    return ""






