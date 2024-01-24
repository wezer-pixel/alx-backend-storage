#!/usr/bin/env python3
'''Task 11's module.
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns the list of schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        topic (str): The topic to filter schools by.

    Returns:
        list: A list of school documents that match the specified topic.
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]