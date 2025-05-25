nodes = 5
edges = [(0, 1), (0, 2), (1, 3), (3, 4), (4, 2)]

# Adjacency list
# Adjacency matrix


class Graph:
    def __init__(self, nodes: int, edges: list):
        self.nodes = nodes
        self.edges = edges

    def adjacency_matrix(self, directed=False):

        # create matrix
        am = []
        for _ in range(self.nodes):
            am.append([0 for _ in range(self.nodes)])

        for edge in self.edges:
            am[edge[0]][edge[1]] = 1

            if not directed:
                am[edge[1]][edge[0]] = 1

        return am

    def print_am(self, am: list):
        print("\n".join([" ".join([str(i) for i in arr]) for arr in am]))

    def adjacency_list(self, directed=False):
        al = {}

        for edge in self.edges:
            al.setdefault(edge[0], [])
            al[edge[0]].append(edge[1])

            if not directed:
                al.setdefault(edge[1], [])
                al[edge[1]].append(edge[0])

        return al

    def print_al(self, al: dict):
        print("\n".join([f"{key}: {value}" for key, value in al.items()]))

    def bfs_al(self, start_node, al: dict):
        queue = [start_node]
        index = 0
        visited = set([start_node])

        while index < len(queue):
            node = queue[index]

            for node in al.get(node):
                if node not in visited:
                    queue.append(node)
                    visited.add(node)

            # mark root visited
            index += 1

        return ", ".join([str(i) for i in queue])

    def bfs_am(self, row_index, am: list):
        queue = [row_index]
        queue_index = 0
        visited = set([row_index])

        while queue_index < len(queue):
            node = queue[queue_index]
            for i, elem in enumerate(am[node]):
                if elem == 1 and i not in visited:
                    queue.append(i)
                    visited.add(i)
            queue_index += 1
        return ", ".join([str(i) for i in queue])

    def dfs_al(self, start_node, al: dict, visited: set = None, res: list = None):
        visited = visited or set()
        if start_node in visited:
            return res
        visited.add(start_node)

        res = res or []
        res.append(start_node)

        nodes = al.get(start_node)
        for node in nodes:
            self.dfs_al(node, al, visited, res)

        return res

    def dfs_am(self, start_node, am: list, visited: set = None, res: list = None):
        visited = visited or set([])
        if start_node in visited:
            return res
        visited.add(start_node)

        res = res or []
        res.append(start_node)
        for index, elem in enumerate(am[start_node]):
            if elem == 1:
                self.dfs_am(index, am, visited, res)

        return res

    def dfs_al_iterative(self, start_node, al: dict):
        res = [start_node]
        visited = set([start_node])

        stack = [(0, al[start_node])]

        while stack:
            index, nodes = stack.pop()
            while index < len(nodes):
                if nodes[index] in visited:
                    index += 1
                    continue
                visited.add(nodes[index])
                res.append(nodes[index])
                stack.append((index + 1, nodes))
                stack.append((0, al[nodes[index]]))
                break

        return res

    def dfs_am_iterative(self, start_node, am: list):
        res = [start_node]
        stack = [(0, am[start_node])]
        visited = set([start_node])

        while stack:
            index, nodes = stack.pop
            while index > len(nodes):
                if nodes[index] == 1 and index not in visited:
                    visited.add(index)
                    res.append(index)
                    stack.append((index + 1, nodes))
                    stack.append((0, am[index]))
                    break

        return res

    def is_cycle_al(self, start_node, al: dict, visited: set, parent):
        visited.add(start_node)
        for neighbor in al[start_node]:
            if neighbor in visited and parent != neighbor:
                return True
            elif neighbor not in visited:
                return self.is_cycle_al(neighbor, al, visited, start_node)
            # else neighbor in visited and parent == neighbor
            # don't do anything
        return False

    def dfs_cycle_al(self, al: dict):
        visited = set()
        for node in al:
            if node in visited:
                continue
            res = self.is_cycle_al(node, al, visited, parent=-1)
            if res:
                return res

        return False

    def bfs_cycle_al(self, al: dict):
        visited = set()

        parent = -1
        for node in al:
            if node in visited:
                continue
            stack = [(node, -1)]
            index = 0
            visited.add(node)

            while index < len(stack):
                current, parent = stack[index]

                for neighbor in al[current]:
                    if neighbor in visited and parent != neighbor:
                        return True
                    elif neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, current))

                index += 1
        return False


def add_space(num: int = 2):
    for _ in range(num):
        print()


# cycle
# edges = [(0, 1), (1, 3), (1, 4), (3, 2), (2, 4)]
#
g = Graph(nodes, edges)
am = g.adjacency_matrix()
# g.print_am(am)
# add_space()
al = g.adjacency_list()
# g.print_al(al)
# add_space()

# for i in range(1):
#     print(i, g.bfs_al(i, al) == g.bfs_am(i, am))
#     print(g.bfs_al(i, al))


# add_space()

# for i in range(5):
#     print(i, g.dfs_al(i, al) == g.dfs_am(i, am))

# print(g.dfs_al(0, al) == g.dfs_al_iterative(0, al))
al = {0: [1, 2], 1: [0], 2: [0, 3], 3: [2]}


print("bfs_cycle_al", g.bfs_cycle_al(al))
