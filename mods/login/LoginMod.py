import flask
import os
import os.path as osp

script_dir = osp.dirname(osp.abspath(__file__))

class LoginMod(flask.Blueprint):
  def __init__(self,parent_app):
    super(LoginMod, self).__init__(
            'login', __name__,
            template_folder=osp.join(script_dir, 'templates')
        )
    @self.route('/login', methods=['get'])
    def login():
    # Render the login page, then continue on to a previously requested
    # page, or the home page.
      return flask.render_template('login.html')
             #next=flask.request.args.get('next', '/home'))