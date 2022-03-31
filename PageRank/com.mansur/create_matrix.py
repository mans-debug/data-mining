import re
import config as conf
import requests
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from calculate_pagerank import pagerank

orig_graph: dict = {}
path = 'C:\\Users\\mansu\\PycharmProjects\PageRank\\resources\\app.properties'
config = conf.parse(path)
visited = set()
# каждой ссылке будет присвоен свой номер, чтобы идентифицировать ее в матрице
link_order: dict = {}


def write_graph_to_file(filepath, graph):
    with open(filepath, 'w', encoding='utf-8') as f:
        for parent, kids in graph.items():
            print(parent + ' :', kids, sep=', ', file=f)
            print('\n')


# отправляет get-запрос и возвращает html текст
def get_html(URL: str):
    try:
        req = requests.get(url=URL)
    except Exception:
        print("err with sending a request to link " + URL)
        return ''
    html_page = req.text
    return html_page


# извлекает ссылки из html страницы с помощью regex
def get_links(URL: str):
    if 'https' not in URL and 'http' not in URL:
        return False
    html_page = get_html(URL)
    pattern = config.get_property('filter.regex')
    links = re.findall(pattern, html_page)
    return set(map(lambda s: s[0:len(s) - 1] if s[-1] == '/' else s, links))


# вставляет одну ссылку в граф
def insert_in_graph(graph, from_link, inserted_link):
    if from_link not in graph:
        graph[from_link] = []
    graph[from_link].append(inserted_link)


# вставляет несколько ссылок по указанной ссылке
def fill_graph(links, origin):
    [insert_in_graph(orig_graph, origin, link) for link in links if link != origin]


# рекурсивно идет по сайтам, до указанной глубины.
# Берет ссылку, собирает с нее все ссылки, заполняет граф, рекурсия по ссылкам
def scrape(link, depth):
    global visited, counter, orig_graph
    visited.add(link)
    links = get_links(link)
    if not links:  # if link is invalid
        return
    print(link)

    fill_graph(links, link)

    if depth > -1:
        [scrape(i, depth - 1) for i in links if i not in visited]


def get_index(link: str, link_order: dict):
    if link not in link_order:
        link_order[link] = len(link_order)
    return link_order[link]


def clean_dict(graph: dict):
    global orig_graph
    for k, v in graph.items():
        new_list = list()
        [new_list.append(link) for link in v if link in graph]
        graph[k] = new_list
    orig_graph = graph
    return graph


def matrix_out_of_graph(graph: dict):
    global link_order
    graph = clean_dict(graph)
    size = (len(graph))
    matrix = np.zeros((size, size), dtype=np.double)
    for key, link_list in graph.items():
        column = get_index(key, link_order)
        value = 1 / len(link_list) if len(link_list) != 0 else 1 / size
        for link in link_list:
            row = get_index(link, link_order)
            if link != key:
                matrix[row][column] = value
    return matrix


# order - это карта в которой каждой ссылке сопоставлен номер
def draw_graph(graph, order, path, file_name):
    path = "C:\\Users\\mansu\\PycharmProjects\\PageRank\\resources\\" + file_name
    nodes = []
    for k, v in graph.items():
        [nodes.append((get_index(k, order), get_index(node, order))) for node in set(v)]
    G = nx.DiGraph(directed=True)
    G.add_edges_from(nodes)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos)

    plt.savefig(path + '.png', dpi=1000)
    plt.savefig(path + '.pdf', bbox_inches='tight')
    plt.show()


def write_matrix_to_file(file, matr):
    with open(file, 'w') as f:
        for x in matr:
            for y in x:
                print(y, end=" ", file=f)
            print(file=f)


def write_vector_to_file(file, vec):
    with open(file, 'w') as f:
        print('[', end='', file=f)
        [print(num, end='', file=f) for num in vector]
        print(']', file=f)


general_filepath = 'C:\\Users\\mansu\\PycharmProjects\\PageRank\\resources\\'
original_url = 'https://www.youtube.com/'
scrape(original_url, 2)
fp = general_filepath + 'graph.txt'
write_graph_to_file(fp, orig_graph)

fp = general_filepath + 'matrix.txt'
matrix: np = matrix_out_of_graph(orig_graph)
write_matrix_to_file(fp, matrix)
vector = pagerank(matrix)
fp = general_filepath + 'vector.txt'
write_vector_to_file(vec=vector, file=fp)

draw_graph(orig_graph, link_order, general_filepath, 'graph-plot')


def write_order_map(file, link_map):
    with open(file, 'w', encoding='utf-8') as f:
        [print(k + " - " + str(v), file=f) for k, v in link_map.items()]


fp = general_filepath + 'order_map.txt'
write_order_map(fp, link_order)
string = "Page with most links - %s\nHas %d links"
s = ''
max_amount = -1
for k,v in orig_graph.items():
    if len(v) > max_amount:
        s = k
print((string, s, max_amount))