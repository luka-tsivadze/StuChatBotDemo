import json

with open('data/raw data/tagged-handwriten-qa.json', 'r', encoding='utf-8') as file:
    qa_data = json.load(file)

contents = []

for dict in qa_data:
    contents.extend(dict["content"])

with open('data/qa-dataset/handwriten-qa.json', 'w', encoding='utf-8') as json_file:
    json.dump(contents, json_file, ensure_ascii=False, indent=4)