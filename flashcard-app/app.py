from flask import Flask, jsonify

app = Flask(__name__)


flashcards = [
    {"id": 1, "question": "What keyword defines a function in Python?", "answer": "def"},
    {"id": 2, "question": "What data structure uses key-value pairs?", "answer": "dictionary"},
    {"id": 3, "question": "How do you output text to the terminal in Python?", "answer": "print"}
]

@app.route("/")
def home():
    return jsonify(flashcards)

@app.route("/flashcards/<int:card_id>")
def get_flashcard(card_id):
    
    for card in flashcards:
        if card["id"] == card_id:
            return jsonify(card)
    
    return jsonify({"error": "Flashcard not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)