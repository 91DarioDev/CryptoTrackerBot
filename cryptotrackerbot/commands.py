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


def price_command(bot, update, args):
	if len(args) == 0:  # return if no args added
		text = "Error: You have to append to the command as parameters the code of the crypto you want\n\nExample:<code>/price btc eth xmr</code>"
		update.message.reply_text(text, parse_mode='HTML')
		return

	response = cryptoapi.get_price(args)
	print(response)
	if 'Response' in response and response['Response'] == 'Error':  # return if response from api is error
		text = "<b>Error!</b>"
		text += "\n{}".format(response['Message']) if 'Message' in response else ''
		update.message.reply_text(text, parse_mode='HTML')
		return

	text = ""
	for coin in response:
		text += "<b>— {}:</b>".format(coin)
		prices = response[coin]
		for price in prices:
			text += "\n  - {}: {}".format(price, prices[price])
		text += "\n\n"
	update.message.reply_text(text, parse_mode='HTML')


def help(bot, update):
	text = (
		"<b>SUPPORTED COMMANDS:</b>"
		"/price - <i>return price of crypto</i>"
		"/help - <i>return help message</i>"
		"\n"
		"This bot is released under the terms of AGPL 3.0 LICENSE"
	)
	update.message.reply_text(text, parse_mode='HTML')