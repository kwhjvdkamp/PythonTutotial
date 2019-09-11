from collections import Counter

from kwhj_python_pck import Document


# Test edge case of blank document
def test_document_empty():
    doc = Document('')
    assert doc.tokens == []
    assert doc.word_counts == Counter()


# Test tokens attribute on Document object
def test_document_tokens():
    doc = Document('a e i o u')
    assert doc.tokens == ['a', 'e', 'i', 'o', 'u']


# Test word_counts attribute on Document object
def test_document_word_counts():
    doc = Document('a e i o u')
    assert doc.word_counts == ['a', 'e', 'i', 'o', 'u']

    # doc = Document('This is a test, this is a test')
    # assert doc.word_counts == Counter({'is': 2, 'a': 2, 'test': 2, 'This': 1, 'this': 1})
