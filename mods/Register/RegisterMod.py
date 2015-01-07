import flask
import os
import os.path as osp

script_dir = osp.dirname(osp.abspath(__file__))

class RegisterMod(flask.Blueprint):
  def __init__(self,parent_app):
    super(RegisterMod, self).__init__(
           'register', __name__,
            template_folder=osp.join(script_dir, 'templates')
        )
    @self.route('/register', methods=['get'])
    def login():
    # Render the login page, then continue on to a previously requested
    # page, or the home page.
      return flask.render_template('register.html')