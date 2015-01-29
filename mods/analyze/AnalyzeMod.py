import flask
import os
import os.path as osp

script_dir = osp.dirname(osp.abspath(__file__))

class AnalyzeMod(flask.Blueprint):

  def __init__(self,parent_app):
    super(AnalyzeMod, self).__init__(
            'analyze', __name__,
            template_folder=osp.join(script_dir, 'templates')
        )
    @self.route('/analyze', methods=['get'])
    def login():
    # Render the login page, then continue on to a previously requested
    # page, or the home page.
      return flask.render_template('analyze.html')