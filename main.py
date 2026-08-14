import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: GROQ_API_KEY was not found.")
    print("Please check your .env file.")
    exit()

client = Groq(api_key=api_key)


while True:

    print("================================")
    print("       AI INTERVIEW AGENT")
    print("================================")

    role = input("\nEnter the job role: ").strip()

    if not role:
        print("ERROR: Job role cannot be empty.")
        continue

    print("\nYou selected:", role)

    # Generate 5 questions
    print("\nGenerating questions...")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional entry-level interviewer. "
                    "Generate exactly 5 short, simple and beginner-friendly "
                    "theory questions for the given job role. "
                    "Questions must be suitable for a fresher. "
                    "Do not ask coding questions. "
                    "Do not ask practical programming tasks. "
                    "Do not ask advanced or lengthy questions. "
                    "Use different important topics related to the role. "
                    "Return only 5 questions, one per line."
                )
            },
            {
                "role": "user",
                "content": f"Generate 5 theory questions for the role: {role}"
            }
        ]
    )

    questions = []

    for line in response.choices[0].message.content.splitlines():
        line = line.strip()

        if line:
            if "." in line[:4]:
                line = line.split(".", 1)[1].strip()

            questions.append(line)

    questions = questions[:5]

    if len(questions) < 5:
        print("ERROR: Could not generate 5 questions.")
        continue


    # Interview
    print("\n================================")
    print("       INTERVIEW STARTED")
    print("================================")

    answers = []

    for i, question in enumerate(questions):

        print(f"\n{i + 1}. {question}")

        answer = input("Your answer: ").strip()

        if not answer:
            answer = "[No answer provided]"

        answers.append(answer)

        print("Answer received!")


    # Prepare interview data
    interview_data = ""

    for i in range(5):
        interview_data += (
            f"\nQuestion {i + 1}: {questions[i]}\n"
            f"Candidate Answer: {answers[i]}\n"
        )


    # Evaluation
    print("\nEvaluating interview...")

    evaluation = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a fair and professional interviewer. "

                    "Evaluate exactly five theory interview answers. "

                    "Each question is worth exactly 20 marks. "
                    "The total score is exactly 100. "

                    "Give credit for short but correct beginner-level answers. "
                    "Give partial marks for partially correct answers. "

                    "Do not invent mistakes or missing information. "
                    "Evaluate only what the candidate actually answered. "

                    "Do not assume education, experience or background. "

                    "Do not mention coding or practical assessments. "

                    "The Theory Score MUST equal the sum of all five "
                    "question scores. "

                    "The Overall Score MUST be exactly the same as "
                    "the Theory Score. "

                    "The recommendation MUST be exactly one of: "
                    "Strong candidate, Good candidate, "
                    "Needs improvement, Requires further preparation."
                )
            },
            {
                "role": "user",
                "content": f"""
Evaluate this interview.

ROLE:
{role}

QUESTIONS AND ANSWERS:
{interview_data}

SCORING:

Question 1 = 20 marks
Question 2 = 20 marks
Question 3 = 20 marks
Question 4 = 20 marks
Question 5 = 20 marks

Total = 100 marks.

IMPORTANT:

- Score every question separately.
- Each score must be between 0 and 20.
- Add all five scores correctly.
- Theory Score must equal the sum of the five scores.
- Overall Score must equal Theory Score.
- Do not invent mistakes.
- Do not penalize a short answer if it is correct.
- Give partial marks when appropriate.
- Do not repeat the same weakness.
- Do not mention coding.
- Do not mention practical assessment.

Return EXACTLY this structure:

FINAL INTERVIEW REPORT

Role: {role}

INTERVIEW TRANSCRIPT

Question 1:
{questions[0]}

Candidate Answer:
{answers[0]}

Score: X/20


Question 2:
{questions[1]}

Candidate Answer:
{answers[1]}

Score: X/20


Question 3:
{questions[2]}

Candidate Answer:
{answers[2]}

Score: X/20


Question 4:
{questions[3]}

Candidate Answer:
{answers[3]}

Score: X/20


Question 5:
{questions[4]}

Candidate Answer:
{answers[4]}

Score: X/20


SCORING SUMMARY

Theory Score: X/100
Overall Score: X/100

Strengths:
- ...
- ...
- ...

Weaknesses:
- ...
- ...
- ...

Final Feedback:
...

Recommendation:
...

The recommendation MUST be exactly one of:

Strong candidate
Good candidate
Needs improvement
Requires further preparation
"""
            }
        ]
    )


    # Display report
    final_report = evaluation.choices[0].message.content

    print("\n================================")
    print("FINAL INTERVIEW REPORT")
    print("================================")

    print(final_report)


    # Save report
    report_number = 1

    while os.path.exists(
        f"Interview_Report_{report_number}.txt"
    ):
        report_number += 1

    report_name = (
        f"Interview_Report_{report_number}.txt"
    )

    with open(
        report_name,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(final_report)


    print("\n================================")
    print("Interview report saved!")
    print("Report:", report_name)
    print("================================")


    # Another interview
    again = input(
        "\nStart another interview? (yes/no): "
    ).strip().lower()

    if again != "yes":
        print("\nInterview Agent closed.")
        break