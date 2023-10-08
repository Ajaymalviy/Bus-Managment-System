from flask import Flask
app=Flask(__name__,sinstance_relative_config=True)
# # # DEBUG=True
# # # app.config.from_object(__name__)
# # # app.config.from_pyfile('mycofig.cfg') @app.route('/')
# # # def index():
# # #     return "hello there"
# # # if __name__=='__main__':
# # #     # app.run()

# # app = Flask(__name__)
# # app.config.from_object('myonfig.cfg.default_settings')
# # app.config.from_envvar('myconfig.cfg')
# app.config.from_object('yourapplication.default_settings')
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')
#  if __name__=='__main__':
#      app.run()
config1.txt = os.path.join(app.instance_path, 'application.cfg')
with open('config1.txt') as f:
    config = f.read()

# or via open_instance_resource:
with app.open_instance_resource('application.cfg') as f:
    config = f.read()