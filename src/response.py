import enum

class status(enum.Enum):
    SUCCESS = 1
    FAILURE = 2

async def respond(ctx, message, ResponseStatus):
    resp_status_str = "[INFO]" if ResponseStatus == status.SUCCESS else "[ERROR]"
    await ctx.response.send_message(f"```{resp_status_str} - {message}```")