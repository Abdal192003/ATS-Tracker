# ATS Resume Tracking System

A Streamlit web application that uses Google's Gemini AI to analyze resumes against job descriptions and provide ATS (Applicant Tracking System) compatibility scores.

## Features
- Upload your resume in PDF format
- Enter job description text
- Get AI-powered analysis of your resume's compatibility
- Receive suggestions for improvement

## Prerequisites
- Python 3.8+
- Google API key with access to Gemini AI

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd ATS-Tracker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running Locally

```bash
streamlit run app.py
```

## Deployment

### Streamlit Cloud (Recommended)
1. Push your code to a GitHub repository
2. Sign up at [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and connect your repository
4. Set `GOOGLE_API_KEY` in the app's settings
5. Deploy!

## License
[MIT](LICENSE)
