from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import openai

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

# Set up OpenAI API credentials
openai.api_key = "enter you openai api key"

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    try:
        # Get the message from the POST request
        message = request.json.get("message")
        if not message:
            return jsonify({"error": "No message provided"}), 400

        # Send the message to OpenAI's API and receive the response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        
        response = completion.choices[0].message['content']
        return jsonify({"content": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
