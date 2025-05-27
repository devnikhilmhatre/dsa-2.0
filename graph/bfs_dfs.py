from dataclasses import dataclass, field
from typing import List, Dict, Any

nodes = 5
edges = [(0, 1), (1, 3), (1, 4), (3, 2), (2, 4)]

# edges = [(0, 1, 2), (1, 3, 4), (1, 4, 9), (3, 2, 1), (2, 4, 2)]


@dataclass
class Graph:
    node_count: int
    edges: List[tuple]
    directed: bool = False
    weighted: bool = False
    al: Dict[Any, list] = field(default_factory=dict)
    am: List[list] = field(default_factory=list)
    unique_nodes: set = field(default_factory=set)

    def __str__(self):
        return "\n".join(
            [
                "-" * 25,
                "\n".join([f"{i}: {j}" for i, j in self.al.items()]),
                "-" * 25,
                "\n".join([f"{i}" for i in self.am]),
                "-" * 25,
            ]
        )

    def generate_al(self):
        al: Dict[Any, list] = {}
        unique_nodes = set()
        for edge in self.edges:
            if self.weighted:
                node1, node2, weight = edge
            else:
                node1, node2 = edge
            unique_nodes.update([node1, node2])
            al.setdefault(node1, [])

            if self.weighted:
                al[node1].append((node2, weight))
            else:
                al[node1].append(node2)

            if not self.directed:
                al.setdefault(node2, [])

                if self.weighted:
                    al[node2].append((node1, weight))
                else:
                    al[node2].append(node1)

        self.al = al
        self.unique_nodes = unique_nodes

    def generate_am(self):
        am = []
        unique_nodes = set()
        for _ in range(self.node_count):
            am.append([(0, 0) if self.weighted else 0 for _ in range(self.node_count)])

        for edge in self.edges:
            if self.weighted:
                node1, node2, weight = edge
            else:
                node1, node2 = edge
            unique_nodes.update([node1, node2])
            if self.weighted:
                am[node1][node2] = (1, weight)
            else:
                am[node1][node2] = 1

            if not self.directed:
                if self.weighted:
                    am[node2][node1] = (1, weight)
                else:
                    am[node2][node1] = 1

        self.am = am

    def bfs_al(self, node, target=None):
        visited = set([node])
        path = [node]

        distance = {node: 0}

        stack, index = [node], 0

        while index < len(stack):
            current = stack[index]
            index += 1

            for neighbor in self.al.get(current) or []:
                if self.weighted:
                    neighbor, _ = neighbor

                if neighbor not in visited:
                    distance[neighbor] = 1 + distance[current]
                    visited.add(neighbor)
                    stack.append(neighbor)
                    path.append(neighbor)

                if neighbor == target:
                    return path, True, distance[target]

        return path, False, 0

    def bfs_am(self, node, target=None):
        visited = set([node])
        path = [node]

        distance = {node: 0}

        stack, index = [node], 0

        while index < len(stack):
            current = stack[index]
            index += 1

            for neighbor, is_connected in enumerate(self.am[current]):
                if self.weighted:
                    is_connected, _ = is_connected

                if is_connected == 1 and neighbor not in visited:
                    distance[neighbor] = 1 + distance[current]
                    visited.add(neighbor)
                    path.append(neighbor)
                    stack.append(neighbor)

                if is_connected == 1 and neighbor == target:
                    return path, True, distance[target]

        return path, False, 0

    def dfs_al(self, node, visited=None, path=None):
        visited = visited or set()
        path = path or []
        if node in visited:
            return path

        visited.add(node)
        path.append(node)

        for neighbor in self.al.get(node) or []:
            if self.weighted:
                neighbor, _ = neighbor

            path = self.dfs_al(neighbor, visited=visited, path=path)

        return path

    def dfs_am(self, node, visited=None, path=None):
        visited = visited or set()
        path = path or []
        if node in visited:
            return path

        visited.add(node)
        path.append(node)

        for neighbor, is_connected in enumerate(self.am[node]):
            if self.weighted:
                is_connected, _ = is_connected

            if is_connected == 1 and neighbor not in visited:
                path = self.dfs_am(neighbor, visited=visited, path=path)

        return path

    def dfs_al_2(self, node):
        visited = set([node])
        path = [node]
        stack = [node]

        while stack:
            current = stack.pop()
            for neighbor in reversed(self.al.get(current) or []):
                if self.weighted:
                    neighbor, _ = neighbor

                if neighbor in visited:
                    continue
                visited.add(neighbor)
                path.append(neighbor)
                stack.append(neighbor)
                # break
        return path

    def dfs_am_2(self, node):
        visited = set([node])
        path = [node]
        stack = [node]

        while stack:
            current = stack.pop()
            for neighbor, is_connected in reversed(list(enumerate(self.am[current]))):
                if self.weighted:
                    is_connected, _ = is_connected

                if is_connected != 1 or neighbor in visited:
                    continue
                visited.add(neighbor)
                path.append(neighbor)
                stack.append(neighbor)
                # break
        return path

    def dfs_al_cycle(self):
        visited = set()

        def is_cyclic(node, parent):
            # mark node visited
            visited.add(node)

            for neighbor in self.al.get(node) or []:
                if self.weighted:
                    neighbor, _ = neighbor
                if neighbor not in visited:
                    if is_cyclic(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
                # else
                # if neighbor in visited and parent and neighbor are same, don't do anything
            return False

        # go through all the nodes
        for node in self.unique_nodes:
            if node in visited:
                continue
            if is_cyclic(node, -1):
                return True

        return False

    def dfs_am_cycle(self):
        visited = set()

        def is_cyclic(node, parent):
            visited.add(node)

            for neighbor, is_connected in enumerate(self.am[node]):
                if self.weighted:
                    is_connected, _ = is_connected

                if is_connected != 1:
                    continue

                if neighbor not in visited:
                    if is_cyclic(neighbor, node):
                        return True
                elif parent != neighbor:
                    return True

            return False

        for node, _ in enumerate(self.am):
            if node in visited:
                continue
            if is_cyclic(node, -1):
                return True

        return False

    def bfs_al_cycle(self):
        visited = set()
        stack, index = [], 0

        for node in self.unique_nodes:
            if node in visited:
                continue
            visited.add(node)
            stack.append((node, -1))

            while index < len(stack):
                current, parent = stack[index]
                index += 1
                for neighbor in self.al.get(current) or []:
                    if self.weighted:
                        neighbor, _ = neighbor

                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, current))
                    elif neighbor != parent:
                        return True

        return False

    def bfs_am_cycle(self):
        visited = set()
        stack, index = [], 0

        for node, _ in enumerate(self.am):
            if node in visited:
                continue
            visited.add(node)
            stack.append((node, -1))

            while index < len(stack):
                current, parent = stack[index]
                index += 1
                for neighbor, is_connected in enumerate(self.am[current]):
                    if self.weighted:
                        is_connected, _ = is_connected
                    if is_connected != 1:
                        continue
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, current))
                    elif neighbor != parent:
                        return True

        return False

    def shorted_path_weighted(self, node, target):
        stack, index = [node], 0
        distance = {node: 0}

        while index < len(stack):
            current = stack[index]
            index += 1

            for neighbor, weight in self.al.get(current) or []:

                # print(
                #     f"neighbor: {neighbor} | ",
                #     f"old_weight: {distance.get(neighbor)} | ",
                #     f"new_weight: {weight + distance.get(current)}",
                # )
                if distance.get(neighbor) is not None and (
                    weight + distance.get(current) < distance.get(neighbor)
                ):
                    distance[neighbor] = weight + distance.get(current)
                    stack.append(neighbor)
                elif distance.get(neighbor) is None:
                    distance[neighbor] = weight + distance.get(current)
                    stack.append(neighbor)

        return distance.get(target)

    """
    1. find if all nodes are connected
    2. find set of connected component
    3. shorted path
    4. directed graph - cycle
    """


weighted = False
directed = False
# edges = [
#     ("a", "b", 1),
#     ("b", "d", 5),
#     ("d", "c", 1),
#     ("a", "c", 1),
#     ("c", "e", 1),
#     ("e", "d", 1),
# ]
# edges = [
#     (0, 1, 1),
#     (0, 2, 5),
#     (1, 2, 1),
#     (2, 3, 1),
#     (0, 3, 10),
# ]
g = Graph(nodes, edges, weighted=weighted, directed=directed)
g.generate_al()
# g.generate_am()
print(g)

print(g.bfs_al(0, 2))
# print("-" * 20)
# print(g.bfs_am(0, 4))
# print("-" * 20)
# print(g.dfs_al(0))
# print("-" * 20)
# print(g.dfs_am(0))
# print("-" * 20)
# print(g.dfs_al_2(0))
# print("-" * 20)
# print(g.dfs_am_2(0))
# print("-" * 20)
# print(g.dfs_al_cycle())
# print("-" * 20)
# print(g.dfs_am_cycle())
# print("-" * 20)
# print(g.bfs_al_cycle())
# print("-" * 20)
# print(g.bfs_am_cycle())
# print("-" * 20)
# print(g.shorted_path_weighted("a", "d"))
