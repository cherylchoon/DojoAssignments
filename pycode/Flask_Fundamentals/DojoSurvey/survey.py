from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def surveyform():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    survey_name = request.form['name']
    survey_location = request.form['location']
    survey_language = request.form['language']
    survey_comment = request.form['comment']

    return render_template('result.html', result_name=survey_name, result_location=survey_location, result_language=survey_language, result_comment=survey_comment)

app.run(debug=True)
