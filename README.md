# Advanced Personality Diagnosis System in Python

## Project Overview
This project is an advanced personality diagnosis system developed in Python, based on professional morphological questions by Tehila Carmel. The system provides a comprehensive and user-friendly experience for users to answer, postpone, or change their responses to questions. Upon completion and data processing, the system delivers accurate and insightful information about the user's personality type.

## Motivation
In recent years, there has been a growing awareness of the importance of improving communication with our environment. New methods are being taught, workshops are held, and there is a significant emphasis on self-awareness and understanding communication styles. Personality assessments help individuals recognize their strengths, unique abilities, and potential challenges, offering actionable insights for personal growth and improved interactions.

## Features & Functionality
- **Two-Part Questionnaire:**
  - 30 challenging questions divided into two sections, each with 15 questions.
  - Each question presents two behavioral options; the user selects the one that best describes them.
- **Flexible Response Management:**
  - Users can answer, postpone, or change their responses at any stage.
  - Postponed questions are revisited later, ensuring all questions are eventually answered.
  - Users can review all answered questions, change previous answers, or respond to postponed questions.
  - The system always presents the next unanswered question upon returning to the questionnaire.
- **Completion Validation:**
  - The system ensures all questions are answered before proceeding.
  - Any remaining postponed questions are highlighted for completion.
- **Scientific Result Calculation:**
  - Results are calculated using a mathematical model based on Tehila Carmel's methodology, providing immediate and accurate feedback without manual calculations.
- **In-Depth Personality Insights:**
  - After diagnosis, users can explore detailed information about any of the four personality types, including descriptions, strengths, weaknesses, and improvement tips.
  - Users can view information about any type, not just their own, as many times as they wish.
  - Option to display secondary communication styles for deeper understanding.
- **Robust Input Validation:**
  - Lambda functions for addition and subtraction.
  - Exception handling to ensure only valid numeric input is accepted, preventing invalid entries.

## Technologies Used
- **Python 3**
- **Standard Python Libraries** (no external dependencies)
- **Object-Oriented Programming**
- **Exception Handling**
- **Dictionary Data Structures**
- **Functional Programming (Lambdas)**

## Project Structure
- `Main.py` – Entry point, manages the main flow and user interaction.
- `code.py` – Contains core logic, question management, result calculation, and utility functions.
- `file1.txt`, `file2.txt`, `file3.txt`, `file4.txt` – Data files for questions, results, or user data.

## How It Works
1. The user is presented with a series of questions, each offering two behavioral options.
2. At any point, the user can answer, postpone, or change their response.
3. The system tracks all responses, postponed questions, and allows for review and modification.
4. Once all questions are answered, the system calculates the result using a scientific method.
5. The user receives a detailed personality analysis and can explore information about all personality types.

## Author
Tehila Siman Tov, 2024

---

*This project was developed as part of a Python course, inspired by the professional work of Tehila Carmel. It aims to provide users with a meaningful, accurate, and insightful personality diagnosis experience.*

---

**BS"D**
