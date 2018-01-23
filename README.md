# CryptoTrackerBot
CryptoTrackerBot - check cryptocurrencies prices on telegram


## How to install:

### On Linux:

- Move to the path where you want to create the virtualenv directory
```
cd path
```
- Create a folder containing the env named `ctbenv`
```
virtualenv -p python3 ctbenv 
```
- Install the bot from the zip
```
ctbenv/bin/pip install https://github.com/91dariodev/cryptotrackerbot/archive/master.zip
```
- Run the bot. The first parameter of the command is the token.
```
ctbenv/bin/cryptotrackerbot token
```
- To upgrade the bot:
```
ctbenv/bin/pip install --upgrade https://github.com/91dariodev/cryptotrackerbot/archive/master.zip
```
- To delete everything:
```
rm -rf ctbenv
```