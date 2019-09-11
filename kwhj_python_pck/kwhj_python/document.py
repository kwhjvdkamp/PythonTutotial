# Import function to perform tokenization
from tokenizer import tokenize
from collections import Counter


# -------------------------------------------------------------------
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of Document
    def __init__(self, text, token_regex=r'[a-zA-z]+'):
        # Store text parameter to the text attribute
        self.text = text
        # Define attribute with the contents of the value param
        self.attribute = "Bla bla"
        self.tokens = self._tokenize()
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)
	
    # Non-public method to tally document's word counts
    def _count_words(self):
        # Use collections.Counter to count the document's tokens
        return Counter(self.tokens)

# ===================================================================

