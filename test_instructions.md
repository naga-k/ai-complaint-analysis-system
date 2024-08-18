## update packages
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=4000 


## test
Test Cases
Analyze Audio Complaint:

This test case uploads a fake audio file and checks if the response contains the expected keys: category, sub_category, summary, and key_issues.
Analyze Complaint Images:

This test case uploads a fake image file and checks if the response contains the expected keys for each image: category, sub_category, summary, and key_issues.
Analyze Video Complaint:

This test case uploads a fake video file and checks if the response contains the expected keys: category, sub_category, summary, and key_issues.
Expected Results
All tests should pass with a status code of 200.
The response should contain the keys: category, sub_category, summary, and key_issues.
Troubleshooting
If any test fails, check the server logs for errors.
Ensure that the OpenAI API key is correctly set in the .env file.
Ensure that the server is running and accessible at http://0.0.0.0:4000.
These instructions should help the team set up and run the tests effectively.
flask run --host=0.0.0.0 --port=4000


Test Cases
Analyze Audio Complaint:

This test case uploads a fake audio file and checks if the response contains the expected keys: category, sub_category, summary, and key_issues.
Analyze Complaint Images:

This test case uploads a fake image file and checks if the response contains the expected keys for each image: category, sub_category, summary, and key_issues.
Analyze Video Complaint:

This test case uploads a fake video file and checks if the response contains the expected keys: category, sub_category, summary, and key_issues.
Expected Results
All tests should pass with a status code of 200.
The response should contain the keys: category, sub_category, summary, and key_issues.
Troubleshooting
If any test fails, check the server logs for errors.
Ensure that the OpenAI API key is correctly set in the .env file.
Ensure that the server is running and accessible at http://0.0.0.0:4000.
These instructions should help the team set up and run the tests effectively. ```

