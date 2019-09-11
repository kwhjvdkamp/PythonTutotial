from collections import Counter

# import kwhj
from kwhj.kwhj_python import Document
# Tests on Document object
# -------------------------------------------------------------------
# blank document
def test_document_empty():
    doc = Document('')
    assert doc.tokens == []
    assert doc.word_counts == Counter()

# ------------------------------------------------------------------- 
# attribute
def test_document_tokens():
    doc = Document('a e i o u')
    assert doc.tokens == ['a', 'e', 'i', 'o', 'u']
    
# ------------------------------------------------------------------- 
# attribute
def test_document_word_counts():
    doc = Document('a e i o u')
    assert doc.word_counts == ['a', 'e', 'i', 'o', 'u']

    # doc = Document('This is a test, this is a test')
    # assert doc.word_counts == Counter({'is': 2, 'a': 2, 'test': 2, 'This': 1, 'this': 1})

# ===================================================================