class YoutubeConnectionError(BaseException):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise YoutubeConnectionError("无法翻墙")

except YoutubeConnectionError as err:
    print(err)
