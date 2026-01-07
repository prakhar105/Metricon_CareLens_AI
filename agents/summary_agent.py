import re
from transformers import T5Tokenizer, T5ForConditionalGeneration

class SummaryAgent:
    def __init__(self):
        model_name = "t5-small"
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def clean_text(self, text):
        """Remove duplicate 'solution:' tokens that T5 sometimes repeats."""
        text = re.sub(r'(solution:)\s*(solution:\s*)+', r'\1 ', text, flags=re.IGNORECASE)
        return text.strip()

    def fix_capitalization(self, text):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        final = []
        for s in sentences:
            s = s.strip()
            if not s:
                continue
            s = s[0].upper() + s[1:]
            final.append(s)
        return " ".join(final)

    def run(self, issue, solution):
        
        # --------------------------------------
        # CASE 1: No resolution provided
        # --------------------------------------
        if not solution.strip():
            unresolved_summary = (
                f"The customer reports: {issue.strip()} "
                "No resolution has been provided yet."
            )
            return {"summary": self.fix_capitalization(unresolved_summary)}

        # --------------------------------------
        # CASE 2: Normal summarization
        # --------------------------------------
        text = f"summarize: Issue: {issue}. Solution: {solution}."

        inputs = self.tokenizer.encode(
            text,
            return_tensors="pt",
            max_length=512,
            truncation=True
        )

        output_ids = self.model.generate(
            inputs,
            max_length=80,
            min_length=20,
            num_beams=4,
            length_penalty=2.0,
            early_stopping=True
        )

        raw = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        cleaned = self.clean_text(raw)
        final = self.fix_capitalization(cleaned)

        return {"summary": final}
