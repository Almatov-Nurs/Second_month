import re

file_mock = 'MOCK_DATA.txt'
name = 'name_result.txt'
email = 'email_result.txt'
extension = 'extension_result.txt'
color = 'color_result.txt'

reader_file = open(file_mock, mode='r', encoding='UTF-8')
name_file = open(name, mode='w', encoding='UTF-8')
email_file = open(email, mode='w', encoding='UTF-8')
extension_file = open(extension, mode='w', encoding='UTF-8')
color_file = open(color, mode='w', encoding='UTF-8')

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

for n in result_name:
    print(n)
    name_file.write(n + '\n')
name_file.write(f'Total: {len(result_name)}')
print(len(result_name))

for e in result_email:
    # print(e)
    email_file.write(e + '\n')
email_file.write(f'Total: {len(result_email)}')
# print(len(result_email))

for ex in result_extension:
    # print(ex)
    extension_file.write(ex + '\n')
extension_file.write(f'Total: {len(result_extension)}')
# print(len(result_extension))

for c in result_color:
    # print(c)
    color_file.write(c + '\n')
color_file.write(f'Total: {len(result_color)}')
# print(len(result_color))
