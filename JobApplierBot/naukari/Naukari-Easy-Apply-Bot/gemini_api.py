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
    "linkedin": "https://www.linkedin.com/in/anant-langote-544030241"
  },
  "education": [
    {
      "degree": "B.Tech in Computer Science Engineering",
      "institution": "Bheemanna Khandre Institute of Technology, Bhalki",
      "startDate": "2018",
      "endDate": "2022",
      "cgpa": "7.9"
    }
  ],
  "skills": {
    "languages": ["Java", "JavaFX",  "SQL", "MySQL", "MariaDB"],
    "frameworks": ["Spring Boot", "JavaFX"],
    "tools": ["Confluence", Visual Studio Code", "IntelliJ", "Eclipse", "Enterprise Architect", "DrawIO", "Apache JMeter", "Git"],
    "testing": ["JUnit", "FxRobot (GUI Testing)"],
	"scripting": ["Bash"],
    "os": ["Linux"],
    "softSkills": ["Communication", "Collaboration", "Adaptability", "Time Management"]
  },
  "languages": ["Marathi", "Kannada", "English", "Hindi"],
  "experience": [
    {
      "title": "Software Engineer",
      "company": "Alten Global Technology Pvt Ltd",
      "location": "Bengaluru, India",
      "startDate": "Nov 2022",
      "endDate": "Present",
      "responsibilities": [
        "Developed charts and processed cartographic data for sonar systems using Java and Spring Boot.",
        "Performed mosaic calculations for active, passive, and ray data, improving analysis efficiency by 15%.",
        "Integrated calculations into real-time apps for seamless system performance."
      ]
    }
  ],
  "projects": [
    {
      "name": "Sonar Application for Ultra CSS",
      "year": "2023",
      "description": "Designed a JavaFX-Spring Boot sonar app for real-time visualization aligned to client requirements."
    },
    {
      "name": "Test Harness Tool",
      "description": "Built tool to test sonar plugins on laptops, replacing need for lab environment."
    },
    {
      "name": "Employee Engagement Tool",
      "description": "Created tool to help new joiners onboard and learn project-related content efficiently."
    }
  ],
  "activities": [
    "Led a team to win two hackathons, demonstrating technical and leadership skills."
  ]
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