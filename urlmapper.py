import webapp2
import mainpage
import credits
import download
import yesnofeedback


app = webapp2.WSGIApplication(
    [
        ('/', mainpage.MainPage),
        ('/download', download.DownloadPage),
        ('/yesnofeedback', yesnofeedback.YesNoFeedback),
        ('/credits', credits.Credits)
    ], debug=True)

