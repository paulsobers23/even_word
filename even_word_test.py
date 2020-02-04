import pytest
from even_word import even_word

@pytest.mark.skip()
def even_word_test():
    assert even_word('aaaa') == 0
    assert even_word('potato') == 2
    assert even_word('aabbbb') == 0
    assert even_word('aaabbbccc') == 3
