 AI Interview Agent

 1. What the Agent Does

I built this project as a simple AI Interview Agent that can conduct mock interviews for different job roles.

The user first enters a job role, such as Data Analyst or AI Developer. The agent then generates interview questions related to that role. The candidate answers the questions, and the AI evaluates the answers and provides scores and feedback.

The main goal of this project is to give a simple interview practice experience using AI.

 2. Features

- Generates interview questions based on the job role
- Conducts a 5-question interview
- Takes answers directly from the terminal
- Evaluates each answer using AI
- Gives a score for each question
- Calculates the overall score
- Shows strengths and weaknesses
- Gives final feedback and recommendation
- Saves the interview report as a text file
- Can be used for different job roles

 3. Technologies Used

I used the following technologies to build the project:

- Python
- Groq API
- Large Language Model (LLM)
- python-dotenv
- Git
- GitHub

The application currently runs through the command line.

 4. Installation

First, clone this repository and open the project folder in VS Code.

Then install the required Python packages:

bash
pip install -r requirements.txt

5. API Key Setup

This project uses the Groq API to generate questions and evaluate answers.

Create a file named .env in the project folder and add your own API key:

GROQ_API_KEY=your_actual_groq_api_key

I have not included my actual API key in this repository for security reasons.

The repository contains a .env.example file that shows the required format.

6. How to Run

Open the terminal in the project folder and run:

python main.py

The program will ask for the job role.

For example:

Enter the job role: Data Analyst

After entering the role, the interview will start.

The agent will ask five questions and wait for the candidate's answer after each question.


7. Example Interview

A simple example of the interview looks like this:

================================
       AI INTERVIEW AGENT
================================


Enter the job role: Data Analyst


Generating questions...


================================
       INTERVIEW STARTED
================================


1. What is the primary function of a data analyst?


Your answer: A data analyst collects, cleans, analyzes and interprets data to help organizations make better decisions.

The process continues until all five questions are completed.


8. Sample Output

After completing the interview, the agent evaluates the answers.

The final report contains the score for each question, overall score, strengths, weaknesses and final feedback.

For example:

Question 1 Score: 18/20
Question 2 Score: 17/20
Question 3 Score: 19/20
Question 4 Score: 18/20
Question 5 Score: 19/20


Overall Score: 91/100


Recommendation: Good candidate

The interview report is also saved as a text file so that it can be checked later.


9. Design Approach

I kept the design simple because the main focus of the project is the interview functionality.

The basic flow of the agent is:

User enters job role
↓
AI generates interview questions
↓
Candidate answers the questions
↓
AI evaluates the answers
↓
Scores are generated
↓
Final feedback is created
↓
Interview report is saved

Python handles the interview flow and communication with the Groq API, while the AI model is responsible for generating questions and evaluating the candidate's answers.


10. Tradeoffs

I decided to build the project as a command-line application instead of spending time creating a graphical interface.

This helped me focus more on making the interview process and AI evaluation work properly within the available development time.

I also used the same AI model for generating questions and evaluating answers. This keeps the project simple and reduces the amount of configuration required.

The scoring is AI-based, so it may not always be exactly the same as a human interviewer's evaluation. I tried to make the evaluation consider correctness, relevance, clarity and completeness of the answer.


11. Limitations

The current version runs only through the command line and does not have a web or graphical interface.

The evaluation depends on the AI model, so scores can sometimes vary depending on the answer and the generated questions.

Currently, the agent accepts typed answers and does not support voice interviews.

The project also requires an internet connection and a valid Groq API key to work.

Future Improvements

If I continue developing this project, I would like to add:

A web-based interface
Voice-based interviews
Resume-based interview questions
Different interview difficulty levels
Interview history and dashboard
More detailed candidate analysis
Questions that become harder or easier based on the candidate's performance
Author

DarshanSubramani



This version is better for you** because it explains what *you actually built* in a simple way instead of using complicated technical language.
