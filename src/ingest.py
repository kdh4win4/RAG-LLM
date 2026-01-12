import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def ingest_docs():
    # 1. 문서 로드
    loader = PyPDFLoader("./data/sample.pdf")
    documents = loader.load()
    
    # 2. 텍스트 분할 (Chunking)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    
    # 3. 벡터 DB 저장
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=docs, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )
    print("Ingestion complete!")

if __name__ == "__main__":
    ingest_docs()
