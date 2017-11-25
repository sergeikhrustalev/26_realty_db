# Real Estate Site

Site for searching Real Estate advertisements

# Set up database

Creating new base
```bash
python database_manager.py --newbase --loaddata ads.json
```
Add new data to the base

```bash
python database_manager.py --loaddata new_ads.json
```

# Running site

Production mode:

```bash
$python server.py
```

Debug mode:

```bash
$SERVER_DEBUG=True python server.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
