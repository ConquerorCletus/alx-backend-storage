#!/usr/bin/env python3
"""
This module contains schools_by_topic function.
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    find by specific value
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
