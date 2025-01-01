from leetcode_data.database import DatabaseHandler, Question
from flask import Flask, render_template, request

app = Flask(__name__)

db_handler = DatabaseHandler()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query', '')

    results = []
    if query:
        session = db_handler.session
        results = session.query(Question).filter(Question.title.ilike(f"%{query}%")).all()

    return render_template('results.html', query=query, results=results)


if __name__ == "__main__":
    # scraper = scrape_leetcode.Scrape_Questions()
    # scraper.scrape_questions()
    # questions = scraper.get_questions()

    # databaseHandler = database.DatabaseHandler()
    # # databaseHandler.add_questions(questions)
    # question_list = databaseHandler.get_questions()
    #
    # print("Anything")
    app.run(debug=True)
