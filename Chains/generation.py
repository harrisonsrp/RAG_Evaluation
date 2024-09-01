# LangChain Libraries
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate


from RAG_Evaluation.prompts import *
from RAG_Evaluation.LLM.models import OpenAIModel



generate_llm = OpenAIModel().generate_model()
embedder_llm = OpenAIModel().embed_model()
vectorstore = FAISS.load_local("faiss_embed", embedder_llm, allow_dangerous_deserialization=True)

retrieval_qa_chat_prompt = (retrieval)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", retrieval_qa_chat_prompt),
        ("human", "{input}"),
    ]
)
combine_docs_chain = create_stuff_documents_chain(generate_llm, prompt)
retrival_chain = create_retrieval_chain(
    retriever=vectorstore.as_retriever(),
    combine_docs_chain=combine_docs_chain
)
