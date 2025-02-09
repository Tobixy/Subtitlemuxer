class Chat:

    START_TEXT = """This is a Telegram Bot to Mux subtitle into a video

<b>Send me a Telegram file to begin</b>

/help for more details..

Credits :- @mohdsabahat
    """

    HELP_USER = "??"

    HELP_TEXT ="""<b>Welcome to the Help Menu</b>

1.) Send a Video file or url.
2.) Send a subtitle file (ass or srt)
3.) Choose you desired type of muxing!

To give custom name to file send it with url seperated with |
<i>url|custom_name.mp4</i>

<b>Note : </b><i>Please note that only english type fonts are supported in hardmux other scripts will be shown as empty blocks on the video!</i>

<a href="https://github.com/mohdsabahat/sub-muxer">Repo URL</a>"""

    NO_AUTH_USER = "You are not authorised to use this bot.\nContact the bot owner!"
    DOWNLOAD_SUCCESS = """File downloaded successfully!

Time taken : {} seconds."""
    FILE_SIZE_ERROR = "ERROR : Cannot Extract File Size from URL!"
    MAX_FILE_SIZE = "File size is greater than 2Gb. Which is the limit imposed by telegram!"
    LONG_CUS_FILENAME = """Filename you provided is greater than 60 characters.
Please provide a shorter name."""
    UNSUPPORTED_FORMAT = "ERROR : File format {} Not supported!"
    CHOOSE_CMD = "Subtitle file downloaded successfully.\nChoose your desired muxing!\n[ /softremove , /softmux , /hardmux ]"

    START_TEXT_PM = """Hi there! I am a Telegram Bot to Mux subtitles into a video.

You can use me to add subtitles to your videos. Just send me a video file and a subtitle file (ass or srt format), and choose the type of muxing you want.

Use /help to learn more about how to use me."""

    START_TEXT_GROUP = "Hi, I'm a bot to help you mux subtitles into videos. If you have any questions, send me a private message."

    HELP_TEXT_PM = """<b>Welcome to the Help Menu</b>

1.) Send a Video file or url.
2.) Send a subtitle file (ass or srt)
3.) Choose you desired type of muxing!

To give custom name to file send it with url seperated with |
<i>url|custom_name.mp4</i>

<b>Note : </b><i>Please note that only english type fonts are supported in hardmux other scripts will be shown as empty blocks on the video!</i>

<a href="https://github.com/mohdsabahat/sub-muxer">Repo URL</a>"""
