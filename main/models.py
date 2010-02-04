# -*- coding: utf-8 -*-
# main.models

from google.appengine.ext import db

class Village(db.Model):
    name        = db.TextProperty(required=True)
    description = db.TextProperty()
    capacity    = db.IntegerProperty(required=True)
    daytime     = db.FloatProperty(required=True)
    nighttime   = db.FloatProperty(required=True)
    playing     = db.BooleanProperty(default=False)
    created     = db.DateTimeProperty(auto_now_add=True)
