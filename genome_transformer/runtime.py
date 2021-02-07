from google.colab import drive
drive.mount("/root/drive", force_remount=True)
#!pip install colab_ssh --upgrade
from colab_ssh import launch_ssh_cloudflared
launch_ssh_cloudflared(password="colab")
