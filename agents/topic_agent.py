from sentence_transformers import SentenceTransformer, util

class TopicAgent:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.topics = [
            "Billing",
            "Delivery - Order Modification",
            "Account Management - Communication Preferences",
            "Technical Issue - WiFi",
            "Warranty / Repairs",
            "Order Status",
            "Refund Request",
            "Product Issue",
            "Customer Account Update",
            "Others",
        ]
        self.topic_embeddings = self.model.encode(self.topics, convert_to_tensor=True)

    def run(self, text):
        # 1️⃣ Handle empty input
        if not text or not text.strip():
            return {"topic": "Others"}

        try:
            # 2️⃣ Normal processing
            text_emb = self.model.encode(text, convert_to_tensor=True)
            scores = util.cos_sim(text_emb, self.topic_embeddings)[0]
            best_idx = scores.argmax().item()
            return {"topic": self.topics[best_idx]}

        except Exception as e:
            # 3️⃣ Safe fallback (prevents LangGraph crash)
            print("[TopicAgent ERROR]", e)
            return {"topic": "Others"}
