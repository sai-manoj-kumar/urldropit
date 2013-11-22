import handler


class MainPage(handler.Handler):
    def get(self):
        error = self.request.get('error')
        if error is not None:
            self.render('sb_form.jinja2', active='home', error=error)
        else:
            self.render('sb_form.jinja2', active='home')
