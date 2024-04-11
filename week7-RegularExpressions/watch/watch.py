import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # if matches := re.search(r'src="(https://www.youtube.com/embed/(\w+))"', s):
    #     return f"{matches.group(1)}//youtu.be/{matches.group(2)}"
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"', s):
        return f"https://youtu.be/{matches.group(1)}"
    # if matches := re.search(r'^src="(http:|https:)//(?:www\.)?youtube\.com/embed/(\w+)"', s, re.IGNORECASE):
    #     return f"{matches.group(1)}//youtu.be/{matches.group(2)}"
    else:
        return None

if __name__ == "__main__":
    main()
