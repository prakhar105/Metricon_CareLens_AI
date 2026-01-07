import streamlit as st
from graph.langraph_app import build_graph
import json

st.set_page_config(
    page_title="🏡 Metricon CareLens AI 👁️‍🗨️",
    page_icon="🏡",
    layout="wide"
)

graph = build_graph()

# --------------------------
# Sidebar
# --------------------------
with st.sidebar:
    st.title("🏡 Metricon CareLens AI 👁️‍🗨️")
    st.markdown("""
    ### 👋 Welcome!
    This AI tool helps support agents quickly classify, analyze,  
    and summarize customer issues using:
    
    - 🎯 **Topic Detection (MiniLM)**
    - 🙂 **Sentiment Analysis (DistilBERT)**
    - 📝 **Summarization (T5-Small)**
    - 🤖 **LangGraph Orchestration**
    
    ---
    **Tip:** Provide detailed issue text for best results.
    """)

# --------------------------
# Header
# --------------------------
st.markdown("""
# 🏡 Metricon CareLens AI 👁️‍🗨️  
### Powered by LangGraph + Transformers  
""")

st.markdown("Effortlessly classify, analyze, and summarize customer issues to assist support teams.")

# --------------------------
# Input boxes
# --------------------------
st.markdown("### 📝 Customer Issue")
issue = st.text_area("", height=120, placeholder="Describe the customer's issue...")

st.markdown("### 🛠️ Resolution (Optional)")
solution = st.text_area("", height=120, placeholder="Describe the resolution provided so far...")

run = st.button("🚀 Run AI", use_container_width=True)

# --------------------------
# Run AI
# --------------------------
if run:
    if not issue.strip():
        st.error("❌ Please enter a customer issue before running the model.")
        st.stop()

    with st.spinner("🔍 Running analysis... please wait"):
        try:
            state = {"issue": issue, "solution": solution}
            output = graph.invoke(state)

        except Exception as e:
            st.error(f"🔥 LangGraph error: {e}")
            st.stop()

    st.markdown("---")
    st.markdown("## 📊 AI Outputs")

    # ---------- Cards Layout ----------
    col1, col2 = st.columns([1, 1])

    # TOPIC
    with col1:
        st.markdown("### 📌 Topic Classification")
        topic = output.get("topic", {})
        st.json(topic)

    # SENTIMENT
    with col2:
        st.markdown("### 🙂 Sentiment Analysis")
        sent = output.get("sentiment", {})
        sentiment_label = sent.get("sentiment", "N/A")
        sentiment_conf = sent.get("confidence", 0)

        # UI badge styling
        if sentiment_label == "NEGATIVE":
            st.markdown(f"""
            <div style='padding:10px;border-radius:8px;background:#4a1f1f;color:#ff6b6b'>
                <b>Negative</b> — Confidence: {sentiment_conf:.2f}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='padding:10px;border-radius:8px;background:#1f3d1f;color:#65d674'>
                <b>Positive</b> — Confidence: {sentiment_conf:.2f}
            </div>
            """, unsafe_allow_html=True)

        st.json(sent)

    # SUMMARY
    st.markdown("### 📝 Issue Summary")
    summary = output.get("summary", {})
    st.json(summary)

    # ORCHESTRATOR FINAL ACTION
    if "final" in output:
        st.markdown("### 🤖 Final Orchestrated Recommendation")
        st.json(output["final"])

    st.markdown("---")

    # Download section
    result_json = json.dumps(output, indent=4)
    st.download_button(
        label="📥 Download Results as JSON",
        data=result_json,
        file_name="metricon_ai_output.json",
        mime="application/json"
    )
