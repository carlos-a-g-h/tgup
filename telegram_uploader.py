#!/usr/bin/python3.9

import asyncio

from pathlib import Path
from telethon import TelegramClient

def is_there(f):
	if not f.exists():
		return False

	if not f.is_file():
		return False

	return True

async def uploader(client,some_chat,files_list,once=False):

	some_chat=config.get("tg_chat")

	try:
		int(some_chat)
	except:
		pass
	else:
		some_chat=int(some_chat)

	the_chat=await bot.get_entity(some_chat)
	if not the_chat:
		print("Not a TG entity, finishing program now")
		if once:
			await client.disconnect()

		return

	for fpath in files_list:
		await asyncio.sleep(0.5)
		if not is_there(fpath):
			print("Not found (wait, what?):",fpath.name)
			continue

		print("Uploading:",fpath.name)

		try:
			await bot.send_file(the_chat,fpath)
		except Exception as e:
			print("Upload error:",e)

	print("Program finished")
	if once:
		await client.disconnect()

if __name__=="__main__":

	import json
	import sys

	app_path=Path(sys.argv[0])
	app_name=app_path.stem
	app_conf=app_path.parent.joinpath(app_name+".json")

	if not is_there(app_conf):
		print("Missing config file:",str(app_conf))
		sys.exit(1)

	# Read config file

	config_raw=open(str(app_conf)).read()
	config_raw=config_raw.strip()
	try:
		config=json.loads(config_raw)
	except:
		do_eval=True
	else:
		do_eval=False

	if do_eval:
		try:
			assert config_raw.startswith("{")
			assert config_raw.endswith("}")
			config=eval(config_raw)
		except:
			print("Config file not valid")
			sys.exit(1)

	try:
		if not config.get("tg_api_id"):
			raise Exception("Missing: Telegram API ID (tg_api_id)")

		if not config.get("tg_api_hash"):
			raise Exception("Missing: Telegram API Hash (tg_api_hash)")

		if not config.get("tg_bot_token"):
			raise Exception("Missing: Telegram Bot token (tg_bot_token)")

		if not config.get("tg_chat"):
			raise Exception("Missing: Telegram Chat (tg_chat)")

	except Exception as e:
		print("Error while reading config:",e)
		sys.exit(1)

	# Get filepaths from args

	if not len(sys.argv)>1:
		print("Nothing selected")
		sys.exit(1)

	fpath_lst_raw=sys.argv[1:]
	fpath_lst=[]

	for fpath in fpath_lst_raw:

		fp=Path(fpath.strip())
		if not is_there(fp):
			print("Ignoring:",fp.name)
			continue

		print("Adding:",fp.name)
		fpath_lst.append(fp)

	fpath_lst_raw.clear()
	del fpath_lst_raw

	if len(fpath_lst)==0:
		print("Nothing to upload")
		sys.exit(1)

	bot=TelegramClient(app_name,config.get("tg_api_id"),config.get("tg_api_hash")).start(bot_token=config.get("tg_bot_token"))
	loop=asyncio.get_event_loop()
	loop.run_until_complete(uploader(bot,config.get("tg_chat"),fpath_lst,once=True))
