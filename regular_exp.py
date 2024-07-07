import re
text = "The agent's phone number is 408-555-1234. \
    Call the phone number soon!"
match = re.search('phone', text)
matches = re.findall('phone', text)
print(match.span(), len(matches))