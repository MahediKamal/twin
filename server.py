# source venv/bin/activate
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/img')
def downlod_img():
	p = "mohimBC.mp4"
	return send_file(p,as_attachment=True)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5050, debug=True, threaded=True)
