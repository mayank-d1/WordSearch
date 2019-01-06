from api import create_app
""" basic template to import app settings and create a new instance of app
    app name :- api
    Settings in init path
"""

app = create_app()

if __name__ == '__main__':
    """ Start flask app"""
    app.run(debug=False)
