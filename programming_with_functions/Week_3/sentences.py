import random

def main():

    print("The point of this program is to have the computer make random sentences and output them to you.")
    print()
    
    print(get_sentence(1, "past"))
    print(get_sentence(1, "present"))
    print(get_sentence(1, "future"))
    print(get_sentence(2, "past"))
    print(get_sentence(2, "present"))
    print(get_sentence(2, "future"))


def get_sentence(quantity, tense):
    
    sentence = f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)}"

    return sentence

def get_preposition():

    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):

    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

    return prepositional_phrase

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word

def get_verb(quantity, tense):

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    word = random.choice(words)
    return word


if __name__ == "__main__":
    main()