#!/usr/bin/env python3
'''Task 14's module.
'''


def top_students(mongo_collection):
    '''Prints all students in a collection sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection containing student data.

    Returns:
        pymongo.command_cursor.CommandCursor: A cursor object containing the sorted student data.
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students