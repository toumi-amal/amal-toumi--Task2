# amal-toumi--Task2
# Python FAQ Retrieval System

This project is a basic FAQ retrieval system that utilizes a pre-trained machine learning model to search for the most relevant answer to a given question. The model uses a `sentence-transformers` model to calculate sentence embeddings and compares the embeddings to find the most similar FAQ.

## Instructions for Setting Up and Running the Code

1. **Clone the Repository**

   First, clone this repository to your local machine using the following command:

   
      git clone https://github.com/your-username/faq-retrieval.git
   
      cd faq-retrieval
3. **Install Dependencies**

Install the required dependencies from the requirements.txt file using pip:
  pip install -r requirements.txt
This will install all the necessary packages, such as streamlit, sentence-transformers, and others that are required to run the app.

3. **Run the Streamlit App**

Once all dependencies are installed, you can run the Streamlit app with the following command:

streamlit run app.py
This will launch the app in your default web browser.

After the app is running, you can type a question into the input field. The app will retrieve the most similar FAQ from the dataset and display the corresponding answer.

**Assumptions or Challenges Faced**
Model Selection: We used the sentence-transformers pre-trained models for generating sentence embeddings. Choosing the right model for the task was crucial to ensure good performance in retrieving relevant answers. We selected paraphrase-mpnet-base-v2 for its efficiency and speed in production.


