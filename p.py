import pyrogram

class PinterestBot(pyrogram.Bot):

    def __init__(self, token):
        super().__init__(token)

    def on_message(self, message):
        if message.text is not None:
            link = message.text
            if message.text.endswith(".jpg") or message.text.endswith(".png"):
                image = pyrogram.File.from_url(link)
                self.send_photo(message.chat.id, image)
            elif message.text.endswith(".mp4"):
                video = pyrogram.File.from_url(link)
                self.send_video(message.chat.id, video)
            else:
                gif = pyrogram.File.from_url(link)
                self.send_animation(message.chat.id, gif)

bot = PinterestBot(token="YOUR_BOT_TOKEN")
bot.run()
