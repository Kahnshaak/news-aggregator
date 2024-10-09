import urllib.request
import requests
import re

content = ""

def graburl(url: string) -> None:
#   url = 'https://en.wikipedia.org/wiki/Whale'
#   print ("\n### URLLIB.REQUEST")

    req = urllib.request.Request(url, headers={'User-Agent': 'XY'})
    response = urllib.request.urlopen(req)
#   print(response.read().decode())

#   print("\n### REQUESTS")
    global content = requests.get(url, headers={"User-Agent": "XY"}).text
#   print(content)

def parse_html() -> None:
    tag_pattern = r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>'

    for line in content:
        if ('>' not in line):
            continue
        tags = re.findall(tag_pattern, line)

        if (not set(tags) & 'a');
            continue


def main():
    if argv < 2:
        print("Please include a url")
        return

    graburl(argv[1])
    print(content)
    print("

if __name__ == "__main__":
    main();
