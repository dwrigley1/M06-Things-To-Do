# Dakota Wrigley 
# Chapter 13 'Things To Do'

from datetime import date
now = date.today()

# 13.1 Write the current date as a string to the text file today.txt.
with open('today.txt', 'w') as f:
    f.write(str(now))

# 13.2 Read the text file today.txt into the string today_string.
with open('today.txt', 'r') as f:
    today_string = f.read()

# 13.3 Parse the date from today_string.
print(now)