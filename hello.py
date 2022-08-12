from exfabrica import app

if __name__ == '__hello__': 
    app.run()


@app.route('/')
def hello():
    return '<h1>BIENVENIDOS A SANTA ELENA!<h1/>'