from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/design")
def design():
	return render_template("design.html")
'''
@app.route("/download")
def download():
'''
'''
@app.route("/download")
def download():
	try:
		return send_file('/var/www/PythonProgramming/PythonProgramming/static/ohhey.pdf', attachment_filename='pattern.pdf')
	except Exception as e:
		return str(e)
'''


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

