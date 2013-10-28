import re

phone_numbers = [
                '4559953958',
                'hello (555)995 - 3958',
                '(555) 995 - 3958 called me',
                'I want to reach (555) 995 3958',
                'phone number:555 995-3958',
                'call 555 995 - 3958',
                'As seen on T.V.! 555 995 3958',
                'Do Not Call List: 555-995-3958',
                '555 - 995 - 3958 :)',
                '(123)'
                ]

print r'\w = [a-zA-Z0-9_]'
print r'\d = [0-9]'
print r'\s = [ \t\n\r\f\v]'
print 'uppercase to negate\n'

for number in phone_numbers:
    num = re.findall(r"""[(]?[0-3|5-9]\d{2}[)]  # matches digits with option parenthesis, excludes numbers that start with 4
                        ?\s?-?\s?\              # optionally matches spaces and hyphens
                        d{3}                    # matches 3 digits
                        \s?[-]?\s?              # optionally matches spaces and hyphens
                        \d{4}                   # matches 4 digits
                        """, number, flags=re.VERBOSE)
    if num:
        print 'MATCHED!',num
    else:
        print 'NOT MATCHED:',number

print """[(]?[0-3|5-9]\d{2}[)]  # matches digits with option parenthesis,
?\s?-?\s?\              # optionally matches spaces and hyphens
d{3}                    # matches 3 digits
\s?[-]?\s?              # optionally matches spaces and hyphens
\d{4}                   # matches 4 digits
"""
