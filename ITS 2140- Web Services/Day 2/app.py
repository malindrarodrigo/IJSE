# pip install Flask

# python --version

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, port=8081) # to change the port 


# make docker file
# docker build -t class3 .
# docker run -p 5000:5000 class3

