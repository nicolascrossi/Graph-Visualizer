from typing import Tuple, Union

from pygame import Rect
from pygame.surface import Surface
import pygame.draw as draw


class Node:

    def __init__(self, dim: Tuple[int, int], weight, color: Tuple[int, int, int]):
        self.weight = weight

        # self.left: Tuple[Node | None, int] = (None, -1)
        # self.up: Tuple[Node | None, int] = (None, -1)
        # self.right: Tuple[Node | None, int] = (None, -1)
        # self.down: Tuple[Node | None, int] = (None, -1)

        # self.left: Node | None = None
        # self.up: Node | None = None
        # self.right: Node | None = None
        # self.down: Node | None = None

        self.left: Union[Node, None] = None
        self.up: Union[Node, None] = None
        self.right: Union[Node, None] = None
        self.down: Union[Node, None] = None

        self.dim = dim
        self.rect = Rect(0, 0, *dim)
        self.color = color

        self.pos = (0, 0)

    def __iter__(self):
        return NodeIter(self)

    def draw(self, screen: Surface, pos: Tuple[int, int]):
        self.rect = draw.rect(screen, self.color, (*pos, *self.dim))

    def inside(self, pos):
        return self.rect.collidepoint(*pos)

class NodeIter:

    def __init__(self, node: Node):
        self.node: Node = node
        self.index: int = 0

    def __next__(self):
        # match self.index:
        #     case 0:
        #         self.index += 1
        #         return self.node.left
        #     case 1:
        #         self.index += 1
        #         return self.node.up
        #     case 2:
        #         self.index += 1
        #         return self.node.right
        #     case 3:
        #         self.index += 1
        #         return self.node.down
        #     case _:
        #         raise StopIteration

        if self.index == 0:
            self.index += 1
            return self.node.left
        elif self.index == 1:
            self.index += 1
            return self.node.up
        elif self.index == 2:
            self.index += 1
            return self.node.right
        elif self.index == 3:
            self.index += 1
            return self.node.down
        else:
            raise StopIteration