import logging
import handler


class DownloadPage(handler.Handler):
    def get(self):
        url = self.request.get('url').strip()
        filename = self.request.get('filename').strip()
        if url is not None and url != '':
            logging.debug('URL is %s' % url)
            if not url.startswith(('http://', 'https://', 'ftp://')):
                url = 'http://' + url
                logging.debug('Modified URL is %s' % url)
            self.render('sb_download.jinja2', url=url, filename=filename)
        else:
            self.redirect('/?error=URL field should not be blank')