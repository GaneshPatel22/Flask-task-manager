# AI Profile Builder

## Overview

AI Profile Builder is a Flask-based web application that generates professional profiles of public personalities using AI and publicly available information.

The application retrieves information from Wikipedia, sends the retrieved context to an AI model through OpenRouter, and generates a structured profile with references.

---

## Features

- AI-generated professional profiles
- Wikipedia information retrieval
- Automatic profile image
- Source references
- Download profile as PDF
- Responsive web interface
- Error handling for unavailable AI services

---

## Tech Stack

- Python
- Flask
- HTML
- CSS
- OpenRouter API
- Requests
- Markdown
- ReportLab

---

## AI Workflow (RAG-style)

1. User enters a person's name.
2. The Retriever module fetches public information from Wikipedia.
3. The retrieved context is sent to the AI model via OpenRouter.
4. The AI generates a structured professional profile.
5. The profile, image, and references are displayed in the web application.
6. Users can download the generated profile as a PDF.

---

## Project Structure

```
AI_Profile_Builder/
│
├── app.py
├── requirements.txt
├── utils/
│   ├── gemini.py
│   └── retriever.py
├── Templates/
│   ├── index.html
│   └── profile.html
├── Static/
│   ├── Style.css
│   └── script.js
```

---

## Installation

Clone the repository

```bash
git clone <repository_url>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
OPENROUTER_API_KEY=YOUR_API_KEY
```

Run

```bash
python app.py
```

---

## Sample Input

Name:

```
Satya Nadella
```

---

## Output

The application generates:

- Executive Summary
- Biography
- Career
- Achievements
- References
- Profile Image

---

## Future Improvements

- News retrieval
- Better RAG pipeline
- Multiple data sources
- AI fact verification
- Better PDF formatting