import flask
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

class RIMSApp(flask.Flask):
  ENV_CONFIG = "RIMS_CONFIG"
  
  def __init__(self, config_file_path=None):
    super(RIMSApp, self).__init__(
        'rims',
        static_folder=os.path.join(script_dir, 'static'),
        template_folder=os.path.join(script_dir, 'templates')
    )
    self.jinja_env.add_extension('jinja2.ext.do')
    #
    # Basic routing
    #
    
    @self.route('/home')
    @self.route('/')
    def rims_index():
      return flask.render_template("index.html")
      
    #
    # Modules
    #
    # Load up required and optional module blueprints
    #
    
    from mods.browse import BrowseMod
    self.module_browse = BrowseMod(self)
    self.register_blueprint(self.module_browse)
    
    from mods.imgImport import ImportMod
    print ImportMod
    self.module_import = ImportMod(self)
    self.register_blueprint(self.module_import)
    
    from mods.login import LoginMod
    self.module_login = LoginMod(self)
    self.register_blueprint(self.module_login)
    
    from mods.Review import ReviewMod
    self.module_review = ReviewMod(self)
    self.register_blueprint(self.module_review)
    
    from mods.Register import RegisterMod
    self.module_register = RegisterMod(self)
    self.register_blueprint(self.module_register)

    #self._log.debug("Importing Search module")
    #from .mods.search import SearchMod
    #self.module_search = SearchMod(self)
    #self.register_blueprint(self.module_search,
    #                        url_prefix="/search")
  def run(self, host=None, port=None, debug=False, **options):
    super(RIMSApp, self).run(host,port, **options)
    

if __name__ == '__main__':
    from RIMSApp import RIMSApp
    blah = RIMSApp(None)
    blah.run(host='0.0.0.0')