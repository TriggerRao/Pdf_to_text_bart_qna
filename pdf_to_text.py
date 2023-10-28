import fitz
import spacy
import nlp_model


def pdf_to_text(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text


nlp_model = spacy.load("nlp_model")
pdf_path = "Satyam_CV.pdf"
text = pdf_to_text(pdf_path)
tx = " ".join(text.split("\n"))
print(tx)

doc = nlp_model(tx)
for ent in doc.ents:
    print(f"{ent.label_.upper():{30}}- {ent.text}")
