# MTG Card Fetcher Bot for Telegram
## Users
### Syntax
Use the **/card <name of card>** command to search for a card. Capitalisation and minimal spelling errors are ignored.
```
/card The Ur-Dragon
```

### Partial searches
Partial names work as well. If the search comes up with one unique card, it is displayed immediately.
```
/card vorinclex
>> Vorinclex, Voice of Hunger
```

If the search results in too many possible cards, the bot offers possible matches.
```
/card ajani
>> Too many cards match the ambiguous name "ajani", which card did you mean to fetch?
>> Ajani's influence
>> Ajani, Wise Counselor
>> Ajani's Welcome
>> Ajani's Last Stand
```

## Developers
### Bot Token
Add your telegram token to an **auth.py** in the root directory like so:
```
token = "RandomAlphanumericalString"
```