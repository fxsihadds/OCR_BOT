from functools import wraps
from typing import Callable
import asyncio

# Ensure a Consistent event loop!
def get_or_create_event_loop():
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop


loop = get_or_create_event_loop()

def run_sync_in_thread(func: Callable) -> Callable:
    """
        A decorator for running a synchronous long running function asynchronously in a separate thread,
        without blocking the main event loop which make bot unresponsive.

        To use this decorator, apply it to any synchronous function, then you can then call that function to anywhere
        in your program and can use it along with await keyword. This will allow the function to be run asynchronously,
        and avoid blocking of the main event loop.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        return await loop.run_in_executor(None, func, *args, **kwargs)

    return wrapper
