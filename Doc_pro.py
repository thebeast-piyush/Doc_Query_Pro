# Import required libraries
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS  # Updated import
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI  # Updated import
from langchain_community.callbacks.manager import get_openai_callback  # Updated import

# Load environment variables from .env file
load_dotenv()

# Function to process text and create a knowledge base using FAISS
def process_text(text):
    # Split the text into chunks using Langchain's CharacterTextSplitter
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Convert the chunks of text into embeddings to form a knowledge base
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    
    return knowledge_base

# Main function to run the Streamlit app
def main():
    # Title of the app
    st.title("OpenAI PDF 💬")
    
    # Upload PDF file
    pdf = st.file_uploader('Upload your PDF Document', type='pdf')
    
    # Check if a PDF file has been uploaded
    if pdf is not None:
        # Create a PdfReader object to extract text from the PDF
        pdf_reader = PdfReader(pdf)
        text = ""
        
        # Loop through all the pages of the PDF and extract text
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Create the knowledge base from the extracted text
        knowledge_base = process_text(text)
        
        # Text input for the user's query
        query = st.text_input('Ask a question to the PDF')

        # If the user has entered a query
        if query:
            # Perform a similarity search in the knowledge base
            docs = knowledge_base.similarity_search(query)
            
            # Use OpenAI LLM for the response
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type='stuff')
            
            # Callback to get the cost of the OpenAI API usage
            with get_openai_callback() as cost:
                # Run the QA chain with the input documents and query
                response = chain.run(input_documents=docs, question=query)
                print(cost)  # Print the cost information
            
            # Display the response in the Streamlit app
            st.write(response)

# Run the Streamlit app
if __name__ == "__main__":
    main()
