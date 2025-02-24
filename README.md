## APPLICATION TRACKING SYSTEM
This project is a Streamlit application designed to help users evaluate their resumes against a given job description using Google's Gemini AI model. It provides three key functionalities:

Resume Evaluation: Provides an overall assessment of how well a resume matches a job description.
Improvement Suggestions: Offers advice on improving the resume and highlighting areas for skill development.
Percentage Match: Calculates a percentage score representing the match between the resume and job description, along with a list of missing keywords.
### Project Link
https://application-tracking-system-wxrzvz5bvo8k9udfrtd2yk.streamlit.app/

### Functionality
The application takes a PDF resume and a job description as input. It then uses the Gemini AI model to analyze the text and provide insightful feedback.

### Steps:

Upload Resume: Upload your resume in PDF format.
Paste Job Description: Copy and paste the job description into the provided text area.
Select Functionality: Choose one of the three buttons:
"Tell me about the resume": Get a general evaluation of your resume's suitability for the job.
"How can I improve my skills": Receive suggestions on how to enhance your skills and make your resume more competitive.
"Percentage match": Get a numerical percentage score and a list of missing keywords.
View Results: The application will process your input and display the AI-generated response.
### Setup
To run this application locally, you will need:

Python 3.10+: Ensure you have Python 3.10 or a later version installed.
Required Libraries: Install the necessary libraries using pip:
pip install streamlit google-generativeai python-dotenv PyPDF2

Google Generative AI API Key: Obtain a Google Generative AI API key and set it as an environment variable named GOOGLE-API-KEY. You can do this by creating a .env file in the same directory as your Python script and adding the following line:
GOOGLE-API-KEY=your_api_key_here

Run the Application: Navigate to the project directory in your terminal and run:
streamlit run app.py

### Code Overview
The Python code (app.py) utilizes the following libraries:

Streamlit: For creating the user interface.
PyPDF2: For extracting text from PDF files.
google.generativeai: For interacting with the Gemini AI model.
python-dotenv: For securely managing API keys.
The core logic involves:

Extracting text from the uploaded PDF resume using PyPDF2.
Constructing a prompt for the Gemini AI model based on the selected functionality.
Sending the prompt to the Gemini AI model and receiving the response.
Displaying the response in the Streamlit application.
### Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

