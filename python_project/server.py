from flask_app import app
from flask_app.controllers import item_controller, store_controller


if __name__=="__main__":
    app.run(debug = True)