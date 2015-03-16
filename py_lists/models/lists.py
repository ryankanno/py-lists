#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import Integer, Unicode, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class List(object):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    description = Column(String(150))
    start_at = Column(DateTime)
    end_at = Column(DateTime)

    def __init__(self, code=None, description=None,
                 start_at=None, end_at=None):
        self.code = code
        self.description = description
        self.start_at = start_at
        self.end_at = end_at

    def __repr__(self):
        return u"<Action %r>".format(self.code)


class ListItem(object):
    __tablename__ = 'list_items'

    id = Column(Integer, primary_key=True)
    code = Column(String(3))
    description = Column(Unicode(600))
    is_critical = Column(Boolean())
    start_at = Column(DateTime)
    end_at = Column(DateTime)

    def __init__(self, code=None, description=None, is_critical=False,
                 start_at=None, end_at=None):
        self.code = code
        self.description = description
        self.is_critical = is_critical
        self.start_at = start_at
        self.end_at = end_at

    def __repr__(self):
        return u"<Violation %r>".format(self.code)


# vim: filetype=python
