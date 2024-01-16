# A 2 Q 1 Task 4: Extract the ‘diseases’, and ‘drugs’ entities in the ‘extracted_text.txt file’ separately using ‘en_core_sci_sm’.

import spacy
import scispacy
nlp = spacy.load('en_core_sci_sm')
with open('extracted_text.txt', 'r') as f:
    text = f.read()
doc = nlp(text)
diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
drugs = [ent.text for ent in doc.ents if ent.label_ == 'DRUG']
print(diseases)
print(drugs)
