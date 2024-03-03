import random


class RandomizedSet():

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)

        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            ind = self.numMap[val]
            last_val = self.numList[-1]
            self.numList[ind] = last_val
            self.numList.pop()
            self.numMap[last_val] = ind
            del self.numMap[val]

        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)
