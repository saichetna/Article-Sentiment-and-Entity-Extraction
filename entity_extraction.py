import spacy

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract entities that are PERSON or ORG
    entities = []
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'ORG']:
            entities.append((ent.text, ent.label_))
    
    return entities
