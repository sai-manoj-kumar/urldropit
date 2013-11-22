from google.appengine.ext import db


class YesNoFeedback(db.Model):
    url = db.StringProperty(required=True)
    filename = db.StringProperty()
    success = db.BooleanProperty(required=True)
    timestamp = db.DateTimeProperty(auto_now_add=True)
