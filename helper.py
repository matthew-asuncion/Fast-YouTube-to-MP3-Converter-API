from urllib.parse import urlparse, parse_qs


def id_grabber(youtube_url):
    youtube_id = None
    # reference: https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python/54383711#54383711
    # Youtube URL Examples:
    # - http://youtu.be/SA2iWivDJiE
    # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    # - http://www.youtube.com/embed/SA2iWivDJiE
    # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    query = urlparse(youtube_url)
    print(query)
    #ParseResult(scheme='https', netloc='www.youtube.com', path='/watch', params='', query='v=x6Nr6EX3AwY', fragment='')

    if query.hostname == "youtu.be":
        youtube_id = query.path[1:]
    elif query.hostname in {"www.youtube.com", "youtube.com"}:
        if query.path == "/watch":
            youtube_id = parse_qs(query.query)["v"][0]
        elif query.path[:7] == "/watch/":
            youtube_id = query.path.split("/")[1]
        elif query.path[:7] == "/embed/":
            youtube_id = query.path.split("/")[2]
        elif query.path[:3] == "/v/":
            youtube_id = query.path.split("/")[2]
        # below is optional for playlists
        elif query.path[:9] == "/playlist":
            youtube_id = parse_qs(query.query)["list"][0]

    return youtube_id
