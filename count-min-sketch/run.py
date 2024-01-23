import hashlib


class CountMinSketch(object):
    def __init__(self, hash_num, width):
        self.hash_num = hash_num
        self.width = width
        self.count_matrix = [[0 for _ in range(width)] for _ in range(hash_num)]

    def construct(self, data):
        """
        :type data: List[str]
        """

        from tqdm import tqdm

        len_data = len(data)
        with tqdm(total=len_data) as pbar:
            while data:
                new_item = data.pop(0)
                hash_results = self.hash(new_item)
                for i, value in enumerate(hash_results):
                    index = value % self.width
                    self.count_matrix[i][index] += 1
                pbar.update(1)

    def query(self, input):
        """
        :type input: str
        :rtype: int
        """
        hash_results = self.hash(input)
        min_count = float("inf")
        for i, value in enumerate(hash_results):
            index = value % self.width
            count = self.count_matrix[i][index]
            min_count = min(min_count, count)
        return min_count

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

    def __str__(self):
        close_line = "+---------+" + "---+" * self.width

        header = "|         |"
        for i in range(self.width):
            header += " {} |".format(i)

        row_template = "| hash {}  |" + " {} |" * self.width

        table_text = ""
        table_text += close_line + "\n"
        table_text += header + "\n"
        table_text += close_line + "\n"
        for i, row in enumerate(self.count_matrix):
            table_text += row_template.format(i + 1, *row) + "\n"
        table_text += close_line + "\n"

        return table_text


if __name__ == "__main__":
    hash_num = 5  ## depth = 5
    width = 28
    ## cardinality = 210000
    ## epsilon = 0.1
    ## delta = 0.01

    words = [
        "melody",
        "mosaic",
        "mountain",
        "river",
        "dragon",
        "pineapple",
        "trampoline",
        "sunset",
        "constellation",
        "twilight",
        "adventure",
        "chair",
        "kaleidoscope",
        "galaxy",
        "bicycle",
        "labyrinth",
        "whisper",
        "potion",
        "echo",
        "moonlight",
    ]

    ratios = [i * 1000 for i in range(1, len(words) + 1)]

    data = []
    for i in range(len(words)):
        data += [words[i]] * ratios[i]

    cms = CountMinSketch(hash_num, width)
    cms.construct(data)

    # print(cms)

    for word in words:
        print("{}: {}".format(word, cms.query(word)))
