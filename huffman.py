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
        freq = {}
        sorted_freq = MinPQ()
        tree = MinPQ()
        for char in src:
            if char in freq.keys():
                freq[char] += 1
            else:
                freq.update({char:1})
        for char in src:
            print(freq[char],char)
            sorted_freq.insert(freq[char],char)
            print(sorted_freq.peek())
        i = 0
        while sorted_freq.size() > 2:
            tree.insert(i,sorted_freq.del_min())
            print(tree.peek())
            i += 1
    
    
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
        pass

    def source_text(self):
        """
        Returns the original source text.
        Returns:
            str: The original source text.
        """
        
        pass 

    def root(self):
        """
        Returns the root node of the Huffman tree.
        Returns:
            Node: The root node of the Huffman tree.
        """
        pass
    
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
        
        if node.char is not None:
            return {node.char: prefix}
        
        dictionary = {}
        dictionary.update(self._build_dictionary(node.left, prefix + '0'))
        dictionary.update(self._build_dictionary(node.right, prefix + '1'))
        return dictionary
def main():
    HuffmanEncoding("nhoj elttil pus")
if __name__ =="__main__":
    main()
    

# self.dictionary = self._build_dictionary
   
# 1. Count the frequency of each character
# 2. For each character, create a node that stores the character value and its frequency.
# 3. Push all of these nodes to a min-ordered priority queue
# 4. Pop off the two least frequent nodes and create a new node that has these two as left and right children and the combined frequency of both.
# 5. Push this new node to the priority queue.
# 6. If there is more than one node left on the queue, go back to step 4. Otherwise, the one remaining node is the root of our tree.