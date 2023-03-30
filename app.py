from flask import Flask, render_template, request
import random
import csv

app = Flask(__name__)

quiz_data = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        quiz_data.append(row)
print(quiz_data)


@app.route('/')
@app.route('/quiz')
def quiz():
    question = random.choice(quiz_data)
    return render_template('quiz.html', question=question)


@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']
    user_answer = request.form['answer']
    correct_answer = next((q['Answer'] for q in quiz_data if q['Question'] == question), None)
    if user_answer.lower() == correct_answer.lower():
        result = "Correct!"
    else:
        result = f"Sorry, the correct answer is {correct_answer}."
    return render_template('answer.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
