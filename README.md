# 🏡 Metricon CareLens AI

**Metricon CareLens AI** is an AI-powered, multi-agent support co-pilot built to help customer support and operations teams **quickly understand, classify, and act on customer issues**.

The system leverages **Small Language Models (SLMs)**, **LangGraph-based orchestration**, and a clean **Streamlit UI** to deliver structured, explainable outputs such as **topic classification, sentiment analysis, issue summarization, and recommended next actions**.

This project is implemented as a **production-style Proof of Concept (POC)** inspired by real-world Metricon customer support workflows.

---

## ✨ Key Capabilities

- 📌 **Topic Classification** – Automatically categorizes customer issues (e.g., Warranty / Repairs, Billing, Delivery)
- 🙂 **Sentiment Analysis** – Detects customer sentiment with confidence scores
- 📝 **Issue & Resolution Summarization** – Generates professional summaries from raw issue text
- 🤖 **Orchestrated Recommendation** – Produces a final, actionable recommendation
- 🧠 **Agent-Based Architecture** – Modular, debuggable, and extensible
- 🔒 **Fully Open-Source & Local** – No paid APIs, runs locally on CPU/GPU

---

## 🧠 Architecture Overview

The system follows a **multi-agent pipeline**, orchestrated using **LangGraph**:

```
Customer Issue + Optional Resolution (Streamlit UI)
                │
                ▼
        [ Topic Detection Agent ]
                │
                ▼
       [ Sentiment Analysis Agent ]
                │
                ▼
     [ Issue & Resolution Summary Agent ]
                │
                ▼
        [ Orchestrator Agent ]
                │
                ▼
        Final Structured Recommendation
```

Each agent is responsible for a **single concern**, ensuring clarity, testability, and scalability.

---

## 🤖 AI Agents & Models

### 1️⃣ Topic Detection Agent
- **Model:** `all-MiniLM-L6-v2`
- **Library:** `sentence-transformers`
- **Method:** Semantic similarity against predefined support topics

---

### 2️⃣ Sentiment Analysis Agent
- **Model:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Library:** `transformers`
- **Output:** POSITIVE / NEGATIVE sentiment with confidence score

---

### 3️⃣ Issue & Resolution Summary Agent
- **Model:** `t5-small`
- **Library:** `transformers`
- **Features:**
  - Summarizes issue + resolution
  - Handles unresolved cases gracefully
  - Cleans and capitalizes output for professional reporting

---

### 4️⃣ Orchestrator Agent
- Aggregates outputs from all agents
- Produces a **final structured recommendation** containing:
  - Topic
  - Sentiment
  - Summary
  - Recommended next action

---

## 🖥️ User Interface

Built with **Streamlit**, the UI provides:

- Text input for **Customer Issue**
- Optional input for **Resolution**
- One-click AI execution
- Clear, sectioned AI outputs (as shown in the screenshot)

Designed for **internal support teams, demos, and stakeholder reviews**.

---

## 🧪 Example Workflow

**Customer Issue**
> "My ceiling has started cracking again even though it was repaired last month. This is getting really frustrating."

**Resolution (Optional)**
> "Inspector scheduled for tomorrow, escalated to warranty team."

**AI Output**
- **Topic:** Warranty / Repairs
- **Sentiment:** NEGATIVE (High confidence)
- **Summary:** Clean, professional issue summary
- **Final Recommendation:** Actionable next step for support team

---

## 🛠️ Tech Stack

- **Python:** 3.10
- **UI:** Streamlit
- **Agent Orchestration:** LangGraph
- **ML Framework:** PyTorch
- **NLP Models:** Hugging Face Transformers
- **Embeddings:** Sentence-Transformers (MiniLM)
- **Environment Management:** uv

---

## 📦 Dependency Versions

```txt
torch==2.1.2
transformers==4.33.3
sentence-transformers==2.2.2
huggingface-hub==0.17.3
langgraph==0.0.40
streamlit==1.30.0
```

---

## ▶️ Running the Application Locally

```bash
# Install dependencies
uv sync

# Run the Streamlit app
uv run streamlit run app.py
```

Open in browser:
```
http://localhost:8501
```

---

## 🚀 Future Enhancements

- SLA & urgency scoring
- Confidence-based escalation
- CRM / ticketing system integration
- Trend & sentiment analytics dashboard
- Multi-language support

---

## 💼 Why This Project Matters

This project demonstrates:

- Real-world application of **Small Language Models**
- Clean **agent-based system design**
- Deterministic orchestration using LangGraph
- Production-aware debugging and state management

It is designed to be easily extended into a **full-scale customer support intelligence system**.

---

## 👤 Author

**Prakhar Awasthi**  
AI / ML Engineer

---

## 📄 License

This project is provided as a **Proof of Concept (POC)** for educational and demonstration purposes.

