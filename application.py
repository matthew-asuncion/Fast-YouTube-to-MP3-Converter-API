from flask import Flask
from flask import request
from flask import render_template
import helper

application = app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def converter():
    youtube_url = ""
    if request.method == "POST" and "youtube_link" in request.form:
        # Declare all variables.
        youtube_url = str(request.form.get("youtube_link")).strip()
        # print(youtube_url)
        # https://www.youtube.com/watch?v=lUKGzvQj4bI.

    # Extracting the ID from youtube_link
    youtube_id = str(helper.id_grabber(youtube_url))

    # Making the IFrame link with the Youtube URL
    api_converter_link = "https://www.yt-download.org/api/button/mp3/" + youtube_id

    return render_template(
        "index.html",
        youtube_url=youtube_url,
        youtube_id=youtube_id,
        api_converter_link=api_converter_link,
    )


if __name__ == "__main__":
    # Use 'debug=True' to avoid resarting vs code
    # everytime there is an update in the code.
    app.run(debug=True)
