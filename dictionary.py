import json

vietnameseDictionary = {}
with open('words.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        
        if line:
            item = json.loads(line)
            vietnameseDictionary[item['text']] = item['source']