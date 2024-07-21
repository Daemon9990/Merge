import os


class Config(object):
    API_HASH = os.environ.get("API_HASH","87a837607d9761cdf98bbc3e61eef098")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7238067007:AAG1pDJTUBwKzeeu0o-G0acMrQUA4JN9Zug")
    TELEGRAM_API = os.environ.get("TELEGRAM_API","23270278")
    OWNER = os.environ.get("OWNER,"6890795853")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","BillyButcher_007")
    PASSWORD = os.environ.get("PASSWORD","VKLeech")
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://parcel:malliga@cluster0.xoax6ur.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL","-1002157233898")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING",BABcEltutHg88NEe4zMtwpBOb-JJPEckyW7Nynl95JKnlj10nDdEXPawFIdVqXXOWPt3tJxEGKCiBnAij7JM-XbgvF1UpP3R-BDc6vP8NnSS0w1OxaPsdZeHohaXuaRpf0sxTYQnX6QD7fS-bZpgWmaFWxUTL6ABVYx8q7P45PXizU_YyANvVMcFtcBxD2w87zdtKpLwKkuhxPsH3yuQueZVlj2_nu34lenkzU8vfGkrnHoFwAQxq1IPkPdsu-1ZvBTsOb-_vGNe3YwDjybAozUbfi0PsNVTzaRRPC9MsYsuJNl_5WMJI4BRSb9u5WuTaf2qVrrvm06Ev2Hw7iHibSciAAAAAZq5M00A")
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
