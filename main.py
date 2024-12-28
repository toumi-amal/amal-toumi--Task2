from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
import pandas as pd

data = pd.read_csv("unique_questions.csv", encoding="ISO-8859-1")

def find_similar_question(example_question):
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-mpnet-base-v2")
    faq_questions = data["Questions"].tolist()
    faq_embeddings = model.embed_documents(faq_questions)
    
    # Encode the example question
    example_embedding = model.embed_documents([example_question])
    
    # Calculate cosine similarity between the example and all FAQ questions
    similarities = cosine_similarity(example_embedding, faq_embeddings).flatten()
    
    # Find the index of the most similar question
    most_similar_idx = similarities.argmax()
    
    # Retrieve the most similar question, its answer, and the similarity score
    most_similar_question = faq_questions[most_similar_idx]
    max_similarity_score = similarities[most_similar_idx]
    if max_similarity_score < 0.7:
        most_similar_answer = "Sorry, there is no relevant answer in the database."
    else:
        most_similar_answer = data['Answers'].iloc[most_similar_idx]

    return most_similar_question, most_similar_answer
