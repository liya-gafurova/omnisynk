from rake_nltk import  Rake

class RakeNLTKKeyWordExtraction():
    def __init__(self):
        self.rake = Rake()

    def get_keywords(self, text):
        self.rake.extract_keywords_from_text(text)
        return self.rake.get_ranked_phrases()

rake_keywors = RakeNLTKKeyWordExtraction()