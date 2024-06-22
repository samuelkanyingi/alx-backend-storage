#!/usr/bin/env python3
""" 101-main """
def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    """
    pipeline = [
        {
            '$addFields': {
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))
