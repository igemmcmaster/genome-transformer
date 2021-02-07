colab:
	apt install vim htop --yes
	curl -fsSL https://code-server.dev/install.sh | sh
	pip3 install -r requirements.txt

data: domain = none
data:
	ncbi-genome-download \
		--assembly-levels complete \
		--debug \
		--formats genbank \
		--output-folder "/root/drive/Shareddrives/mGEM/3 - Dry lab/Research Development/GenBank" \
		--parallel 4 \
		--progress_bar \
		--retries 9999 \
		$(domain)
