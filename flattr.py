import handler


class Flattr(handler.Handler):
    def get(self):
        self.render('flattr.jinja2', active='flattr')
