from flask import Flask, render_template_string, request

app = Flask(__name__)

# USSD Logic Endpoint
@app.route("/ussd", methods=["POST", "GET"])
def ussd():
    # Support both form data (from simulator/gateway) and JSON
    text = request.values.get("text", "")
    
    text_array = text.split("*")
    user_response = text_array[-1].strip() if text else ""

    # 1. MAIN MENU
    if text == "":
        response = "CON Welcome to Mobile Services\n"
        response += "1. View Balance\n"
        response += "2. Recharge\n"
        response += "3. Kopa\n"
        response += "4. More"

    # 2. OPTION 1: VIEW BALANCE
    elif text == "1":
        response = "END Your current account balance is KES 1,450.00."

    # 3. OPTION 2: RECHARGE
    elif text == "2":
        response = "CON Enter amount to recharge:"
    elif len(text_array) == 2 and text_array[0] == "2":
        amount = user_response
        response = f"END Success! You have recharged KES {amount}."

    # 4. OPTION 3: KOPA
    elif text == "3":
        response = "CON Kopa Loan Limit: KES 5,000\n"
        response += "1. Request Loan\n"
        response += "2. Check Limit\n"
        response += "99. Back"
    elif text == "3*1":
        response = "END Your loan request of KES 1,000 has been sent."
    elif text == "3*2":
        response = "END Your current borrow limit is KES 5,000."

    # 5. OPTION 4: MORE SERVICES
    elif text == "4":
        response = "CON More Services:\n"
        response += "1. Mini Statement\n"
        response += "2. My Account\n"
        response += "99. Back"
    elif text == "4*1":
        response = "END Last txn: -KES 200 to Electricity."
    elif text == "4*2":
        response = "END Account status: Active."

    # 6. GLOBAL BACK / HOME
    elif user_response == "99":
        response = "CON Welcome to Mobile Services\n"
        response += "1. View Balance\n"
        response += "2. Recharge\n"
        response += "3. Kopa\n"
        response += "4. More"

    else:
        response = "END Invalid option. Please try again."

    return response

# Browser UI Simulator Home Page
@app.route("/", methods=["GET"])
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>USSD Simulator</title>
        <style>
            body { font-family: Arial, sans-serif; background: #121212; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .phone { background: #222; padding: 25px; border-radius: 20px; width: 320px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); border: 2px solid #444; }
            .screen { background: #0f172a; color: #38bdf8; padding: 15px; border-radius: 10px; min-height: 120px; font-family: monospace; white-space: pre-wrap; font-size: 14px; margin-bottom: 15px; border: 1px solid #334155; }
            input { width: 100%; padding: 10px; box-sizing: border-box; background: #333; border: 1px solid #555; color: white; border-radius: 5px; margin-bottom: 10px; font-size: 16px; }
            button { width: 100%; padding: 10px; background: #22c55e; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 16px; }
            button:hover { background: #16a34a; }
        </style>
    </head>
    <body>
        <div class="phone">
            <h3>USSD Test Simulator</h3>
            <div id="screen" class="screen">Loading...</div>
            <input type="text" id="userInput" placeholder="Enter option (e.g. 1)" autofocus>
            <button onclick="sendUssd()">Send / Submit</button>
            <button onclick="resetSession()" style="background:#ef4444; margin-top:8px;">Reset / Home</button>
        </div>

        <script>
            let currentText = "";

            async function fetchUssd(textSequence) {
                let formData = new URLSearchParams();
                formData.append("text", textSequence);

                let res = await fetch("/ussd", {
                    method: "POST",
                    body: formData
                });
                let data = await res.text();
                
                document.getElementById("screen").innerText = data;
                
                if (data.startsWith("END")) {
                    // Session ended, next input resets or handles
                }
            }

            function sendUssd() {
                let input = document.getElementById("userInput");
                let val = input.value.trim();
                if (!val) return;

                if (currentText === "") {
                    currentText = val;
                } else {
                    currentText += "*" + val;
                }

                input.value = "";
                fetchUssd(currentText);
            }

            function resetSession() {
                currentText = "";
                document.getElementById("userInput").value = "";
                fetchUssd("");
            }

            // Load main menu on start
            fetchUssd("");

            // Allow Enter key to submit
            document.getElementById("userInput").addEventListener("keypress", function(e) {
                if (e.key === 'Enter') sendUssd();
            });
        </script>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)