from flask import Flask, render_template, request, redirect
import data_manager as dm
import connection as cm

app = Flask(__name__)


@app.route('/')
@app.route('/list', methods=['POST', 'GET'])
def route_list():
    """Show list of questions, sorted by the latest question on top"""
    question_path = "sample_data/question.csv"
    unordered_questions = dm.get_all_data_from_file(question_path)
    sorted_questions = cm.descending_sort_data_by_parameter(unordered_questions, 'submission_time')
    return render_template('list.html', sorted_questions=sorted_questions)


@app.route('/add-question', methods=['POST', 'GET'])
def add_question():
    """Add new question to list, then redirect to /list page"""
    if request.method == 'POST':
        title = request.form["title"]
        message = request.form["message"]
        values = (title, message)
        return redirect("/list", values=values)
    else:
        return render_template('add-question.html')


# @app.route('/question/<question_id>')
# def route_expand_question(question_id: int):
#

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
