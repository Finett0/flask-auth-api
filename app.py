from flask import Flask
from flask_sqlachemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "%0k*wFLFItFToA^rt;l5"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #uri database

db = SQLAlchemy(app)

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)