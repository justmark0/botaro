from fastapi.responses import HTMLResponse
from multiprocessing import Process

import utils.bot
from data.database import engine
from utils.auth import *
import sys

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return 'You can go to the <a href=\"/docs\"> docs</a> to see the documentation>'


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"usr": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token}


@app.post("/me", response_model=UserBasic)
async def read_users_me(form_data: Token):
    user = await get_current_user(form_data.access_token)
    if user is not None:
        return UserBasic(username=user.username)
    return {"message": "No such user"}


@app.post("/reg")
def registrate_new_user(form_data: User):
    try:
        create_user(form_data)
    except Exception as e:
        return {"message": e.args[0]}
    return {"message": "success"}


@app.post("/new_bot")
async def registrate_new_bot(auth: Token, bot_data: Bot):
    user = await get_current_user(auth.access_token)
    if user is None:
        return {"message": "No such user"}
    if len(user.bots) > 5:
        return {"message": "You cannot registrate new bots limit is 5"}
    try:
        create_bot(bot_data, user)
    except Exception as e:
        return {"message": e.args[0]}
    p = Process(target=utils.bot.start_bot, args=(bot_data.token,))
    p.start()
    return {"message": "success"}
