from flask import Flask
from .views.account import account
from .views.index import ind

app = Flask(__name__)
app.config.from_object('settings.Config')
app.register_blueprint(account)
app.register_blueprint(ind)

if __name__ == '__main__':
    app.run()
