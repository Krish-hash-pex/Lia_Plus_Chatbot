
import re
from typing import List, Dict

class SentimentAnalyzer:
    def __init__(self, pos_words=None, neg_words=None):
        # Small lexicon tuned for demo/assignment. Easily extensible.
        self.pos_words = set(pos_words or [
            "good","great","happy","love","excellent","better","satisfied","awesome",
            "fantastic","pleased","thanks","thank","positive","enjoy","enjoyed",
            "wonderful","nice","amazing","helpful"
        ])
        self.neg_words = set(neg_words or [
            "bad","terrible","sad","hate","poor","worse","disappointed","disappoints",
            "angry","upset","unhappy","problem","issue","annoy","annoyed","negative",
            "frustrated","frustrating","sorry","complain","complaint","delay","late"
        ])

    def _clean_and_tokenize(self, text: str) -> List[str]:
        text = text.lower()
        # remove punctuation except keep alphanumerics and spaces
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        tokens = [t for t in text.split() if t]
        return tokens

    def score(self, text: str) -> float:
        """Return a sentiment score: positive -> positive number, negative -> negative number."""
        tokens = self._clean_and_tokenize(text)
        pos = sum(1 for t in tokens if t in self.pos_words)
        neg = sum(1 for t in tokens if t in self.neg_words)
        denom = max(1, len(tokens))
        return (pos - neg) / denom

    def classify(self, text: str, threshold=0.02) -> str:
        s = self.score(text)
        if s > threshold:
            return "Positive"
        elif s < -threshold:
            return "Negative"
        else:
            return "Neutral"

    def analyze_statements(self, messages: List[str]) -> List[Dict]:
        """Return a list of dicts: {text, score, label} for each message."""
        return [{"text": m, "score": self.score(m), "label": self.classify(m)} for m in messages]

    def analyze_conversation(self, messages: List[str]) -> Dict:
        """Aggregate message scores and return overall_label and overall_score."""
        scores = [self.score(m) for m in messages]
        overall = (sum(scores) / len(scores)) if scores else 0.0
        if overall > 0.02:
            label = "Positive"
        elif overall < -0.02:
            label = "Negative"
        else:
            label = "Neutral"
        return {"overall_score": overall, "overall_label": label}
