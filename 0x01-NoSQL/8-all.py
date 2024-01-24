#!/usr/bin/env python3
'''Task 8's module.
'''


def list_all(mongo_collection):
    '''Lists all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.

    Returns:
        list: A list of all documents in the collection.
    '''
    return [doc for doc in mongo_collection.find()]