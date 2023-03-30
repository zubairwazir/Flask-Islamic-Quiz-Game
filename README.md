## Flask Islamic Quiz Game 
Here is a step-by-step guide on how to create an Islamic Quiz Game using Python and Flask:

1. Create a database of Islamic quiz questions and answers in a CSV file or any other database format. For example:

```
Question,Answer
What is the first pillar of Islam?,Shahada
What is the Islamic holy book?,Quran
What is the name of the pilgrimage to Mecca?,Hajj
What is the name of the month of fasting in Islam?,Ramadan
Who was the first Caliph of Islam?,Abu Bakr
```

2. Install the Flask library if it's not already installed in your Python environment. You can do this by running the following command in your terminal or command prompt:

```pip install flask```

3. Create a Flask app in your Python script **app.py**:

```
from flask import Flask, render_template, request
import random
import csv

app = Flask(__name__)
```
4. Load the quiz questions and answers from the CSV file into a list of dictionaries:

```
quiz_data = []

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        quiz_data.append(row)
```
5. Create a route for the quiz page that displays a random question from the quiz data:

```
@app.route('/')
@app.route('/quiz')
def quiz():
    question = random.choice(quiz_data)
    return render_template('quiz.html', question=question)
```
6. Create a HTML template for the quiz page that displays the question and allows the user to submit their answer:
```
<!DOCTYPE html>
<html>
<head>
    <title>Islamic Quiz Game</title>
</head>
<body>
    <h1>Islamic Quiz Game</h1>
    <p>{{ question['Question'] }}</p>
    <form action="{{ url_for('answer') }}" method="POST">
        <input type="hidden" name="question" value="{{ question['Question'] }}">
        <input type="text" name="answer" placeholder="Enter your answer">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
7. Create a route for the answer page that checks the user's answer and displays the result:
``` 
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
```
8. Create a HTML template for the answer page that displays whether the user's answer was correct or not:
```
<!DOCTYPE html>
<html>
<head>
    <title>Islamic Quiz Game</title>
</head>
<body>
    <h1>Islamic Quiz Game</h1>
    <p>{{ result }}</p>
    <a href="{{ url_for('quiz') }}">Next Question</a>
</body>
</html>
 ```
9. Here is complete **app.py**:
``` 
from flask import Flask, render_template, request
import random
import csv

app = Flask(__name__)

quiz_data = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        quiz_data.append(row)


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
```
10. Run the Flask app in terminal:
```
flask run
or
python app.py
```
**Author:** [Zubair Ahmad](https://zubairwazir.github.io/)

**Contact:** Follow me on [LinkedIn](https://www.linkedin.com/in/zubairwazir/) and [Twitter](https://twitter.com/zubairwazir777)