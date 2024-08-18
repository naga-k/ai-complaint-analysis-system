from app.extensions import openai_client

def analyze_text_with_gpt(text):
    try:
        response = openai_client.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that analyzes customer complaints. Categorize the complaint, summarize it, and extract key issues."},
                {"role": "user", "content": f"Analyze this complaint: {text}"}
            ]
        )
        
        analysis = response.choices[0].message['content']
        
        # Implement logic to structure the GPT-4 output
        return {
            "category": "Category placeholder",
            "summary": "Summary placeholder",
            "key_issues": ["Issue 1", "Issue 2"]
        }
    except Exception as e:
        raise Exception(f"Error in processing complaint: {str(e)}")