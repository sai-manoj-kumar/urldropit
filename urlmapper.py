import webapp2
import flattr
import mainpage
import credits
import download
import yesnofeedback


app = webapp2.WSGIApplication(
    [
        ('/', mainpage.MainPage),
        ('/download', download.DownloadPage),
        ('/yesnofeedback', yesnofeedback.YesNoFeedback),
        ('/flattr', flattr.Flattr),
        ('/credits', credits.Credits)
    ], debug=True)

