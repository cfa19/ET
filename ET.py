import openai
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if client.api_key is None:
    raise ValueError("The API key was not found")

def evaluate(ticket, reply):
    prompt = f"""
    Evaluate the following response:
    
    Ticket: "{ticket}"
    Reply: "{reply}"
    
    For the reply, evaluate it along two aspects:
    1. **Content**: How relevant, correct, and complete is the reply? Rate it from 1 to 5.
    2. **Format**: How clear, structured, and grammatically correct is the reply? Rate it from 1 to 5.
    
    Provide the scores for both aspects and give a brief explanation for each score.
    The response should be in the following format:
    content_score: <score>
    content_explanation: <brief explanation>
    format_score: <score>
    format_explanation: <brief explanation>
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.5
        )
        
        output = response.choices[0].message.content.strip().split("\n")
        
        content_score = int(output[0].split(":")[1].strip())
        content_explanation = output[1].split(":")[1].strip()
        format_score = int(output[2].split(":")[1].strip())
        format_explanation = output[3].split(":")[1].strip()
        
        return content_score, content_explanation, format_score, format_explanation
    
    except openai.OpenAIError as err:
        print(f"There was an error with the API: {err}")
        return None, None, None, None
    except Exception as e:
        print(f"An unexpected error occurred: {err}")
        return None, None, None, None

tickets_df = pd.read_csv(r"C:\Users\cfa08\OneDrive\Desktop\Examen\tickets.csv")
# tickets_df = pd.read_csv("C:\\Users\\cfa08\\OneDrive\\Desktop\\Examen\\tickets.csv") #2nd option


tickets_df['content_score'], tickets_df['content_explanation'], tickets_df['format_score'], tickets_df['format_explanation'] = zip(*tickets_df.apply(
    lambda row: evaluate(row['ticket'], row['reply']), axis=1))

tickets_df.to_csv('tickets_evaluated.csv', index=False)
print("Evaluation complete")