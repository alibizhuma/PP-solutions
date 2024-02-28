import re
#1
txt = str(input())
x = re.compile(r'ab*')
t = x.match(txt)
print("program that matches a string that has an a followed by zero or more b:", t.group())

#2
txt = str(input())
x = re.compile(r'ab{2,3}')
t = x.match(txt)
print("program that matches a string that has an a followed by two to three b:", t.group())

#3
txt = str(input())
x = re.compile(r'[a-z]+_[a-z]+')
t = x.match(txt)
print("program to find sequences of lowercase letters joined with a underscore:", t.group())

#4
txt = str(input())
x = re.compile(r'[A-Z][a-z]+')
t = x.match(txt)
print("program to find the sequences of one upper case letter followed by lower case letters:", t.group())

#5
txt = str(input())
x = re.compile(r'a.*b$')
t = x.match(txt)
print("program that matches a string that has an a followed by anything, ending in b:", t.group())

#6
txt = str(input())
x = txt.replace(' ', ':').replace(',',':').replace('.',':')
print("program to replace all occurrences of space, comma, or dot with a colon:", x)

#7
txt = str(input())
snake_case = txt.split('_')
camel_case = snake_case[0] + ''.join(word.capitalize() for word in snake_case[1::])
print("program to convert snake case string to camel case string:", camel_case)

#8
def split_at_uppercase(input_string):
    result = re.findall('[A-Z][^A-Z]*', input_string)
    return result
text = str(input())
print("program to split a string at uppercase letters:", split_at_uppercase(text))
 
#9
def capital_letters(input_string):
    res = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return res


cnt = str(input())

print("program to insert spaces between words starting with capital letters:", capital_letters(cnt))

#10
def camel_to_snake(camel_case):
    res = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case)
    return res.lower()

camel = str(input())
snake_case = camel_to_snake(camel)

print("program to convert a given camel case string to snake case:", snake_case)


