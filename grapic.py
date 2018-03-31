from collections import Counter

graph = {
    'A': ['B', 'E', 'G'],
    'B': ['C'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['C', 'F', 'G'],
    'F': [],
    'G': ['A']
}


# 获取出度
def get_out(node, graph):
    return len(graph[node]) if node in graph else 'Not in Graphic'


# 获取入度
def get_in(node, graph):
    L = [x for value in graph.values() for x in value]
    times = Counter(L).get(node)
    return times if times else 'Not in Graphic'


# 获取路径
def get_road(start,goals,graph):
    road = [start]
    solns = []
    find(road,goals,solns,graph)
    print(solns)


def find(road,goals,solns,graph):
    state = road[-1]
    if road[-1] is goals:
        solns.append(road)
    else:
        for node in graph[state]:
            if node not in road:
                # 这里不能使用road.append(node),因为find(road)是形参，局部变量，如果append将返回不了。
                find(road+[node],goals,solns,graph)


if __name__ == '__main__':
    print(get_out('A', graph))
    print(get_in('E', graph))
    print(get_road('A','C',graph))
