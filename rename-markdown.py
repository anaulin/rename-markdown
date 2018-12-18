import argparse
import os
import string

def main(directory):
  print(directory)
  for filename in os.listdir(directory):
    if filename.endswith(".md"):
      with open(os.path.join(directory, filename)) as f:
        first_line = f.readline().strip()
        if not first_line.startswith("#"):
          print("First line doesn't seem to be a title. Skipping. (Line was: {})".format(first_line))
        else:
          # Remove leading '#' and trim whitespace
          title = first_line.replace('#', '').strip()
          # Remove non-printable characters
          allowed_chars = set(string.ascii_letters + string.digits + string.whitespace + '-_')
          printable_title = ''.join(filter(lambda x: x in allowed_chars, title))
          # Replace whitespace with dashes
          no_whitespace = "-".join(printable_title.split())
          new_filename = "{}.md".format(no_whitespace.lower())
          print("Renaming {} to {}".format(filename, new_filename))
          os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    else:
      print("Skipping non-markdown file: {}".format(filename))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('directory', help='Directory with files to rename')
  main(vars(parser.parse_args())['directory'])
