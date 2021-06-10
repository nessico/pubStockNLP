import requests
import string
import json
import re


def cleanText(line):
  regex = re.compile('<a.*a>?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});|<br.*"quote">?>|</span.*<br>|<br>|<span.*;">|<span.*">|<span>|</span>')

  cleanText = re.sub(regex, '', line)
  return cleanText

response = requests.get('REDACTED') #REDACTED
# access JSON content
json_data = json.loads(response.text)

count = 0

# going thru each page 
for page in json_data:
  # going through each thread 
  for thread in page["threads"]:
    # getting threadID
    threadID = thread["no"]
    # getting comments from each thread 
    response = requests.get('REDACTED ' + str(threadID) + '.json') #Redacted
    # converting data 
    current_data = json.loads(response.text)

    # looking at each comment 
    for i in range(len(current_data["posts"])):
      try:
        # posting the comment and adding 1 if there one is found
        current_comment = current_data["posts"][i]["com"]
        print(cleanText(current_comment))
        # print(current_comment)
        count += 1
      except KeyError:
        print("")
		
# Perform Sentiment Analysis after getting results, reminder not to upload the sentiment analysis before it's perfected

print(count)


