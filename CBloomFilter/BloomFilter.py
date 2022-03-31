import math
import hashlib

class BloomFilter:

    # num_hashes - number_of_hashes required
    # num_bytes - number of space required
    def __init__(self, number_of_elements: int, probability: float):
        self.num_bytes = int(-number_of_elements * math.log(probability) / math.log(2) ** 2) + 1
        self.num_hashes = int(self.num_bytes / number_of_elements * math.log(2)) + 1

        arr = []
        [arr.append(0) for i in range(self.num_bytes)]
        self.arr = arr

    @staticmethod
    def get_string_hash(s: str) -> int:
        return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16)

    def generate_hashes(self, s: str) -> list:
        h1 = self.get_string_hash(s)
        h2 = self.get_string_hash(str(h1))
        hashes = []
        for i in range(0, self.num_hashes):
            hashes.append(h1 + (i * h2))

        return hashes

    def add(self, s: str) -> None:
        hashes = self.generate_hashes(s)
        for i in hashes:
            self.arr[i % len(self.arr)] += 1

    def remove(self, s: str) -> None:
        hashes = self.generate_hashes(s)
        for i in hashes:
            index = i % len(self.arr)
            if self.arr[index] == 0:
                raise Exception(("there wasn't such word - %s", s))
            self.arr[index] -= 1

    def lookup(self, s: str) -> bool:
        for i in self.generate_hashes(s):
            if self.arr[i % len(self.arr)] <= 0:
                return False
        return True


