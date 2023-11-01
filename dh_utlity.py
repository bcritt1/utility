#output functions
def write_txt(data):
    with open('output.txt', 'w') as file:
    for d in {data}:
        file.write(d + '\n')

def write_json(data):
    import os
    user = os.getenv('USER')
    with open('/scratch/users/{}/outputs/data.json'.format(user), 'w', encoding='utf-8') as f:
        json.dump(str({data}), f, ensure_ascii=False, indent=4)

def df_to_csv(data):
    import os
    import pandas as pd
    user = os.getenv('USER')
    df = pd.DataFrame({data})
    df.to_csv('/scratch/users/{}/outputs/output.csv'.format(user)))

# inputs
#should this have path parameter? requires user input
def corpus_read():
    import os
    user = os.getenv('USER')
    corpusdir = '/scratch/users/{}/corpus/'.format(user)
    corpus = []
    for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

#pre-processing and nlp set-up

def enable_nltk():
    import ssl
    try:
        create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
        
def clean_text(data):
    import re
    sorpus = re.sub(r'(\\n[ \t]*)+', '', {data})

def spacy_nlp(corpus):
    nlp = spacy.load("en_core_web_sm")
# May need to increase length for large corpora. len(corpus) in python to find length.
nlp.max_length = 5000000
# Convert corpus to string to make spacy happy
sorpus = str({corpus})
# Perform nlp on sorpus
doc = nlp(sorpus)

def huggingface_nlp(corpus):
    # Import language models and pipeline elements
    from transformers import AutoTokenizer, AutoModelForTokenClassification
    tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
    model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")


    # Process text sample (from wikipedia)
    from transformers import pipeline
    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    entities = nlp({corpus})