import requests
import connections
from fake_useragent import UserAgent

ua = UserAgent()

# geting name for file
def get_name(file_url):
    return(file_url.split("/")[-1])

# parsing video
def download_file(url):
    try:
        request = requests.get(url, headers={"User-Agent": ua.random}, stream=True)
        with open(get_name(url), "wb") as webfile:
            for chunk in request.iter_content(chunk_size=1024 * 100):
                webfile.write(chunk)
        return("Download complete!")
    except Exception as error:
        print(error)

download_file(connections.video_url)