# vknuker
Deletes all VK messages by query.

*Still being tested so use carefully.*

## Requierments

This script requiers [vk_api](https://pypi.org/project/vk-api/) to run.
```bash
pip install vk-api
```

## Usage

### options.json

First of all, you need to edit `options.json`:
```json
{
  "version": "5.131",

  "user_id": "id",
  "pass": "pass",
  "login": "login"
}
```
Replace `"id"` with your VK id, `"pass"` with your VK password, `"login"` with your VK login.

It should look something like this:
```json
{
  "version": "5.131",

  "user_id": "12345678",
  "pass": "iLoveMyMom123",
  "login": "89123456789"
}
```

### Running the script

To use the script, run `main.py`, you will then be guided by the prompts.
You then have to confirm that you want to delete the messages and the process will start.
