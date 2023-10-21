from maze.stack_frontier import StackFrontier


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise IndexError("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
