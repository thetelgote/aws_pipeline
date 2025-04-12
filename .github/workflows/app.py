from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)  # ✅ fixed typo

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f1f1f1;
        }

        .chat-container {
            width: 400px;
            height: 500px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-color: white;
            display: flex;
            flex-direction: column;
            padding: 20px;
        }

        .chat-box {
            flex-grow: 1;
            overflow-y: auto;
            margin-bottom: 20px;
            padding-right: 10px;
        }

        .chat-message {
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
            max-width: 80%;
        }

        .chat-message.bot {
            background-color: #e0e0e0;
            align-self: flex-start;
        }

        .chat-message.user {
            background-color: #4caf50;
            color: white;
            align-self: flex-end;
        }

        .user-input {
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #ddd;
            width: calc(100% - 60px);
            margin-right: 10px;
        }

        #send-btn {
            background-color: #4caf50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }

        #send-btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<div class="chat-container">
    <div id="chat-box" class="chat-box">
        <div id="bot-message" class="chat-message bot">Hello! How can I assist you today?</div>
    </div>
    <input type="text" id="user-input" class="user-input" placeholder="Type a message...">
    <button id="send-btn">Send</button>
</div>

<script>
    const sendButton = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    sendButton.addEventListener("click", function() {
        const message = userInput.value;
        if (message.trim() !== "") {
            const userMessage = document.createElement("div");
            userMessage.classList.add("chat-message", "user");
            userMessage.textContent = message;
            chatBox.appendChild(userMessage);

            fetch(`/get?msg=${encodeURIComponent(message)}`)
                .then(response => response.json())
                .then(data => {
                    const botMessage = document.createElement("div");
                    botMessage.classList.add("chat-message", "bot");
                    botMessage.textContent = data.response;
                    chatBox.appendChild(botMessage);
                    chatBox.scrollTop = chatBox.scrollHeight;
                });
        }
        userInput.value = "";
    });
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_code)

@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    user_input = request.args.get("msg")
    bot_response = f"You said: {user_input}"
    return jsonify({"response": bot_response})

if __name__ == "__main__":  # ✅ fixed typo
    app.run(host="0.0.0.0", port=5000, debug=True)
