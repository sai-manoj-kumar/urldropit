import handler


class MainPage(handler.Handler):
    def get(self):
        error = self.request.get('error')
        if error is not None:
            self.render('mainpage.jinja2', active='home', error=error)
        else:
            self.render('mainpage.jinja2', active='home')
