from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# For building test set
from giskard.rag import KnowledgeBase, generate_testset
# dataframe
import pandas as pd
from LLM.models import OpenAIModel

if __name__ == '__main__':
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

    df = pd.DataFrame([doc.page_content for doc in documents], columns=["text"])
    print(df.head(10))

    ## Add dataframe to giskard KnowledgeBase
    knowledge_base = KnowledgeBase(df)

    # generate a testset
    test_set = generate_testset(
        knowledge_base,
        num_questions=10,
        agent_description="A chatbot answering question about prompt engineering"
    )
    test_set.save("test-set.jsonl")