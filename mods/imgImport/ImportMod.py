import flask
import os
import os.path as osp

script_dir = osp.dirname(osp.abspath(__file__))

class ImportMod(flask.Blueprint):

  def __init__(self,parent_app):
    super(ImportMod, self).__init__(
            'imgImport', __name__,
            template_folder=osp.join(script_dir, 'templates')
        )
    @self.route('/imgImport', methods=['get'])
    def login():
    # Render the login page, then continue on to a previously requested
    # page, or the home page.
      return flask.render_template('import.html')
      
    @self.route('/_upload', methods=["POST"])
    def upload():
      print "This is an attempted upload"