import re
import random
import string
from BloomFilter import BloomFilter

regex = '(?<=[^a-zA-Z])?[A-Za-zА-Яа-я]+(?=[^a-zA-Z])?'
regex = re.compile(regex)
file_path = "crimeandpunishment.txt"
words = set()
with open(file_path, 'r', encoding='utf-8') as f:
    while line := f.readline():
        filtered = set(map(lambda s: s.lower(), re.findall(pattern=regex, string=line)))
        words.update(filtered)
words = list(words)

expected_elements = len(words)
probability = 0.15
bl_filter = BloomFilter(number_of_elements=expected_elements, probability=probability)

random_words = []
num_of_words_testes = 20000

[random_words.append(words[random.randint(0, len(words) - 10)]) for i in range(num_of_words_testes)]
[bl_filter.add(word) for word in words]


# with open('results_right.txt', 'w', encoding='utf-8') as f:
#     print('Number of elements  - %d;\tSize of the array - %d;\tprobability %f' % (len(words), len(bl_filter.arr), probability), file=f)
#     [print('For word %s the result is %s' % (word, str(bl_filter.lookup(word))), file=f) for word in random_words]

def get_rand_string(N):
    return ''.join(random.choices(string.ascii_lowercase, k=N))


with open('results_wrong.txt', 'w', encoding='utf-8') as f:
    print('Number of elements  - %d;\tSize of the array - %d;\tprobability %f' % (
        len(words), len(bl_filter.arr), probability), file=f)
    [print('For word %s the result is %s' % ('random', str(bl_filter.lookup(get_rand_string(random.randint(1, 14))))),
           file=f) for i in range(num_of_words_testes)]
