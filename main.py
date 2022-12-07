from flask import Flask, jsonify, redirect, request
import os
app = Flask(__name__)


@app.route('/')
def index():
    f = open("link.txt", "r")
    link = f.read()
    f.close()
    return redirect(link)

@app.route('/change_link', methods=['POST'])
def change_link():
    args = request.args
    data = request.form
    token = args.get('token')
    if token == os.environ.get("SECURITY_TOKEN"):
        link = data.get('link')
        f = open("link.txt", "w")
        f.write(link)
        f.close()
    return link, token
    
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
