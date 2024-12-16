import requests

class Scrape_Questions():
    def __init__(self):
        self.totalNumQuestions = 0
        self.questionsList = []
    def get_question_by_tag(self):
        data = {
            "query": """query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
                    problemsetQuestionList: questionList(
                        categorySlug: $categorySlug
                        limit: $limit
                        skip: $skip
                        filters: $filters
                    ) {
                        total: totalNum
                        questions: data {
                            acceptanceRate: acRate
                            difficulty
                            QID: questionFrontendId
                            paidOnly: isPaidOnly
                            title
                            titleSlug
                            topicTags {
                                slug
                            }
                        }
                    }
                }
            """,
            "variables": {
                "categorySlug": "",
                "skip": 0,
                "limit": 1000,
                "filters": {}
            },
        }

        r = requests.post("https://leetcode.com/graphql", json=data).json()
        questionsList = r["data"]["problemsetQuestionList"]

        self.parse_question_list(questionsList)


    def parse_question_list(self, questionsData):
        self.totalNumQuestions = questionsData["total"]
        self.questionsList = questionsData["questions"]

    def get_questions(self):
        return self.questionsList


if __name__ == "__main__":
    scraper = Scrape_Questions()

    scraper.get_question_by_tag()

    questions = scraper.get_questions()
    print(questions[0]["acceptanceRate"])
    print("Almost")
    print("Done")
