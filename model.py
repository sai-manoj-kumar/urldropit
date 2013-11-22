from google.appengine.ext import db


class YesNoFeedback(db.Model):
    url = db.StringProperty(required=True)
    success = db.BooleanProperty(required=True)
