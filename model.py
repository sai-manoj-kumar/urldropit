from google.appengine.ext import db


class YesNoFeedback(db.Model):
    url = db.TextProperty(required=True)
    message = db.TextProperty()
    success = db.BooleanProperty(required=True)
    timestamp = db.DateTimeProperty(auto_now_add=True)
