# MTG Card Fetcher Bot for Telegram
## Users
### Inline search
To search for cards, mention the bot then input your search **without sending the message**. Cards should appear shortly after.
```
@MTGCFBot The Ur-Dragon
```

### Command
Use the **/card <name of card>** command to display a card. Capitalization and minimal spelling errors do not affect the result.
```
/card The Ur-Dragon
```

## Developers
### Bot Token
Add your telegram token to an **auth.py** in the root directory like so:
```
token = "RandomAlphanumericalString"
```