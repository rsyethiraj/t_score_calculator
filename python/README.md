*PYTHON IMPLEMENTATION*
---

There are 3 files in the python implementation: 
---
- calculate_t_score.py - Contains all the methods required to calculate a T score. It can be run both as a script of as part of the flask web server. 
    - To run the file as a script, simply input 'python t_score_calculator,.py -w [add your weights here] -s [add your erg scores here either as splits or watts] -n [optionally add names here]'. If you want to input weights as pounds, make sure to add the flag '-b' or the weights will be inputted as kilograms. 
- app.py - Running this app in a web server with the command 'FLASK_APP=app.py flask run --port=5001' will create a web server on Localhost/5001 which can be used by both the react frontend and by another terminal window. To test the backend out, you can send it POST requests from another window using the command: ' curl -X POST http://localhost:5001/t-score \
     -H "Content-Type: application/json" \
     -d '{"weights": [your weights here], "speeds": [your speeds here]}, "names: [optionally, your names here]", 'in_lbs': (optionally True)'. Make sure to replace the fields with desired values. 
- react frontend not implemented yet. 

