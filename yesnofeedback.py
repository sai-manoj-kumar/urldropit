import json
import logging
import handler
import model


class YesNoFeedback(handler.Handler):
    def post(self):
        url = json.loads(self.request.body).get('url', False).strip()
        status = json.loads(self.request.body).get('success', None)
        logging.info(self.request.headers)
        if status:
            logging.info('Success: %s' % url)
        else:
            logging.error('Failed: %s' % url)
        self.response.write('Response Taken')
        if url not in [None, ''] or True:
            yesno = model.YesNoFeedback(url=url, success=status)
            yesno.put()
