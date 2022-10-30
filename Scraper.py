from scholarly import scholarly
import csv
import time
import json

JSON_FILE = 'data.json'
json_dict = {} # dictionary to store the data

if __name__ == "__main__":
    researcher_names=["xiaowei zhuang",
"long cai",
"dylan cable",
"fei chen",
"evan murray",
"vignesh shanmugam",
"simon zhang",
"michael diao"]
    for researcher_name in researcher_names:
        print("searching for researcher: ", researcher_name)
        search_query = scholarly.search_author(researcher_name)
        try:
            author = scholarly.fill(next(search_query))
            # scholarly.pprint(author)
            json_dict[researcher_name] = author
        except StopIteration:
            print("No results found for ", researcher_name)

    with open(JSON_FILE, 'w') as outfile:
        json.dump(json_dict, outfile)