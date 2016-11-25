# python3
from collections import deque
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
                # f = open('case.txt')
                # self.n = int(f.readline())
                # self.parent = list(map(int, f.readline().split()))

        def compute_height_naive(self):
                maxHeight = 0
                memo = {}
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                            if i in memo:
                                height += memo[i]
                                break
                            height += 1
                            i = self.parent[i]

                        memo[vertex] = height
                        maxHeight = max(maxHeight, height);
                return maxHeight;

        # def compute_height(self):
        #     root_index = self.parent.index(-1)
        #     visited = []
        #     level = 0
        #     Q = deque()
        #     Q.append(root_index)
        #     while len(Q) != 0:
        #         current_index = Q.pop()
        #         if not current_index in visited:
        #             print('a' + str(current_index))
        #             # visited.append(current_index)
        #             # enqueuing child nodes of the current index
        #             for i, node in enumerate(self.parent):
        #                 if node == root_index and not i in visited:
        #                     print(i)
        #                     Q.append(i)
        #             visited.append(current_index)
        #             #changing level for the next iteration
        #             root_index = current_index
        #             level += 1
        #     return level

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height_naive())

threading.Thread(target=main).start()
