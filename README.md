# 🌍 Carbon Footprint Tracking App

## 📖 Overview
The **Carbon Footprint Tracking App** is designed to help users measure and reduce their environmental impact by calculating the carbon dioxide (CO2) emissions produced by their daily activities. It leverages modern technologies, including **React Native** for the frontend, **FastAPI** for the backend, and an **LLM (Large Language Model)** for personalized recommendations.

---

## ✨ Features
- 🚗 **Activity Tracking**: Input daily activities like driving, electricity usage, or flights.
- 📊 **Carbon Footprint Calculation**: Calculate the total CO2 emissions for each activity.
- 🤖 **AI-Powered Recommendations**: Get personalized tips on reducing your carbon footprint.
- ⚡ **Real-Time Updates**: Changes in the app are reflected instantly using hot reloading.

---

## 🛠️ Tech Stack
- **Frontend**: React Native (with Expo for development)
- **Backend**: Python (FastAPI framework)
- **Database**: PostgreSQL
- **AI Integration**: OpenAI API for generating recommendations
- **Containerization**: Docker

---

## 🚀 How It Works
1. **User Inputs Activities**:
   - Enter an activity type (e.g., car, electricity).
   - Provide a value (e.g., kilometers driven or kWh consumed).
2. **Backend Calculation**:
   - The app sends data to the backend, which calculates the carbon footprint using predefined emission factors.
3. **Result Display**:
   - The calculated CO2 emissions are displayed in the app.
4. **AI Recommendations** (optional):
   - AI suggests actionable ways to reduce your carbon footprint.

---

## 🖥️ Installation

### Prerequisites
- Node.js
- Python 3.9+
- Expo CLI
- Docker (optional for containerization)
- PostgreSQL database

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/carbon-footprint-tracker.git
   cd carbon-footprint-tracker/backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the backend server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
4. Test the server:
   - Open your browser and visit `http://127.0.0.1:8000/health`.

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Expo development server:
   ```bash
   expo start
   ```
4. Open the app in **Expo Go**:
   - Download Expo Go from the [Google Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent) or [Apple App Store](https://apps.apple.com/app/expo-go/id982107779).
   - Scan the QR code displayed in the terminal/browser.

---

## Results:
![WhatsApp Image 2025-01-06 at 23 02 03_8ee87a3d](https://github.com/user-attachments/assets/982ca5e6-9464-403b-9500-3bf8fab8c7e4)

![WhatsApp Image 2025-01-06 at 23 02 03_14b690b8](https://github.com/user-attachments/assets/534fd7aa-6cc7-44a3-8cba-723991651d22)

---

## 📂 Project Structure
```
carbon-footprint-tracker/
├── backend/
│   ├── main.py         # FastAPI backend code
│   ├── models.py       # Pydantic models
│   ├── requirements.txt # Backend dependencies
├── frontend/
│   ├── App.js          # React Native app entry point
│   ├── components/     # UI components
│   ├── package.json    # Frontend dependencies
├── Dockerfile          # Docker setup
└── README.md           # Project documentation
```

---

## ⚠️ Troubleshooting
- Ensure your phone and PC are connected to the same network for Expo Go.
- If the backend isn’t reachable:
  - Verify the `host` is set to `0.0.0.0`.
  - Check the firewall settings.
  - Replace `localhost` with your PC’s IP address in the fetch URL.
- Use the **Tunnel** option in Expo if QR code scanning doesn’t work.

---

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

---



### Made with ❤️ for a greener planet! 🌿

