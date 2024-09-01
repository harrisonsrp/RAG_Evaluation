retrieval = """
        Use the given context to answer the question.
        If you don't know the answer, say you don't know.
        Context: {context}
        remember to keep answer just 250 character
        """

evaluation_role_prompting = """
            You are an AI expert system meant to evaluate the performance of a student in prompt engineering course.
            for given question:{question} the student will provide answer:{AI_answer}.
            your job is to figure out if the accuracy of the answer.
            you have real answers:{Actual_answer} for all the questions you just need to find out if the student got it right.
    
            Remember:
            1. Provide your evaluation as percentage (0-100%) indicating how much student response is close
            to actual response
            2. Give a summary of why you are giving this feedback and what are missing
            3. If your evaluation percentage was less than 85% consider the response as False, otherwise is true
            
            Response Format (in json):
            Accuracy: [Evaluation percentage]
            Binary evaluation: [True/False]
            Feedback: [summary of feedback]
            """

evaluation_chain_of_thought_prompting = """
            Task Breakdown:
            Question: {question}
            Student's Answer: {AI_answer}
            Actual Answer: {Actual_answer}
            
            Evaluation Process:
            Comparison: Begin by comparing the student's answer to the actual answer. Consider the key components, completeness, and correctness of the provided response.
            Evaluation Percentage: Determine how close the student's response is to the actual answer, assigning a percentage (0-100%) based on the degree of alignment.
            Analysis: Reflect on why you gave this percentage. Identify any key points the student missed, misunderstood, or correctly addressed.
            Binary Decision: If the evaluation percentage is less than 85%, mark the response as False; otherwise, mark it as True.
            
            Response Format (in json):
            Accuracy: [Evaluation percentage]
            Binary Evaluation: [True/False]
            Feedback: [Summary of feedback]
            
            """


evaluation_ReACT_prompting = """
            You are an AI expert system designed to evaluate a student's performance in a prompt engineering course.
            
            Task:
            Question: {question}
            Student's Answer: {AI_answer}
            Actual Answer: {Actual_answer}
            
            Thought Process (Reasoning):
            Observation: Review the question, the student's answer, and the actual answer.
            Analysis: Compare the student's answer with the actual answer, identifying areas of alignment and discrepancy. Evaluate the correctness, completeness, and relevance of the student's response.
            Evaluation: Assign a percentage (0-100%) that reflects how close the student's answer is to the actual answer.
            
            Action:
            Binary Evaluation: Based on the percentage, determine if the answer is correct (True) or incorrect (False). If the percentage is less than 85%, consider the response as False; otherwise, consider it True.
            Feedback: Summarize the key points of the evaluation, explaining why the student's answer received the given percentage and what was missing or incorrect.
            
            Response Format (in json):
            Accuracy: [Evaluation percentage]
            Binary Evaluation: [True/False]
            Feedback: [Summary of feedback]
            """
evaluation_self_consistency_prompting = """
            You are an AI expert system designed to evaluate a student's performance in a prompt engineering course.
            
            Task:
            Question: {question}
            Student's Answer: {AI_answer}
            Actual Answer: {Actual_answer}
            
            
            Evaluation Process:
            Initial Evaluation:
            Compare the student's answer to the actual answer.
            Assign an initial percentage (0-100%) based on the accuracy, completeness, and relevance of the student's response.
            
            Self-Consistency Check:
            Reevaluate the student's answer by considering alternative interpretations or variations of the correct answer.
            Reflect on whether the initial evaluation remains consistent or if adjustments are needed.
            
            Final Evaluation:
            Determine the final percentage based on the consistency of your evaluations.
            Decide whether the student's answer is correct (True) or incorrect (False). If the final percentage is less than 85%, consider the response as False; otherwise, consider it True.
            
            Response Format (in json):
            Accuracy: [Final evaluation percentage]
            Binary Evaluation: [True/False]
            Feedback: [Summary of feedback, including any shifts in evaluation due to the self-consistency check]
            """
