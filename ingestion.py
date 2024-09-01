import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader
from LLM.models import OpenAIModel
from langchain.text_splitter import RecursiveCharacterTextSplitter

urls = [
    "https://medium.com/@fareedkhandev/prompt-engineering-complete-guide-2968776f0431",
    "https://medium.com/@researchgraph/prompt-engineering-21112dbfc789",
    "https://blog.fabrichq.ai/what-is-prompt-engineering-a-detailed-guide-with-examples-4d3cbbd53792"
]
loader = WebBaseLoader(urls)
# Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=20
)
documents = loader.load_and_split(text_splitter)

# LLM
embedder_llm = OpenAIModel().embed_model()

# Embedding the document chunks
vectorstore = FAISS.from_documents(documents, embedder_llm)
vectorstore.save_local("faiss_embed")
print("===== Ingestion Completed ===== ")