from views import *
import uvicorn


if __name__ == "__main__":
    bots = get_bots()
    for bot in bots:
        p = Process(target=utils.bot.start_bot, args=(bot.token,))
        p.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
