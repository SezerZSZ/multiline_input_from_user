import re

pattern = r'([#|$|%|*|&])(?P<name>[A-za-z]+)\1\=(?P<len>\d{2})\!\!(?P<geohashcode>[\w\W]+)'

# This is the hard part of the work... (multiline input)
L = []
input_elements = []
# Taking multiline input and storing it to input elements...
while True:
    n = input()
    if n == '':
        break
    else:
        L.append(list(map(str, n.split())))
        input_elements = [''.join(el) for el in L]
#  Iterating over the input strings in the list "input elements" for finding a match:
#  Giving every string to the pattern, to detect the matches and none matches...
for string in input_elements:
    matches = re.search(pattern, string)
    if matches == None:
        print('Nothing found!')

    else:
        name = matches.group('name')
        length = int(matches.group('len'))
        code = matches.group('geohashcode')
        if len(code) == length:
            #  Increasing each char with the length given above...
            geohashcode = ''.join([chr(ord(x) + length) for x in code])
            print(f"Coordinates found! {name} -> {geohashcode}")
            break
        elif len(code) > length:
            code = code[:length]
            #  Increasing each char with 16...
            geohashcode = ''.join([chr(ord(x) + length) for x in code])
            print(f"Coordinates found! {name} -> {geohashcode}")
            break


