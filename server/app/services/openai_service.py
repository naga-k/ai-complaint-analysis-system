from app.extensions import openai
import re

# The prompt provided to the GPT-4 model
prompt = """You are an AI that specializes in analyzing customer complaints. You will be provided with JSON data that contains multiple customer complaints, each identified by a unique complaint ID. 
Your task is to:
1. Categorize each complaint into a main category.
2. Sub-categorize each complaint to a sub category under the corresponding main category.
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

For the above Input, you can set the category as "Credit card" and the Sub-category as "Transaction denied"

Return the output as a JSON object as:
{
    "category": "Category",
    "sub_category": "Sub-Category",
    "summary": "Summary",
    "key_issues": ["Issue 1", "Issue 2"]
}
"""

def extract_category(analysis):
    # Use regular expressions to extract the category and sub-category
    category_match = re.search(r'"category":\s*"(.+?)"', analysis)
    sub_category_match = re.search(r'"sub_category":\s*"(.+?)"', analysis)

    if category_match and sub_category_match:
        return {
            "category": category_match.group(1),
            "sub_category": sub_category_match.group(1)
        }
    else:
        return {
            "category": "N/A",
            "sub_category": "N/A"
        }

def extract_summary(analysis):
    # Use regular expressions to extract the summary
    summary_match = re.search(r'"summary":\s*"(.+?)"', analysis)
    
    if summary_match:
        return summary_match.group(1)
    else:
        return "Summary not found"

def extract_key_issues(analysis):
    # Use regular expressions to extract the key issues as a list
    key_issues_match = re.search(r'"key_issues":\s*\[(.*?)\]', analysis)
    
    if key_issues_match:
        key_issues_str = key_issues_match.group(1)
        key_issues = [issue.strip().strip('"') for issue in key_issues_str.split(',')]
        return key_issues
    else:
        return ["No key issues found"]

def analyze_text_with_gpt(text):
    try:
        # Send the complaint text to GPT with the prompt
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Analyze this complaint: {text}"}
            ]
        )
        
        analysis = response.choices[0].message.content
        print(analysis)
        
        # Call helper functions to extract required information
        category_info = extract_category(analysis)
        summary = extract_summary(analysis)
        key_issues = extract_key_issues(analysis)

        # Return the output
        return {
            "category": category_info["category"],
            "sub_category": category_info["sub_category"],
            "summary": summary,
            "key_issues": key_issues
        }
        
    except Exception as e:
        raise Exception(f"Error in processing complaint: {str(e)}")

def transcribe_audio(file_path, language="en"):
    # Open the audio file
    with open(file_path, "rb") as audio_file:
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=language,
            response_format="json"
        )

    # Extract and return the text from the response
    transcript = response.text
    return transcript.strip()

