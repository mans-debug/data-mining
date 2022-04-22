import numpy as np
# служебное, необходимо для перевода словаря в матрицу
order = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
}
# служебное, необходимо для вывода
order_list = ['A', 'B', 'C', 'D', 'E', 'F']
# Задание графа
adjacency_list = {
    'A': ['B'],
    'B': ['C'],
    'C': ['E'],
    'E': ['F', 'D'],
    'D': ['B'],
    'F': []
}

nodes_num = 6
A = np.zeros((nodes_num, nodes_num), dtype=np.float32)
# перевод из графа в матрицу
for k, v in adjacency_list.items():
    for node in v:
        A[order[k]][order[node]] = 1

At = np.transpose(A)
# создание векторов
auth = np.ones(nodes_num)[:, np.newaxis]
hub = np.ones(nodes_num)[:, np.newaxis]

# просто вывод
print('Iteration\t\t', 'NodeName', 'AuthorityPoints', '\t\tHubbingPoints', sep='\t   ')
for j in range(len(auth)):
    print("{3}\t\t\t\t\t\t\t{0}\t\t\t{1}\t\t\t{2:15}".format(order_list[j], float(auth[j]), float(hub[j]), -1))

print('\n\n')
k = 10 # кол-во итераций
for i in range(k):
    auth = At.dot(hub)  # умножение транс. матрицы на вектор
    auth /= max(auth)  # calculating constant
    hub = A.dot(auth)  # умножение матрицы на вектор
    hub /= max(hub)  # calculating constant
    # просто вывод
    for j in range(len(auth)):
        print("{3}\t\t\t\t\t\t\t{0}\t\t\t{1}\t\t\t{2:15}".format(order_list[j], float(auth[j]), float(hub[j]), i))

    print('\n\n')
