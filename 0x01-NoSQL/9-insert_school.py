#!/usr/bin/env python3
'''Task 9's module.
'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
        **kwargs: The key-value pairs representing the fields and values of the document to be inserted.

    Returns:
        str: The inserted document's ID.

    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id