# USSD & Mobile Services Simulator

A lightweight Python Flask application that simulates a telecom USSD menu flow (View Balance, Recharge, Kopa Loans, and More) paired with a mobile-native web popup interface for real-time local testing and demonstration.

---

 🚀 Features
* **Session State Management:** Tracks user navigation history using accumulator strings (e.g., `3*1` for nested menus).
* **Telecom Protocol Simulation:** Mimics standard carrier response syntax using `CON` (continue session) and `END` (terminate session).
* **Mobile-Native UI:** Includes a built-in browser-based popup interface designed to look and feel like a native mobile carrier dialog box.
* **RESTful API Integration:** Utilizes asynchronous JavaScript (`fetch`) to handle communication between the frontend interface and Python backend.

---

## 🛠️ Tech Stack
* **Backend:** Python, Flask, REST API routing
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), DOM Manipulation
* **Tools:** Git, GitHub, VS Code

---

## 📂 Project Structure
```text
ussd-mobile-simulator/
│
├── app.py              # Main Flask server containing USSD logic & UI template
└── README.md           # Project documentation
