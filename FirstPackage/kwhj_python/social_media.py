from collections import Counter

# parent class
from .document import Document

# -------------------------------------------------------------------

# private function
def filter_word_counts(word_counts, first_char):
    """Filter Document.word_counts by the first character of the word
    
    :param word_counts: the word_counts attribute of a Document class instance
    :param first_char: only keep word counts that start with this character
    
    >>> # How to filter to only words that start with 'A'
    >>> filter_word_counts(document.word_counts, 'A')
    """
    return Counter({k: v for k, v in word_counts.items() if k[0] == first_char})

# ===================================================================

# inherited class
class SocialMedia(Document):
    """Analyze text data from social media
    
    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        Document.__init__(self, text)
        
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')

# ===================================================================



