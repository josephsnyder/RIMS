import flask
import os
import os.path as osp

import sys

sys.path.append("../../..")
from RIMSAuth import requires_auth
script_dir = osp.dirname(osp.abspath(__file__))

class BrowseMod(flask.Blueprint):

  def __init__(self,parent_app):
    super(BrowseMod, self).__init__(
            'browse', __name__,
            template_folder=osp.join(script_dir, 'templates')
        )
    @self.route('/browse', methods=['get'])
    @requires_auth
    def login():
    # Render the login page, then continue on to a previously requested
    # page, or the home page.
      return flask.render_template('browse.html')