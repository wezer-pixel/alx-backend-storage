#!/usr/bin/env python3
'''Task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to update.
        name (str): The name of the document to update.
        topics (list): The new list of topics to set.

    Returns:
        None
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )