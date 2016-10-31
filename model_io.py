"""
Utilities for importing documents to run LDA on, and exporting the results.
"""
import csv


def load_documents(filename, text_field='text', url_field='url'):
    """
    Load documents from CSV.

    The CSV file should have a column header containing url and text.
    """
    with open(filename) as f:
        reader = csv.DictReader(f)
        raw_documents = list(reader)

    return [{'base_path': doc[url_field], 'text': doc[text_field]} for doc in raw_documents if doc[text_field] != '']


def export_topics(topics, filename):
    """
    Export the topics generated by gensim_engine. Each topic is
    a dict containing keys `topic_id` and `words`.
    """
    with open(filename, 'w') as topics_file:
        for topic in topics:
            topic_string = "{},{}\n".format(topic['topic_id'], topic['words'])
            topics_file.write(topic_string)


def export_tags(tagged_documents, filename):
    """
    Export the tags generated by the LDA model.
    """
    with open(filename, 'w') as tagged_documents_file:
        for tagged_document in tagged_documents:
            tag_string = '{},{}\n'.format(tagged_document['base_path'], tagged_document['tags'])
            tagged_documents_file.write(tag_string)