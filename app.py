from flask import Flask
app=Flask(__name__)
@app.route('/')
def run():
    return "<h1>Rioyich tenkai - domain Expansion</h1>"
app.run('0.0.0.0',5000)
