from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome on your website ! @evanbtc :)</h1>"

# If you want to return html file (from flask import render_template)
# Your html file needs to be in the template folder (app/templates/index.html) 
@app.route('/html')
def html():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
