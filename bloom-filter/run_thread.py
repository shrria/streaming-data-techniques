import time
import hashlib
from bitarray import bitarray
from concurrent.futures import ThreadPoolExecutor


# number of worker threads
WORKER_NUM = 4


class BloomFilter(object):
    def __init__(self, hash_num, bit_num):
        self.hash_num = hash_num
        self.bit_num = bit_num
        self.bit_array = bitarray(self.bit_num)
        self.bit_array.setall(0)

    def construct(self, data):
        """
        :type data: List[str]
        """

        def worker(chunk):
            for new_item in chunk:
                for value in self.hash(new_item):
                    index = value % self.bit_num
                    self.bit_array[index] = True

        # Split data into chunks
        chunk_size = len(data) // WORKER_NUM
        chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

        with ThreadPoolExecutor(max_workers=WORKER_NUM) as executor:
            executor.map(worker, chunks)

    def hash(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        hash_results = [None for _ in range(self.hash_num)]

        value = input
        for i in range(self.hash_num):
            value = self._hash(value)
            hash_results[i] = self._hex_to_int(value)

        return hash_results

    def _hex_to_int(self, hex_str):
        """
        :type hex_str: str
        :rtype: int
        """
        return int(hex_str, 16)

    def _hash(self, input):
        """
        :type input: str
        :rtype: str
        """
        hash_func = hashlib.sha256()
        hash_func.update(input.encode("utf-8"))
        return hash_func.hexdigest()

    def contains(self, input):
        """
        :type input: str
        :rtype: bool
        """
        hash_results = self.hash(input)
        for value in hash_results:
            index = value % self.bit_num
            if not self.bit_array[index]:
                return False

        return True


if __name__ == "__main__":
    hash_num = 22
    data = [str(item) for item in range(15, int(4e5))]

    size_of_raw_data = data.__sizeof__()

    sol = BloomFilter(hash_num, 13419081)

    start = time.time()
    sol.construct(data)
    end = time.time()
    print(f"construction time: {end - start}")

    print(f"size of raw data: {size_of_raw_data}")
    print(f"size of bit array: {sol.bit_array.__sizeof__()}")

    test_data_not_contains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in test_data_not_contains:
        assert not sol.contains(str(item))
