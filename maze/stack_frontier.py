from node import Node


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self) -> Node:
        if self.empty():
            raise IndexError("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
