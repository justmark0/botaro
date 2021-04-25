from views import *
import uvicorn


if __name__ == "__main__":
    bots = get_bots()
    for bot in bots:
        p = Process(target=utils.bot.start_bot, args=(bot.token,))
        p.start()
        bot_processes.append({"token": bot.token, "pid": p.pid})
    uvicorn.run(app, host="0.0.0.0", port=8000)
