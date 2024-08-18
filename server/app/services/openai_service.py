from app.extensions import openai_client

prompt = """You are an AI that specializes in analyzing customer complaints. You will be provided with JSON data that contains multiple customer complaints, each identified by a unique complaint ID. 
Your task is to:
1. Categorize each complaint into one of the predefined main categories.
2. Sub-categorize each complaint under the corresponding main category.
3. If the data is not a complaint, return a message stating that it is not a complaint and Category should be N/A and Sub Category should be N/A as well.
4. Generate a summary of the complaint.
5. Generate Key issues from the complaint.

Example Categories:
1. Category: Credit Card
  - Sub-Categories: General Enquiry, Issue with the product, Transactions denied, Card Not Working.

2. Category: User Account
  - Sub-Categories: General Enquiry, Account access issue, Account Blocked, Remove Temporary Block.

Here is how the Input text containing customer complaints will be:

- My credit card seems to be not working when used in any stores. The transaction is not going through whatsoever. I have tried using my card in multiple stores and there is no luck. Assist me at the earliest. Thank you.

For the above Input, you can set the category as "Credit card" and the Sub-category as "Transcation denied"

Return the output as a JSON object as:
{
    "category": "Category",
    "sub_category: "Sub-Category"
    "summary": "Summary",
    "key_issues": ["Issue 1", "Issue 2"]

}
"""

def analyze_text_with_gpt(text):
    try:
        response = openai_client.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Analyze this complaint: {text}"}
            ]
        )
        
        analysis = response.choices[0].message['content']
        print(analysis)

        
        # Implement logic to structure the GPT-4 output
        return {
            "category": "Category placeholder",
            "summary": "Summary placeholder",
            "key_issues": ["Issue 1", "Issue 2"]
        }
    except Exception as e:
        raise Exception(f"Error in processing complaint: {str(e)}")

def extract_category(analysis):
    # Implement logic to extract category from the analysis
    # This is a placeholder implementation
    return "Category placeholder"

def extract_summary(analysis):
    # Implement logic to extract summary from the analysis
    # This is a placeholder implementation
    return "Summary placeholder"

def extract_key_issues(analysis):
    # Implement logic to extract key issues from the analysis
    # This is a placeholder implementation
    return ["Issue 1", "Issue 2"]

