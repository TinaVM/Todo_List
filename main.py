from flask import Flask
from flask import Flask, render_template
#imported module and creating an app using Flask
app = Flask('index.html')

#defining the basic route "/" and its corresponding request handler
@app.route("/")
def main():
    return render_template('index.html')
#checking if the executed file is the main program and running the app
if __name__ == "__main__":
    app.run()





