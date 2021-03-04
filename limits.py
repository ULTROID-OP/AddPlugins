borg = bot
@ultroid_cmd(pattern="limits")
async def _(event):
    bot = "@SpamBot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/start")
                danish = await conv.get_response()
                final = ("HeHe", "")
                await borg.send_message(event.chat_id, danish.text)
                await event.delete()
           
