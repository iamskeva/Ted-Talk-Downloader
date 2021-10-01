import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

url = 'https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection'

url_1 = 'https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity'


def input_url(url):

    vid = requests.get(url)
    print('Download about to start')
    soup = BeautifulSoup(vid.content, 'html.parser')
    for val in soup.findAll('script'):
        if (re.search('talkPage.init', str(val))) is not None:
            result = str(val)
    result_mp4 = re.search('(?P<url>https?://[^\s]+)(mp4)', result).group('url')
    return result_mp4.split('"')[0]

def download_mp4():
    mp4_url = input_url(url)
    print("Downloading video from ..... ", mp4_url)

    file_name = mp4_url.split("/")[len(mp4_url.split("/")) - 1].split('?')[0]
    print('Storing video in ...', file_name)
    video = requests.get(mp4_url)


    with open(file_name, 'wb') as f:
        f.write(video.content)
    print('Download Process Finished')

if __name__ == '__main__':
    download_mp4()