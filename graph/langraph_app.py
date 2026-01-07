from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.topic_agent import TopicAgent
from agents.sentiment_agent import SentimentAgent
from agents.summary_agent import SummaryAgent
from agents.orchestrator import Orchestrator

DEBUG = True

# THIS IS THE CRITICAL FIX
class CustomerState(TypedDict, total=False):
    issue: str
    solution: str
    topic: dict
    sentiment: dict
    summary: dict
    final: dict


def build_graph():
    graph = StateGraph(CustomerState)

    topic_agent = TopicAgent()
    sentiment_agent = SentimentAgent()
    summary_agent = SummaryAgent()
    orchestrator = Orchestrator()

    def topic_node(state: CustomerState):
        out = topic_agent.run(state.get("issue", ""))
        if DEBUG: print("\nTOPIC OUTPUT:", out)
        return {"topic": out}

    def sentiment_node(state: CustomerState):
        out = sentiment_agent.run(state.get("issue", ""))
        if DEBUG: print("\nSENTIMENT OUTPUT:", out)
        return {"sentiment": out}

    def summary_node(state: CustomerState):
        out = summary_agent.run(state.get("issue", ""), state.get("solution", ""))
        if DEBUG: print("\nSUMMARY OUTPUT:", out)
        return {"summary": out}

    def orchestrator_node(state: CustomerState):
        if DEBUG: print("\nFULL STATE BEFORE ORCHESTRATOR:", state)

        topic = state["topic"]["topic"]
        sentiment = state["sentiment"]["sentiment"]
        summary = state["summary"]["summary"]

        out = orchestrator.run(topic, sentiment, summary)
        if DEBUG: print("\nORCHESTRATOR OUTPUT:", out)

        return {"final": out}

    # Add nodes WITHOUT 'outputs' argument
    graph.add_node("topic_node", topic_node)
    graph.add_node("sentiment_node", sentiment_node)
    graph.add_node("summary_node", summary_node)
    graph.add_node("orchestrator_node", orchestrator_node)

    graph.add_edge("topic_node", "sentiment_node")
    graph.add_edge("sentiment_node", "summary_node")
    graph.add_edge("summary_node", "orchestrator_node")
    graph.add_edge("orchestrator_node", END)

    graph.set_entry_point("topic_node")
    return graph.compile()
