import re
from BloomFilter import BloomFilter


def get_words(path):
    sett = list()
    regex = '(?<=[^a-zA-Z])?[A-Za-zА-Яа-я]+(?=[^a-zA-Z])?'
    regex = re.compile(regex)
    with open(path, 'r', encoding='utf-8') as f:
        while line := f.readline():
            filtered = list(map(lambda s: s.lower(), re.findall(pattern=regex, string=line)))
            # sett.update(filtered)
            sett += filtered
    return sett


file_path = "text.txt"
words = list(get_words(file_path))

expected_elements = len(words)
probability = 0.1
bl_filter = BloomFilter(number_of_elements=expected_elements, probability=probability)
[bl_filter.add(word) for word in words]

print(bl_filter.arr)
