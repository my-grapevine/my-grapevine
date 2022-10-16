#This is the file we are going to run when we start the web server

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run()