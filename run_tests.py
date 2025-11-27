from sentiment import SentimentAnalyzer

def test_basic():
    a = SentimentAnalyzer()
    assert a.classify("I love this") == "Positive"
    assert a.classify("I hate this") == "Negative"
    assert a.classify("It is a book") == "Neutral"

if __name__ == '__main__':
    test_basic()
    print("Basic tests passed.")
