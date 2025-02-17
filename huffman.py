from friendsbalt.acs import MinPQ

class HuffmanEncoding:
    def __init__(self, src=None, encoded_text=None, root=None):
        """
        Initializes a new Huffman Encoding. Either source text or encoded text and root must be provided.
        If source text is provided, it builds the Huffman tree and dictionary, and encodes the text.
        If encoded text and root are provided, it decodes the text.
        Args:
            src (str, optional): The source text to be encoded.
            encoded_text (str, optional): The encoded text to be decoded.
            root (Node, optional): The root node of the Huffman tree for decoding.
        """
        if src:
            self.freq = {}
            for char in src:
                if char in self.freq:
                    self.freq[char] += 1
                else:
                    self.freq[char] = 1
            
            self.sorted_freq = MinPQ()
            for char, freq in self.freq.items():
                self.sorted_freq.insert(freq, self.Node(freq, char))
            
            while self.sorted_freq.size() > 1:
                left = self.sorted_freq.del_min()
                right = self.sorted_freq.del_min()
                new_node = self.Node(left.freq + right.freq, left=left, right=right)
                self.sorted_freq.insert(new_node.freq, new_node)
            
            self.root = self.sorted_freq.del_min()
            self.dictionary = self._build_dictionary(self.root)
            self.encoded_text = ''.join(self.dictionary[char] for char in src)
            self.src = src
        elif encoded_text and root:
            self.encoded_text = encoded_text
            self.root = root
            self.dictionary = self._build_dictionary(self.root)
            self.src = self.decode(encoded_text, root)
        else:
            raise ValueError("Either source text or encoded text and root must be provided.")
    
    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right
        
        def is_leaf(self):
            return self.char is not None

    def encoding(self):
        """
        Returns the encoded text.
        Returns:
            str: The encoded text as a string of 0s and 1s.
        """
        return self.encoded_text

    def source_text(self):
        """
        Returns the original source text.
        Returns:
            str: The original source text.
        """
        return self.src 

    def root(self):
        """
        Returns the root node of the Huffman tree.
        Returns:
            Node: The root node of the Huffman tree.
        """
        return self.root
    
    def _build_dictionary(self, node=None, prefix=''):
        """
        Recursively builds a dictionary that maps characters to their corresponding
        Huffman codes based on the Huffman tree.
        Args:
            node (Node, optional): The current node in the Huffman tree. Defaults to None,
                                   which means the function will start from the root node.
            prefix (str, optional): The current Huffman code prefix. Defaults to an empty string.
        Returns:
            dict: A dictionary where keys are characters and values are their corresponding
                  Huffman codes.
        """
        if node is None:
            node = self.root
        
        if node.is_leaf():
            return {node.char: prefix}
        
        dictionary = {}
        dictionary.update(self._build_dictionary(node.left, prefix + '0'))
        dictionary.update(self._build_dictionary(node.right, prefix + '1'))
        return dictionary

    def decode(self, encoded_text, root):
        """
        Decodes the encoded text using the Huffman tree.
        Args:
            encoded_text (str): The encoded text to be decoded.
            root (Node): The root node of the Huffman tree.
        Returns:
            str: The decoded original text.
        """
        decoded_text = []
        node = root
        for bit in encoded_text:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            
            if node.is_leaf():
                decoded_text.append(node.char)
                node = root
        
        return ''.join(decoded_text)

def main():
    huffman = HuffmanEncoding("nhoj elttil pus")
    print("Encoded text:", huffman.encoding())
    print("Decoded text:", huffman.source_text())

if __name__ == "__main__":
    main()