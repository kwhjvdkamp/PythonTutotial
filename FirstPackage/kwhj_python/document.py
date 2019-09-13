# Import function to perform tokenization
from tokenizer import tokenize
from collections import Counter


# -------------------------------------------------------------------
class Document:
    """Analyze text data from document

    :param text: text to analyze
    
    :ivar text: text originally passed to the instance on creation
    :ivar tokens: Parsed list of words from text
    :ivar word_counts: Counter containing counts of hashtags used in text
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

