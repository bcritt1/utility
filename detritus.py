# I think enough parameters are being set here that we should do this in individual modules
def huggingface_nlp(corpus):
    # Import language models and pipeline elements
    from transformers import AutoTokenizer, AutoModelForTokenClassification
    tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
    model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")

    # Process text sample (from wikipedia)
    from transformers import pipeline
    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    entities = nlp({corpus})