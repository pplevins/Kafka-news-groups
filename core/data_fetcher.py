import json

from sklearn.datasets import fetch_20newsgroups


class DataFetcher:
    def __init__(self):
        interesting, not_interesting = DataFetcher.fetch_data_from_sklearn()
        self.data = {"interesting": interesting, "not_interesting": not_interesting}
        interesting_categories = ["alt.atheism",
                                  "comp.graphics",
                                  "comp.os.ms-windows.misc",
                                  "comp.sys.ibm.pc.hardware",
                                  "comp.sys.mac.hardware",
                                  "comp.windows.x",
                                  "misc.forsale",
                                  "rec.autos",
                                  "rec.motorcycles",
                                  "rec.sport.baseball"]
        not_interesting_categories = ["rec.sport.hockey",
                                      "sci.crypt",
                                      "sci.electronics",
                                      "sci.med",
                                      "sci.space",
                                      "soc.religion.christian",
                                      "talk.politics.guns",
                                      "talk.politics.mideast",
                                      "talk.politics.misc",
                                      "talk.religion.misc"]
        self.categories = {"interesting": interesting_categories, "not_interesting": not_interesting_categories}

    @staticmethod
    def fetch_data_from_sklearn():
        interesting_categories = ["alt.atheism",
                                  "comp.graphics",
                                  "comp.os.ms-windows.misc",
                                  "comp.sys.ibm.pc.hardware",
                                  "comp.sys.mac.hardware",
                                  "comp.windows.x",
                                  "misc.forsale",
                                  "rec.autos",
                                  "rec.motorcycles",
                                  "rec.sport.baseball"]
        not_interesting_categories = ["rec.sport.hockey",
                                      "sci.crypt",
                                      "sci.electronics",
                                      "sci.med",
                                      "sci.space",
                                      "soc.religion.christian",
                                      "talk.politics.guns",
                                      "talk.politics.mideast",
                                      "talk.politics.misc",
                                      "talk.religion.misc"]
        newsgroups_interesting = fetch_20newsgroups(subset="all", categories=interesting_categories)
        newsgroups_not_interesting = fetch_20newsgroups(subset="all", categories=not_interesting_categories)

        interesting = []
        for i in range(len(newsgroups_interesting.data)):
            subject = {
                "category": newsgroups_interesting.target_names[newsgroups_interesting.target[i]],
                "text": newsgroups_interesting.data[i]
            }
            interesting.append(subject)
        not_interesting = []
        for i in range(len(newsgroups_not_interesting.data)):
            subject = {
                "category": newsgroups_not_interesting.target_names[newsgroups_not_interesting.target[i]],
                "text": newsgroups_not_interesting.data[i]
            }
            not_interesting.append(subject)

        return interesting, not_interesting

    @staticmethod
    def fetch_data_from_json():
        with open("data/newsgroups_interesting (3).json", "r", encoding="utf-8") as json_file:
            newsgroups_interesting = json.load(json_file)

        with open("data/newsgroups_not_interesting (3).json", "r", encoding="utf-8") as json_file:
            newsgroups_not_interesting = json.load(json_file)

        return newsgroups_interesting, newsgroups_not_interesting
