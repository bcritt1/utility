def corpus_read():
    import os
    user = os.getenv('USER')
    corpusdir = '/scratch/users/{}/corpus/'.format(user)
    corpus = []
    for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

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