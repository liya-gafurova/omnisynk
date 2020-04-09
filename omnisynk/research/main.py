from lib import *

idea_description = "System that could make multiple choice questions for student`s  testing and selftesting processes. \
                    System based on machine learning algorithms for question wording and distractor generation."
intend_for_money_using = "we intend to use money for research and development in natural language processing "



keywords = get_keywords_from_description(description= idea_description+' '+intend_for_money_using)
print(keywords)

res = send_request(keywords)
print(res.text)