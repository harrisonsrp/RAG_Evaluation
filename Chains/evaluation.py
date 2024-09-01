from langchain_core.prompts import PromptTemplate
from RAG_Evaluation.LLM.models import OpenAIModel
from langchain_core.output_parsers import StrOutputParser




def RAG_eval(question, AI_answer, Actual_answer, prompt):
    evaluation_prompt_template = PromptTemplate(
        input_variables=[
            "question", "AI_answer", "Actual_answer"
        ],
        template=prompt
    )
    generate_llm = OpenAIModel().generate_model()

    optimization_chain = evaluation_prompt_template | generate_llm | StrOutputParser()

    result_optimization = optimization_chain.invoke(
        {"question": question, "AI_answer": AI_answer, "Actual_answer": Actual_answer})
    return result_optimization