import google.generativeai as genai
import json
import os

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


def generate_summary(text, bullet_points=10):
    """
    Generate AI summary from chapter content using Google Gemini
    """
    if not GEMINI_API_KEY:
        return "Google Gemini API key not configured"
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Summarize the following text into {bullet_points} bullet points:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return f"Error generating summary: {str(e)}"


def generate_mcq_quiz(chapter_content, num_questions=10):
    """
    Auto-generate Multiple Choice Questions from chapter content using Google Gemini
    """
    if not GEMINI_API_KEY:
        return []
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""
        Generate {num_questions} multiple choice questions based on the following chapter content.
        Format the response as a JSON array with the following structure:
        [
            {{
                "question": "Question text here?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 0,
                "difficulty": "easy"
            }}
        ]
        
        Chapter Content:
        {chapter_content[:2000]}
        
        Return ONLY the JSON array, no additional text.
        """
        
        response = model.generate_content(prompt)
        # Extract JSON from response
        response_text = response.text.strip()
        # Remove markdown code blocks if present
        if response_text.startswith('```json'):
            response_text = response_text[7:]
        if response_text.startswith('```'):
            response_text = response_text[3:]
        if response_text.endswith('```'):
            response_text = response_text[:-3]
        
        quiz_data = json.loads(response_text.strip())
        return quiz_data
    except Exception as e:
        print(f"Quiz Generation Error: {e}")
        return []


def solve_doubt(problem_description, problem_image=None):
    """
    AI-powered doubt solver using Google Gemini
    """
    if not GEMINI_API_KEY:
        return "Google Gemini API key not configured"
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""
        A student has the following doubt/problem:
        
        {problem_description}
        
        Please provide a detailed step-by-step solution with explanation.
        Make it clear and educational for students.
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Doubt Solver Error: {e}")
        return f"Error solving doubt: {str(e)}"


def generate_flashcards(chapter_content, num_cards=20):
    """
    Auto-generate flashcards from chapter content using Google Gemini
    """
    if not GEMINI_API_KEY:
        return []
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"""
        Generate {num_cards} flashcard pairs (question-answer) based on the following chapter content.
        Format as JSON array:
        [
            {{
                "question": "What is...",
                "answer": "The answer is..."
            }}
        ]
        
        Chapter Content:
        {chapter_content[:2000]}
        
        Return ONLY the JSON array, no additional text.
        """
        
        response = model.generate_content(prompt)
        # Extract JSON from response
        response_text = response.text.strip()
        # Remove markdown code blocks if present
        if response_text.startswith('```json'):
            response_text = response_text[7:]
        if response_text.startswith('```'):
            response_text = response_text[3:]
        if response_text.endswith('```'):
            response_text = response_text[:-3]
        
        flashcards = json.loads(response_text.strip())
        return flashcards
    except Exception as e:
        print(f"Flashcard Generation Error: {e}")
        return []


def explain_concept(concept_name, grade_level):
    """
    Generate a detailed explanation of a concept using Google Gemini
    """
    if not GEMINI_API_KEY:
        return "Google Gemini API key not configured"
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Explain the concept of '{concept_name}' for Class {grade_level} students in simple terms with examples. Make it easy to understand and educational."
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Concept Explanation Error: {e}")
        return f"Error explaining concept: {str(e)}"
