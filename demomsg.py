
import argparse
from sentiment import SentimentAnalyzer

class Chatbot:
    def __init__(self, tier2=False):
        self.history = []  # list of tuples (speaker, text)
        self.tier2 = tier2
        self.analyzer = SentimentAnalyzer()

    def add_user(self, text: str):
        self.history.append(("User", text))

    def add_bot(self, text: str):
        self.history.append(("Bot", text))

    def bot_reply(self, user_text: str) -> str:
        # Very simple response logic: if user mentions a problem, apologize and ask for more.
        low = user_text.lower()
        if any(w in low for w in ["help","problem","issue","complain","error","delay","late"]):
            return "I'm sorry you're having issues — can you describe the problem in one sentence?"
        if any(w in low for w in ["thanks","thank you","thx"]):
            return "You're welcome! Anything else I can help with?"
        # Default neutral reply
        return "Thanks for telling me. Could you say more or ask a specific question?"

    def interact_once(self, user_text: str) -> str:
        self.add_user(user_text)
        bot_text = self.bot_reply(user_text)
        self.add_bot(bot_text)
        return bot_text

    def final_sentiment_report(self):
        user_messages = [t for s,t in self.history if s == "User"]
        conv_analysis = self.analyzer.analyze_conversation(user_messages)
        print("\n--- Final Sentiment Report (Conversation-level) ---")
        print(f"Overall conversation sentiment: {conv_analysis['overall_label']} (score={conv_analysis['overall_score']:.3f})\n")
        if self.tier2:
            print("--- Statement-level sentiment ---")
            results = self.analyzer.analyze_statements(user_messages)
            for r in results:
                print(f"→ \"{r['text']}\" → {r['label']} (score={r['score']:.3f})")
            # simple mood trend summary (first vs last)
            scores = [r['score'] for r in results]
            if len(scores) >= 2:
                shift = scores[-1] - scores[0]
                if shift > 0.02:
                    trend = "Improving mood across the conversation"
                elif shift < -0.02:
                    trend = "Declining mood across the conversation"
                else:
                    trend = "No significant mood shift detected"
                print(f"\nMood trend summary: {trend}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chatbot with Sentiment Analysis (demo)')
    parser.add_argument('--tier2', action='store_true', help='Enable statement-level sentiment (Tier 2)')
    args = parser.parse_args()

    # Demo conversation (you can replace these with interactive input if you like)
    demo_messages = [
        "Your service disappoints me",
        "I waited too long and support never replied",
        "Last experience was better",
        "Thanks for listening"
    ]

    bot = Chatbot(tier2=args.tier2)
    for m in demo_messages:
        print("User:", m)
        reply = bot.interact_once(m)
        print("Bot: ", reply, "\n")

    bot.final_sentiment_report()
