from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # This allows other apps to talk to this one

@app.route('/calculate', methods=['GET'])
def calculate():
    """
    Calculates the absolute distance between a current value and a goal value.
    Request Params:
        - current (float): The starting number
        - goal (float): The target number
    Returns:
        - JSON object with 'distance' and 'status'
    """
    # Get arguments from the URL
    current_val = request.args.get('current', type=float)
    goal_val = request.args.get('goal', type=float)

    # Validation: Ensure both numbers are provided
    if current_val is None or goal_val is None:
        return jsonify({
            "error": "Missing parameters. Please provide 'current' and 'goal'.",
            "status": "error"
        }), 400

    # Logic: Calculate Absolute Difference
    # We use abs() so it works for goals that are positive or negative
    distance = abs(current_val - goal_val)

    # Return JSON Response
    return jsonify({
        "original_current": current_val,
        "original_goal": goal_val,
        "distance": round(distance, 2), # Round to 2 decimal places
        "status": "success"
    })

if __name__ == '__main__':
    # Make sure this port is different from main app port
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)