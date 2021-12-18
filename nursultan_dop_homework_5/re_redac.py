import re

file_mock = 'MOCK_DATA.txt'
reader_file = open(file_mock, mode='r', encoding='UTF-8')
txt_file = reader_file.read()


searcher_name = r"[A-Z][A-z]+\s[A-z]+\s[A-Z][A-z]+|" \
                r"[A-Z][A-z]+\s[A-Z][A-z]+|" \
                r"[A-Z][A-z]+\s\w'\D{2}\w+|" \
                r"[A-Z][A-z]+-[A-Z][A-z]+|" \
                r"[A-Z][A-z]+-[a-z]+\s\w+"
searcher_email = r'\w+@\S+'
searcher_extension = r'[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|' \
                     r"[A-Z]+[a-z]+\w+[.]+[a-z]+|" \
                     r"[A-Z]+[a-z]+[.]+[a-z]+[0-9]|" \
                     r"[A-Z]+[a-z]+[.]+[a-z]+|" \
                     r"[A-Z]+[.]+[a-z]+|" \
                     r"[A-Z]+[.]+[a-z]+[0-9]"
searcher_color = r'#\w+'

result_name = re.findall(searcher_name, txt_file)
result_email = re.findall(searcher_email, txt_file)
result_extension = re.findall(searcher_extension, txt_file)
result_color = re.findall(searcher_color, txt_file)

name1 = ''
email1 = ''
extension1 = ''
color1 = ''

for n in result_name:
    name1 += f'{n}\n'

for e in result_email:
    email1 += f'{e}\n'

for ex in result_extension:
    extension1 += f'{ex}\n'

for c in result_color:
    color1 += f'{c}\n'

class Txt_class:
    def __init__(self, name, email, extension, color):
        self.name = name
        self.name += f'\nTotal: {len(result_name)}'
        self.email = email
        self.email += f'\nTotal: {len(result_email)}'
        self.extension = extension
        self.extension += f'\nTotal: {len(result_extension)}'
        self.color = color
        self.color += f'\nTotal: {len(result_color)}'
    def __str__(self):
        return f'{self.name}\n' \
               f'{self.email}\n' \
               f'{self.extension}\n' \
               f'{self.color}\n'


test = Txt_class(name=name1,email=email1,extension=extension1,color=color1)

print(test)