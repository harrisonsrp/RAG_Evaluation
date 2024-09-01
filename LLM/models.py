# from langchain_huggingface.llms import HuggingFacePipeline
# from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
import os


#
# class t5_model:
#
#     def __init__(self, model_id="google/flan-t5-base"):
#         self.model_id = model_id
#         self.tokenizer = T5Tokenizer.from_pretrained(self.model_id)
#
#     def load_model(self, max_new_tokens=1000):
#         model = T5ForConditionalGeneration.from_pretrained(self.model_id)
#         pipe = pipeline("text2text-generation", model=model, tokenizer=self.tokenizer, max_new_tokens=max_new_tokens)
#         hf = HuggingFacePipeline(pipeline=pipe)
#         return hf

class OpenAIModel:

    def __init__(self, model_name="gpt-4o-mini"):
        self.model_id = model_name

    def generate_model(self, temperature=0):
        llm = ChatOpenAI(model=self.model_id, temperature=temperature)
        return llm

    def embed_model(self, embedding_model_name="text-embedding-3-small"):
        embedding_model = OpenAIEmbeddings(model=embedding_model_name)
        return embedding_model