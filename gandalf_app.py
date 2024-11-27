from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

@app.route('/quote', methods=['GET'])
def get_quote():
    try:
        # Read quotes from the file
        with open('gandalf_quotes.txt', 'r') as file:
            quotes = file.readlines()
        if not quotes:
            return jsonify({"error": "No quotes available!"}), 500

        # Choose a random quote
        random_quote = random.choice(quotes).strip()

        # List of Gandalf images
        gandalf_images = [
            "images/gandalf0.jpg",
            "images/gandalf1.jpg",
            "images/gandalf2.jpg",
            "images/gandalf3.jpg",
            "images/gandalf4.jpg",
            "images/gandalf5.jpg",
            "images/gandalf6.jpg",
            "images/gandalf7.jpg",
        ]

        random_image = random.choice(gandalf_images)


        # Return as JSON
        return jsonify({"quote": random_quote, "image": random_image})
    except FileNotFoundError:
        print("FileNotFoundError")
        return jsonify({"error": "gandalf_quotes.txt not found!"}), 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)