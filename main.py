from RAG_Evaluation.test_data.load_test_set import data
from prompts import *
from RAG_Evaluation.Chains.evaluation import RAG_eval
from RAG_Evaluation.Chains.generation import retrival_chain
import textwrap


for item in data:
    question = {"input": item['question']}
    result = retrival_chain.invoke(input=question)

    AI_answer = result['answer']
    Actual_answer = item['reference_answer']

    Evaluation = RAG_eval(
        question=question,
        AI_answer=AI_answer,
        Actual_answer=Actual_answer,
        prompt=evaluation_self_consistency_prompting
    )

    print(f"AI_answer:{AI_answer}")


    print(Evaluation)
