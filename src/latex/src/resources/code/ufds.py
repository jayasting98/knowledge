from typing import Self


class Ufds:
    def __init__(self: Self, n: int) -> None:
        self._parents = list(range(n))
        self._ranks = [0 for _ in range(n)]

    def find(self: Self, x: int) -> int:
        if self._parents[x] != x:
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def union(self: Self, x: int, y: int) -> None:
        set_x = self.find(x)
        set_y = self.find(y)
        if set_x == set_y:
            return
        if self._ranks[set_y] > self._ranks[set_x]:
            self._parents[set_x] = set_y
        else:
            self._parents[set_y] = set_x
            if self._ranks[set_x] == self._ranks[set_y]:
                self._ranks[set_x] += 1
