import pytest
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase

def test_get_preposition():

    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    assert get_preposition() in words

def test_get_prepositional_phrase():

    for i in range(4):
        assert len(get_prepositional_phrase(i + 1).split()) == 3

def test_get_determiner():
    
    words = ["a", "one", "the"]
    assert get_determiner(1) in words
    words = ["some", "many", "the"]
    assert get_determiner(2) in words

def test_get_noun():

    words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    assert get_noun(1) in words
    words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    assert get_noun(2) in words

def test_get_verb():
    
    words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    assert get_verb(1, "past") in words
    words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    assert get_verb(1, "present") in words
    words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    assert get_verb(2, "present") in words
    words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    assert get_verb(1, "future") in words

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])