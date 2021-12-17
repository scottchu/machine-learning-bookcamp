import os
import gdown

def ensure_correct_directory(desire_directory):
  if os.path.basename(os.getcwd()) != desire_directory:
    os.chdir(desire_directory)

  return os.path.basename(os.getcwd())


def maybe_download(url, output):
  if os.path.exists(output):
    return

  dir = os.path.dirname(output)
  if not os.path.exists(dir):
    os.makedirs(dir, exist_ok=True)

  gdown.download(url, output=output, quiet=None)