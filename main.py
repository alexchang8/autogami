from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/design")
def design():
	return render_template("design.html")


'''
@app.route("/patterns/")
def patternFinder():
    return render_template("finder.html")

@app.route("/patterns/<pattern>")
def home(pattern = None):
    return render_template("pattern.html", pattern = pattern)




if __name__ == '__main__':
    app.run(port=6000, debug = False)
    '''
if __name__ == "__main__":
	app.run(debug=True)

