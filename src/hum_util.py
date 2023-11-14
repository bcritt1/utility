#!/usr/bin/env python

"""Utilities for Humanities projects on the Sherlock cluster."""
# light imports ONLY; heavy imports inside modules
import os
import pandas as pd
import csv
import json
import re

__authors__ = "Brad Rittenhouse and Annie Lamar"

"""DATA WRANGLING FUNCTIONS"""


def list_to_text(data, output_filename='output.txt', one_line=False):
    """Writes contents of a Python list to a .txt file.
    Note that this file will overwrite any file with the same filename.
    The default filename is 'output.txt'.

    :param output_filename: the name of the output file
    :param data: the list of text data to write to a .txt file
    :param one_line: if True, write all contents to a single line in the .txt file
    """
    with open(output_filename, 'w+') as file:
        for datum in data:
            if one_line:
                file.write(datum)
            else:
                file.write(datum + '\n')


def write_json(data, output_filename="default"):
    """Writes contents of a Python dictionary to a .json file.
    Note that this file will overwrite any file with the same filename.
    The default filename is 'data.JSON' in the current user's outputs folder.

    :param data: the dictionary to write to a JSON file
    :param output_filename: the name of the output file
    """
    if output_filename == "default":
        user = os.getenv('USER')
        output_filename = '/scratch/users/{}/outputs/data.json'.format(user)
    with open(output_filename, 'w+', encoding='utf-8') as file:
        json.dump(str({data}), file, ensure_ascii=False, indent=4)


def list_to_csv(data_list, output_filename="default", header=None):
    """Writes contents of a list to a .csv file, with optional added headings.
    Note that this file will overwrite any file with the same filename.
    The default filename is 'output.csv' in the current user's outputs folder.

    :param data_list: the list of data to save to a CSV
    :param output_filename: the name of the output .csv file
    :param header: the column headings (optional)
    """
    if header is None:
        header = list(range(0, len(data_list[0])))
    if output_filename == "default":
        user = os.getenv('USER')
        output_filename = '/scratch/users/{}/outputs/output.csv'.format(user)
    dataframe = pd.DataFrame(data_list, columns=header)
    dataframe.to_csv(output_filename)


def corpus_directory_to_dataframe(corpus_directory, scope='file'):
    """
    Returns a DataFrame with all corpus text and corresponding filenames.

    :param corpus_directory: directory that contains all corpus files
    :param scope: options are 'file' or 'lines'; level at which to label and return text
    :return: a DataFrame with all text and the file it came from
    """
    corpus_lists = []
    for file in os.listdir(corpus_directory):
        with open(corpus_directory + "/" + file, errors='ignore', encoding='utf8') as current_file:
            if scope == 'file':
                corpus_lists.append([current_file.read(), str(corpus_directory + "/" + file)])
            elif 'line' in scope:
                for line in current_file.readlines():
                    corpus_lists.append([line, str(corpus_directory + "/" + file)])
    corpus = pd.DataFrame(corpus_lists, columns=['text', 'file'])
    return corpus


def corpus_dataframe_to_list(corpus_dataframe):
    """Converts corpus DataFrame to a list of texts or strings.
    Requires a DataFrame with a column named 'text'."""
    return corpus_dataframe['text'].to_list()


"""MACHINE LEARNING INIT FUNCTIONS"""


def enable_nltk():
    import ssl
    try:
        create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


def remove_text_breaks(data):
    sorpus = re.sub(r'(\\n[ \t]*)+', '', {data})


def spacy_nlp(corpus):
    nlp = spacy.load("en_core_web_sm")


    # May need to increase length for large corpora. len(corpus) in python to find length.
    nlp.max_length = 5000000
    # Convert corpus to string to make spacy happy
    sorpus = str({corpus})
    # Perform nlp on sorpus
    doc = nlp(sorpus)



