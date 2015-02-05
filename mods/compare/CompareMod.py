import flask
import os
import os.path as osp

script_dir = osp.dirname(osp.abspath(__file__))
import sys

sys.path.append("../../..")
from RIMSAuth import requires_auth

class CompareMod(flask.Blueprint):

  def __init__(self,parent_app):
    super(CompareMod, self).__init__(
            'Compare', __name__,
            template_folder=osp.join(script_dir, 'templates')
        )
    @self.route('/compare', methods=['get'])
    @requires_auth
    def login():
    # Render the login page, then continue on to a previously requested
    # page, or the home page.
      return flask.render_template('compare.html')