from pymystem3 import Mystem
m = Mystem()
resources = 'C:/Users/mansu/IdeaProjects/KeywordFinder/src/main/resources'
read = open(resources + '/fromLinks/clean-words.txt', 'r', encoding='utf-8')
write = open(resources + '/normalized/normalized.txt', 'w', encoding='utf-8')
for line in read.readlines():
    lemmas = m.lemmatize(line)
    write.write(''.join(lemmas))