class Orchestrator:
    def run(self, topic, sentiment, summary):
        final_message = {
            "topic": topic,
            "sentiment": sentiment,
            "summary": summary,
            "action": f"This issue falls under '{topic}'. Sentiment is '{sentiment}'. Recommended next step is to proceed with: {summary}"
        }

        print("\nFINAL OUTPUT:", final_message)

        return {"final": final_message}