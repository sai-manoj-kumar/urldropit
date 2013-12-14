import handler


class Credits(handler.Handler):
    def get(self):
        self.render('credits.jinja2', active='credits')
