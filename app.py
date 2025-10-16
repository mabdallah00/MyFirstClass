from flask import Flask, jsonify 
from party_event import PartyEvent 

app = Flask(__name__)

@app.route('/api/event')
def get_event():
  event = PartyEvent("Omar's Birthday Party", "11/03/2025", "6:00pm", "Banquet Hall", "Maysam Abdallah", "Dinosaurs", 100)
  return jsonify(vars(event))

if __name__ == "__main__":
  app.run(debug=True)
