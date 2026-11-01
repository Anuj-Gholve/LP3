# Code-A2 (Huffman Coding)

import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison function for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman Tree
def build_huffman_tree(char_freq):
    heap = [Node(ch, freq) for ch, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pick two smallest nodes (greedy choice)
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge them into a new node
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


# Function to generate Huffman codes
def generate_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes


# Main program
text = input("Enter text to encode: ")

# Step 1: Calculate frequency of each character
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: Build Huffman Tree using greedy approach
root = build_huffman_tree(freq)

# Step 3: Generate Huffman Codes
codes = generate_codes(root)

# Step 4: Encode the text
encoded_text = "".join(codes[ch] for ch in text)

# Step 5: Display results
print("\nCharacter | Frequency | Huffman Code")
print("------------------------------------")
for ch in freq:
    print(f"    {ch!r}     |     {freq[ch]}      |    {codes[ch]}")

print("\nEncoded Text:", encoded_text)

# SAMPLE OUTPUT
"""
Enter text to encode: lord kska git

Character | Frequency | Huffman Code
------------------------------------
    'l'     |     1      |    1100
    'o'     |     1      |    1101
    'r'     |     1      |    001
    'd'     |     1      |    1010
    ' '     |     2      |    011
    'k'     |     2      |    100
    's'     |     1      |    000
    'a'     |     1      |    010
    'g'     |     1      |    1011
    'i'     |     1      |    1111
    't'     |     1      |    1110

Encoded Text: 110011010011010011100000100010011101111111110
"""
