"""
SSH into Colab instance.

Launch and idle a Colab notebook for 24 days.

Uncomment the `pip install` statement.
Execute the code in a Colab notebook.
Follow instructions from cell output.
"""
from google.colab import drive
drive.mount("/home/drive", force_remount=True)
#!pip install colab_ssh --upgrade
from colab_ssh import launch_ssh_cloudflared
launch_ssh_cloudflared(password="colab")
import time
time.sleep(60*60*24*24)
