import os
import threading
from instaloader import Instaloader, Profile
from tqdm import tqdm

[
    {
        "domain": ".instagram.com",
        "expirationDate": 1735373998.223724,
        "hostOnly": False,
        "httpOnly": True,
        "name": "datr",
        "path": "/",
    
        "secure": True,
        "session": False,

        "value": "sVxgZb6eyGx3Ohwuh6GGJARt"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1732349998.302494,
        "hostOnly": False,
        "httpOnly": False,
        "name": "ig_nrcb",
        "path": "/",

        "secure": True,
        "session": False,

        "value": "1"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1701419363.272261,
        "hostOnly": False,
        "httpOnly": True,
        "name": "shbts",
        "path": "/",

        "secure": True,
        "session": False,
       
        "value": "\"1700814567\\0548724221981\\0541732350567:01f70235e461def068faddd6b028bbca5d2878dbd1ad43bf429d2fa2bf91dd4b79663657\""
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1708590662.364925,
        "hostOnly": False,
        "httpOnly": False,
        "name": "ds_user_id",
        "path": "/",

        "secure": True,
        "session": False,

        "value": "8724221981"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1701419363.272172,
        "hostOnly": False,
        "httpOnly": True,
        "name": "shbid",
        "path": "/",

        "secure": True,
        "session": False,

        "value": "\"17671\\0548724221981\\0541732350567:01f7efeb23056375ce5b82d3239fd812b8760a45e4cab76f8e7475b22f92157fc2c800de\""
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1732264262.364797,
        "hostOnly": False,
        "httpOnly": False,
        "name": "csrftoken",
        "path": "/",

        "secure": True,
        "session": False,

        "value": "TxdBjCPlCuKU3YV569JZwSntcNF27BSD"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1732350563.272713,
        "hostOnly": False,
        "httpOnly": True,
        "name": "ig_did",
        "path": "/",

        "secure": True,
        "session": False,

        "value": "3A1753F9-B38D-4C0D-A7E8-E21FC956910E"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1735373998.30245,
        "hostOnly": False,
        "httpOnly": False,
        "name": "mid",
        "path": "/",

        "secure": True,
        "session": False,

        "value": "ZWBcsgALAAESiISoRtRcw-477YbN"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1732350562.89107,
        "hostOnly": False,
        "httpOnly": True,
        "name": "sessionid",
        "path": "/",

        "secure": True,
        "session": False,

        "value": "8724221981%3A9u9PQIVXHbtkDV%3A18%3AAYfwMAa-TaI9iq_9qUKmxl7BeIqhU7RrLBSfuYzIkQ"
    },
    {
        "domain": ".instagram.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "rur",
        "path": "/",

        "secure": True,
        "session": True,

        "value": "\"RVA\\0548724221981\\0541732350666:01f7366d7e92a7efa05bdf6a6503936952bcd91139413714fff925c12c0c5c227fe310ff\""
    }
]
# Ask for the profile username
profile_username = input("Enter the profile username: ")

# Function to download a single post
def download_post(loader, post, target_folder):
    try:
        loader.download_post(post, target=target_folder)
    except Exception as e:
        print(f"Failed to download {post} due to {e}")

# Download the profile's media using multithreading
def download_profile_media(profile_username, output_dir):
    loader = Instaloader()
    loader.context._session.headers.update({'User-Agent': user_agent})
    
    for cookie in cookies:
        loader.context._session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
    
    profile = Profile.from_username(loader.context, profile_username)
    
    output_path = os.path.join(output_dir, profile_username)
    os.makedirs(output_path, exist_ok=True)
    
    downloaded_files = 0
    threads = []
    
    for post in profile.get_posts():
        thread = threading.Thread(target=download_post, args=(loader, post, output_path))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
        downloaded_files += 1
    
    print("Download completed!")
    print(f"Total downloaded files: {downloaded_files}")

# Start the download process
download_profile_media(profile_username, output_dir)
