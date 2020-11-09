
 # importing modules
import helper
import random
import pathlib
import feedparser

root = pathlib.Path(__file__).parent.parent.resolve()
url = root / "latest.xml"
entries = feedparser.parse(url)["entries"]
for entry in entries:
    string_output = entry['description']
    print("latest: ", string_output)

if __name__ == "__main__":
    output = ""
    readme = root / "README.md"
    readme_contents = readme.open().read()
    final_output = helper.replace_chunk(readme_contents,"threat_marker",f'<div class="container alert">{string_output}</div>')
    readme.open("w").write(final_output)
