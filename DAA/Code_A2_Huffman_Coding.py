# Experiment A2: Huffman Coding using a greedy algorithm
# Time complexity: O(n + k log k), where n is input length and k is
# the number of distinct characters (ignoring output-string construction details).

import heapq
from itertools import count


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


def build_huffman_tree(frequencies):
    if not frequencies:
        return None

    tie_breaker = count()
    heap = [(freq, next(tie_breaker), Node(char, freq))
            for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)
        parent = Node(None, freq1 + freq2, left, right)
        heapq.heappush(heap, (parent.freq, next(tie_breaker), parent))

    return heap[0][2]


def generate_codes(root):
    codes = {}

    def visit(node, prefix):
        if node is None:
            return
        if node.char is not None:
            # A single distinct character gets code "0", not an empty code.
            codes[node.char] = prefix or "0"
            return
        visit(node.left, prefix + "0")
        visit(node.right, prefix + "1")

    visit(root, "")
    return codes


def main():
    text = input("Enter text to encode: ")
    if not text:
        print("Please enter a non-empty string.")
        return

    frequencies = {}
    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1

    root = build_huffman_tree(frequencies)
    codes = generate_codes(root)
    encoded_text = "".join(codes[char] for char in text)

    print("\nCharacter | Frequency | Huffman Code")
    print("------------------------------------")
    for char, frequency in frequencies.items():
        display_char = repr(char)
        print(f"{display_char:>9} | {frequency:^9} | {codes[char]}")

    print("\nEncoded text:", encoded_text)


if __name__ == "__main__":
    main()
