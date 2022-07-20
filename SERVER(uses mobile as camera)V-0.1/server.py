# source venv/bin/activate
from flask import Flask, send_file, render_template
import main
import time
# import alexa

app = Flask(__name__)


@app.route('/img')
def downlod_img():
    p = "images/capturedImg.png"
    return send_file(p, as_attachment=True)

# @app.route('/command')
# def send_command():  # send mood file to client
#     x = alexa.Twin()
#     command = x.take_command()
#     # file1 = open("text/command.txt", "w")
#     # file1.write(command)
#     # file1.close()
#     # p = "text/command.txt"
#     # return command


@app.route('/mood')
def send_moodFile():  # send mood file to client
    # reset flg
    file1 = open("text/moodFlg.txt", "w")
    file1.write("False")
    file1.close()
    p = "text/moodFile.txt"
    return send_file(p, as_attachment=True)


@app.route('/moodFlg')
def send_moodFlg():  # send mood file to client
    p = "text/moodFlg.txt"
    return send_file(p, as_attachment=True)


@app.route('/notiFlg')
def send_notiFlg():  # send mood file to client
    p = "text/notiFlg.txt"
    return send_file(p, as_attachment=True)


@app.route('/notification')
def send_notification():  # send mood file to client
    file1 = open("text/notiFlg.txt", "w")
    file1.write("False")
    file1.close()

    p = "text/notificationFile.txt"
    return send_file(p, as_attachment=True)


@app.route('/get_image')
def get_image_from_app():
    print("do work on server")

    #time.sleep(2)
    # run main.py
    runner = main.Main()
    runner.run()
    return "done"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True, threaded=True)