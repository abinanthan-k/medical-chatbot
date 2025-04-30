from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os

load_dotenv()

def download_huggingface_embeddings():
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings

def load_models():
    embeddings = download_huggingface_embeddings()
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index_name = "medical-diagnosis-index"
    print("Searching docs")
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )
    print("Retriver building...")
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})
    print("Loading chat google")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=os.getenv("GOOGLE_API_KEY"))
    return llm, retriever
