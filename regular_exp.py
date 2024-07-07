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

# search for either cat or dog
re.search(r'cat|dog', 'The cat is here')
# . (period) is the wild card character
re.findall(r'.at', 'The cat in the hat went splat.')
# ^ (starts with), $ (ends with) search
# r[^\d] excludes all digits