# CryptoTrackerBot - check cryptocurrencies prices on telegram
# Copyright (C) 2018  Dario 91DarioDev <dariomsn@hotmail.it> <github.com/91dariodev>
#
# CryptoTrackerBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CryptoTrackerBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with CryptoTrackerBot.  If not, see <http://www.gnu.org/licenses/>.

from cryptotrackerbot import cryptoapi
from cryptotrackerbot import utils
from cryptotrackerbot import emoji


def price_command(bot, update, args, job_queue):
    if len(args) == 0:  # return if no args added
        text = "Error: You have to append to the command as parameters the code of the crypto you want\n\nExample:<code>/price btc eth xmr</code>"
        utils.send_autodestruction_message(bot, update, job_queue, text)
        return

    response = cryptoapi.get_price(args)
    #print(response)
    if 'Response' in response and response['Response'] == 'Error':  # return if response from api is error
        text = "<b>Error!</b>"
        text += "\n{}".format(response['Message']) if 'Message' in response else ''
        utils.send_autodestruction_message(bot, update, job_queue, text)
        return

    text = ""
    for coin in response:
        text += "<b>— {}:</b>".format(coin)
        prices = response[coin]
        for fiat in prices:
            emoji_coin = emoji.BTC if fiat.upper() == 'BTC' else emoji.USD if fiat.upper() == 'USD' else emoji.EUR if fiat.upper() == 'EUR' else ""
            text += "\n  - {}{}: {}".format(emoji_coin, fiat, utils.sep(prices[fiat]))
        text += "\n\n"
    utils.send_autodestruction_message(bot, update, job_queue, text)


def help(bot, update, job_queue):
    text = (
        "<b>SUPPORTED COMMANDS:</b>\n"
        "/price - <i>return price of crypto</i>\n"
        "/help - <i>return help message</i>\n"
        "\n"
        "Note: If this bot is added in groups as admin, in order to keep the chat clean of spam, after few seconds it deletes both "
        "the command issued by the user and the message sent by the bot."
        "\n"
        "This bot is <a href=\"https://github.com/91DarioDev/CryptoTrackerBot\">released under the terms of AGPL 3.0 LICENSE</a>."
    )
    utils.send_autodestruction_message(bot, update, job_queue, text, destruct_in=120, disable_web_page_preview=True)