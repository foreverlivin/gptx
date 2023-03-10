from functools import wraps
import os

allowed_users = {1443454117}


def auth():
    """Verify that the user is allowed to use the bot."""

    def decorator(func: callable):
        @wraps(func)
        async def wrapper(update, context):
            if update.effective_user.username not in allowed_users:
                await func(update, context)
            else:
                await update.message.reply_text(
                    "You are not authorized to use this bot"
                )

        return wrapper

    return decorator
