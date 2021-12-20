# CFRankListBot

A bot that displays the top ranks for a Codeforces contest.

## Participants' Details

All the details of a participant is in the `utils/__init__.py` file.

## Commands

### `/getrank <contest-id>`

Gets the ranklist for the particular contest.

## Todo

- [ ] Add the field gender to the data.

## Development

1. Search for @botfather in Telegram.
2. Start your conversation by pressing the Start button.
3. Create the bot by running /newbot command
4. Enter the Display Name (use any name that is available) and User Name for the bot.
5. BotFather will send you a message with the token.
6. Make a `.env` file `cp .env_sample .env`.
7. Fill the token in the `.env`.
8. Run the following commands:

```bash
pip install -r requirements.txt # to install dependencies
python3 bot.py
```

## Deplopy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/codeiiest-dev/CFRankListBot)
