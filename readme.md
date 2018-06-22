# MTG Card Fetcher Bot for Telegram
## Users
### Synthax
Use the **/card <name of card>** command to search for a card. Capitalisation and minimal spelling errors are ignored.

```
/card The Ur-Dragon
```

### Partial searches
Partial names can be used as long as there is enough information to find a specific card.

```
/card vorinclex
>> Vorinclex, Voice of Hunger
```

If the search results in too many possible cards, the bot returns an error.

```
/card urabrask
>> Too many cards match ambiguous name “urabrask”. Add more words to refine your search.
```

## Developers
### Bot Token
Add your telegram token to an **auth.py** in the root directory like so:
```
token = "RandomAlphanumericalString"
```