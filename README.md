# Telegram Uploader

[Download binary (Linux amd64)](https://github.com/carlos-a-g-h/tgup/releases/download/telegram_uploader/telegram_uploader.linux.amd64)

## Description

A program that uploads one or more files to a Telegram chat

## Usage

You can either use the python script or the binary made with pyinstaller

Python
```
python3 telegram_uploader.py filepath1 filepath2 filepath3 filepathN
```
Binary
```
./telegram_uploader filepath1 filepath2 filepath3 filepathN
```

## Configuration

You need Telegram API Id, API Hash, a Bot token and a Chat (username, chat ID, etc...)

The config file must be in the same directory as the program, and the filename of the config file must match the program's stem (filename without the extension)
