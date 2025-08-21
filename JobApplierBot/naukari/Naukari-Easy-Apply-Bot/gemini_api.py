"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyCHD3BOd8-aNp_KCEs_JE0S7uc7Zfy3NOE")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "Remember the provided resume data when answering questions. "
        "Be concise: min 1 word, average 3 words, max 5 words. "
        "For multiple-choice questions, return only the index number."
    ),
)

# Fixed and valid resume JSON
resume_data = """
{
  "name": "Anant Langote",
  "contact": {
    "phone": "9972459442",
    "email": "ananthlangote0317@gmail.com"
  },
  "education": [
    {
      "degree": "B.Tech in Computer Science Engineering",
      "institution": "Bheemanna Khandre Institute of Technology, Bhalki",
      "startDate": "2018",
      "endDate": "2022",
      "cgpa": "7.9"
    },
    {
      "degree": "PU Science",
      "institution": "Diamond Independent PU Science College, Bhalki",
      "startDate": "2016",
      "endDate": "2018",
      "percentage": "83.33"
    },
    {
      "degree": "SSLC",
      "institution": "Govt Morarji Desai Lingeri STN, Yadgir",
      "startDate": "2015",
      "endDate": "2016",
      "percentage": "78.88"
    }
  ],
  "skills": {
    "languages": ["Java", "JavaFX", "C++", "Python", "SQL", "MySQL", "MariaDB"],
    "frameworks": ["Spring Boot", "Microservices"],
    "tools": ["Confluence", "Enterprise Architect", "DrawIO", "Apache JMeter", "Git"],
    "testing": ["JUnit", "FxRobot (GUI Testing)"],
    "os": ["Linux"],
    "other": ["XML", "XSD"]
  },
  "languages": ["Marathi", "Kannada", "English", "Hindi"],
  "experience": [
    {
      "title": "Software Engineer",
      "company": "ALTEN Global Technologies Pvt Ltd",
      "location": "Bangalore",
      "startDate": "Nov 2022",
      "endDate": "Present",
      "responsibilities": [
        "Designed and implemented software using Java, C++, SQL, MySQL, and MariaDB.",
        "Collaborated with stakeholders to gather requirements and create UML designs.",
        "Developed performance testing frameworks using Apache JMeter.",
        "Wrote and maintained protobuf messages for client-server communication.",
        "Developed user interfaces using JavaFX in a Linux environment.",
        "Debugged and resolved production-level issues.",
        "Contributed to version control with Git and documentation using Confluence."
      ]
    }
  ],
  "projects": [
    {
      "name": "Sonar Application Development for Ultra CSS (Defence)",
      "year": "2022 - Present",
      "description": "Developing client-server communication with protobuf, designing software using Java, JavaFX, and C++ in Linux, ensuring timely delivery of project milestones."
    }
  ],
  "summary": "Software Engineer with 2.9 years of experience in designing and maintaining scalable software solutions. Skilled in Java, C++, Python, databases, and testing frameworks. Experienced in performance testing, GUI automation, and collaborative development using Git, Confluence, and Enterprise Architect."
}
"""

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [resume_data],
        },
        {
            "role": "model",
            "parts": [
                "Resume data received. I'll use this information to answer questions concisely."
            ],
        },
        {
            "role": "user",
            "parts": [
                "Remember this resume data. Answer questions using it. "
                "Responses: min 1 word, average 3 words, max 5 words."
            ],
        },
        {
            "role": "model",
            "parts": [
                "Understood. I'll answer using resume data: min 1 word, average 3 words, max 5 words."
            ],
        },
    ]
)



def bard_flash_response(question) -> str:
    try:
        response = chat_session.send_message(question)
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "0"  # Always return string for consistency