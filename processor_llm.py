from dotenv import load_dotenv
from groq import Groq
import re
load_dotenv()

groq=Groq()

def classify_with_llm(log_msg):
    prompt=f''' Classify the log message into one of these categoies: 
    (1) Woorkflow Error, (2) Deprecation Warning.
    If you can't figure out a category, return "Unclassified".
    Put the category inside <category> </category> tags. 
    Log message: {log_msg}
    '''
    chat_completion=groq.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )
    content=chat_completion.choices[0].message.content
    match=re.search(r'<category>(.*)<\/category>',content,flags=re.DOTALL)
    category="Unclassified"
    if match:
        category=match.group(1)
    return category

if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))