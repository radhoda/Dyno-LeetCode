from leetcode_data import scrape_leetcode, database

if __name__ == "__main__":
    scraper = scrape_leetcode.Scrape_Questions()
    scraper.scrape_questions()
    questions = scraper.get_questions()
    databaseHandler = database.DatabaseHandler()

    databaseHandler.add_questions(questions)
    question_list = databaseHandler.get_questions()

    print("Anything")
