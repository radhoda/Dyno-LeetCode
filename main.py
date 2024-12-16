from leetcode_data import scrape_leetcode, database

if __name__ == "__main__":
    scraper = scrape_leetcode.Scrape_Questions()
    questions = scraper.get_questions()
    databaseHandler = database.DatabaseHandler()

    databaseHandler.add_questions(questions)
