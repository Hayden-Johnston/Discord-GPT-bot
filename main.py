# author: Hayden Johnston
# date: 08/20/2023
# description: Entrypoint for Discord bot

from bot import run
from db import create_table

if __name__ == "__main__":
    create_table()
    run()