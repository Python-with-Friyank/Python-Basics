#This Little code below will host an Web application to your local/System IP Address.

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World From Flask"

@app.route('/Contact Us')
def contact_us():
    return "Contact @ <h1> +91 80971916906 </h1>"


@app.route('/profile/<username>')
def profile(username):
    return "Hello " + username


@app.route('/news_feed/<int:feed_id>')
def news_feed(feed_id):
    return "Feed ID is " + str(feed_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False)


# To browse if, go to browser and type http://YourSystemIPAddress:5000/  - enjoy