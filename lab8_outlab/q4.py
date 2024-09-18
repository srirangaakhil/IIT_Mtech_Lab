
from stackapi import StackAPI
import csv

SITE = StackAPI('stackoverflow')
input_tags = input()
input_tags = input_tags.lower()

tagged_ip = ";".join(input_tags.split())
tags = "_".join(input_tags.split())

questions = SITE.fetch('questions', tagged=tagged_ip)

lines = []
for item in questions["items"]:
	if("accepted_answer_id" in item.keys()):
		line = []
		line.append(str(item["question_id"]))
		line.append(tags)
		line.append(item["link"])
		line.append(str(item["tags"]))
		line.append(item["link"] + "#" + str(item["accepted_answer_id"]))
		lines.append(line)

with open(tags + '.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
writeFile.close()
