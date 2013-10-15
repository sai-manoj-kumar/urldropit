import webapp2
import URLDropit
import credits


app = webapp2.WSGIApplication(
    [
        ('/', URLDropit.URLDropit),
        ('/credits', credits.Credits)
    ], debug=True)

