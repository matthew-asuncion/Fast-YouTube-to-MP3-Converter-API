from flask import Flask
from flask import request
from flask import render_template
import helper

application = app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def converter():
    youtube_url = ""
    youtube_id = ""
    api_converter_link = ""
    video_info = []

    # this basically waits for when the user clicks convert (which triggers a POST request) and if the value "youtube_link" is inside the form, it will do the following.
    if request.method == "POST" and "youtube_link" in request.form:

        # This gets the "youtube_link" and then turns it into a string and strips it for empty spaces
        youtube_url = str(request.form.get("youtube_link")).strip()

        # This basically calls the info_grabber() function with the passed paramaters youtube(url) from the helper module.
        video_info = helper.info_grabber(youtube_url)
        # This basically calls the id_grabber() function with the passed paramaters youtubeurl from the helper module and then assigns it to a variable.
        youtube_id = str(helper.id_grabber(youtube_url))

        # A simple concatenation. Making the IFrame link with the Youtube URL
        api_converter_link = "https://www.yt-download.org/api/button/mp3/" + youtube_id

    return render_template(
        "index.html",
        youtube_url=youtube_url,
        youtube_id=youtube_id,
        api_converter_link=api_converter_link,
        video_info=video_info
    )


# if __name__ == "__main__":
#     # Use 'debug=True' to avoid resarting vs code
#     # everytime there is an update in the code.
#     app.run(debug=True)
