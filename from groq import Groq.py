from groq import Groq

# Initialize Groq client with your API key
client = Groq(api_key="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")

# Interview Prompt Template
base_prompt = """
Act as an interviewer for a {job_type} interview. Your job is to ask interview questions one by one related to the job type and evaluate the candidate's answers.


1. Ask questions related to the skills, experience, and problem-solving abilities relevant to the {job_type}. Ask only one question at a time
2. After each question wait for the response, after each response, evaluate the candidate's answer based on relevance, clarity, and completeness.
3. Provide constructive feedback and assign a score out of 10 for the response. Explain the reasoning for the score.
4. calculate the average score after every question
5. Continue to the next question based on previous response
7. keep a count on the number of questions and mention question number
8. donot say lets begin with the first question every time
9. display the score after every question and give suggestions to improvise the answer
10. suggest a better answer based on the response
11. after 15 questions if the average score is below 6, inform the cancidate that his respones are inefficient and ask him to put in more preparation



Example:
Interviewer: What is your experience with software development?
Candidate: I have worked on several projects using Python and Java.
Interviewer: Great! Your answer shows relevant experience but could include more detail about specific projeyescts. Score: 8/10
"""
import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()  # Wait for the speech to finish

# Example Usage
text = "Hello! This is a demonstration of text-to-speech in Python without saving an MP3 file."
text_to_speech(text)



# Chatbot Function
def interview_chatbot(job_type, user_response=None):
    # Format the base prompt with the specific job type
    formatted_prompt = base_prompt.format(job_type=job_type)
    
    # Prepare the message list for the AI
    messages = [{"role": "system", "content": formatted_prompt}]
    if user_response:
        messages.append({"role": "user", "content": user_response})
    
    # Send request to Groq API
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stop=None,
    )
    
    # Return the AI's response
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    # Get the job type from the user
    text_to_speech("What type of job preparation are you searching for? ")
    job_type = input("What type of job preparation are you searching for? ").strip()
    print(f"\nPreparing for a {job_type} interview...\n")
    
    while True:
        # Get the chatbot's question
        question = interview_chatbot(job_type)
        print("Interviewer:", question)
        text_to_speech(question)
        
        # Get the user's response
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'break', 'stop', 'bye']:
            print("Goodbye! Best of luck with your interviews.")
            text_to_speech("Goodbye! Best of luck with your interviews.")
            break
        
        # Get feedback and next question
        feedback = interview_chatbot(job_type, user_response=user_input)
        print("Interviewer:", feedback)
        text_to_speech(feedback)