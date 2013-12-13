import webapp2
import flattr
import mainpage
import credits
import yesnofeedback


app = webapp2.WSGIApplication(
    [
        ('/', mainpage.MainPage),
        ('/yesnofeedback', yesnofeedback.YesNoFeedback),
        ('/flattr', flattr.Flattr),
        ('/credits', credits.Credits)
    ], debug=True)

