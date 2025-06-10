from flask import Flask, request, jsonify
from flask_cors import CORS
from t_score_calculator import calculate_t_scores, convert_input_to_watts

app = Flask(__name__)
CORS(app)

@app.route('/t-score', methods=['POST'])
def compute_t_score():
    try:
        data = request.json
        weights = data.get('weights')
        speeds = data.get('speeds')
        names = data.get('names', None)
        in_lbs = data.get('in_lbs', False)
        
        if not weights or not speeds:
            return jsonify({'error': 'Both rower weights and rower erg scores (speeds) must be provided. '}), 400
        if len(weights) != len(speeds):
            return jsonify({'error': 'The same number of weights and rower erg scores must be provided. '}), 400
        if names and len(names) != len(weights):
            return jsonify({'error': 'If names are provided, the same number of names and weights must be provided. '}), 400
        weights = [float(w) / 2.2 if in_lbs else float(w) for w in weights]
        speeds = convert_input_to_watts(speeds)
        scores = calculate_t_scores(weights, speeds, names)
        return jsonify({'t_scores': scores})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
if __name__ == '__main__':
    app.run(debug=True)
