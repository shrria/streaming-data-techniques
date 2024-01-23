import random


class ReservoirSampling(object):
    def sample(self, k, data):
        """
        :type k: int
        :type data: List[int]
        :rtype: List[int]
        """

        reservoir = data[:k]
        data = data[k:]

        current_idx = k
        while data:
            new_item = data.pop(0)
            j = random.randint(0, current_idx)

            if j < k:
                reservoir[j] = new_item

            current_idx += 1

        print(f"result: {reservoir}")


if __name__ == "__main__":
    k = 50
    data = list(range(1, 100))

    sol = ReservoirSampling()
    sol.sample(k, data)
