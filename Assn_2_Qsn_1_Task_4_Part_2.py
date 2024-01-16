# A 2 Qsn 1 Task 4 P 2: Extract the ‘diseases’, and ‘drugs’ entities in the ‘extracted_text.txt' file separately using  biobert.

import biobert_ner as b_ner
import json
# Load the BioBERT NER model
model = b_ner.load_model('biobert_v1.1_pubmed')
# Read the extracted text
with open('extracted_text.txt', 'r') as f:
    text = f.read()
# Extract the entities
entities = model.predict(text)
# Print the diseases and drugs entities
print('Diseases:')
for entity in entities['diseases']:
    print(entity)
print('\nDrugs:')
for entity in entities['drugs']:
    print(entity)
