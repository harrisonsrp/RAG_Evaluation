import json

# Path to your .jsonl file
file_path = 'test_data/test-set.jsonl'

# Open the .jsonl file and read line by line
with open(file_path, 'r', encoding='utf-8') as file:
    data = [json.loads(line) for line in file]
