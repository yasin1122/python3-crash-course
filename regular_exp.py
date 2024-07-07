import re

text = "The agent's phone number is 408-555-1234. \
    Call the phone number soon!"
match = re.search('phone', text)
matches = re.findall('phone', text)
print(match.span(), len(matches))

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group(1))