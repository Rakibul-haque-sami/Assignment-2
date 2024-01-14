import spacy
from transformers import BertTokenizer, BertForTokenClassification
import torch

# Load scispaCy model
nlp_sci = spacy.load("en_core_sci_sm")  # or "en_ner_bc5cdr_md"

# Load BioBERT model
tokenizer = BertTokenizer.from_pretrained("dmis-lab/biobert-v1.1", do_lower_case=False)
model = BertForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")

# Example text
text = "Hypertension."

# Process text with scispaCy
doc_sci = nlp_sci(text)

# Extract biomedical entities with BioBERT
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predictions = torch.argmax(outputs.logits, dim=2)

# Print entities detected by scispaCy
for ent in doc_sci.ents:
    print(f"scispaCy Entity: {ent.text} - Label: {ent.label_}")

# Print biomedical entities detected by BioBERT
bio_entities = [tokenizer.convert_ids_to_tokens(pred) for pred in predictions[0].numpy()]
for word, bio_entity in zip(tokenizer.tokenize(text), bio_entities[1:-1]):
    print(f"Word: {word} - BioBERT Entity: {bio_entity}")
