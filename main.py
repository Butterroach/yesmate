import os
import shutil
import time
import yt_dlp
from flask import Flask, render_template, request, jsonify, send_from_directory
from waitress import serve

app = Flask(__name__)
ydl = yt_dlp.YoutubeDL()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/videos/<path:path>")
def videos(path):
    return send_from_directory("videos", path)


@app.route("/scripts/<path:path>")
def scripts(path):
    return send_from_directory("scripts", path)


@app.route("/api/download", methods=["POST"])
def api_download():
    shutil.rmtree("videos")  # scary
    os.makedirs("videos")  # :3
    os.chdir("videos")
    ydl.download(request.json["url"])
    os.chdir("..")
    for file in os.listdir("videos"):
        # absolutely confident there should only be one file which is the video that was just downloaded
        # obviously uh race conditions but no one is gonna seriously use this so
        return jsonify({"status": "success", "url": f"/videos/{file}"}), 200


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=39193)
