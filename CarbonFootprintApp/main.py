from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import openai
import psycopg2
import os

# Load environment variables for OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Database connection setup
def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# Data models
class Activity(BaseModel):
    activity_type: str
    value: float

class User(BaseModel):
    name: str
    email: str
    activities: List[Activity]

# Routes
@app.post("/calculate")
def calculate_carbon_footprint(user: User):
    """Calculate the carbon footprint based on user activities."""
    emission_factors = {
        "car": 0.27,  # kg CO2 per km
        "bus": 0.05,
        "flight": 0.25,
        "electricity": 0.45  # kg CO2 per kWh
    }

    total_emissions = 0
    for activity in user.activities:
        factor = emission_factors.get(activity.activity_type.lower(), None)
        if factor is None:
            raise HTTPException(status_code=400, detail=f"Unknown activity: {activity.activity_type}")
        total_emissions += factor * activity.value

    return {"user": user.name, "total_emissions": total_emissions}

@app.post("/recommendations")
def generate_recommendations(user: User):
    """Generate personalized recommendations using OpenAI API."""
    user_activities = ", ".join([f"{activity.activity_type}: {activity.value}" for activity in user.activities])
    prompt = (
        f"The user has the following activities: {user_activities}. "
        "Suggest actionable steps to reduce their carbon footprint."
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    recommendations = response.choices[0].text.strip()
    return {"user": user.name, "recommendations": recommendations}

# Health check
@app.get("/health")
def health_check():
    return {"status": "API is running"}