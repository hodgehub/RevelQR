from flask import Flask, send_file, render_template_string

app = Flask(__name__)

VIDEO_PATH = "video.mp4"

HTML = """
<!DOCTYPE html>
<html>
<body style="margin:0;background:#000;overflow:hidden">
  <video id="v" autoplay playsinline loop
    style="width:100vw;height:100vh;object-fit:cover">
    <source src="/video" type="video/mp4">
  </video>
  <script>
    var v = document.getElementById('v');
    v.volume = 0.5;
    v.play();
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/video")
def video():
    return send_file(VIDEO_PATH, mimetype="video/mp4")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
