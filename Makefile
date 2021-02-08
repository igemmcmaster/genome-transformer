colab:
	apt install vim htop --yes
	curl -fsSL https://code-server.dev/install.sh | sh
	pip3 install -r requirements.txt
	git clone https://github.com/kblin/ncbi-genome-download.git ../ncbi-genome-download
	cd ../ncbi-genome-download && pip3 install .
	useradd -m -s /bin/bash -p igem igem
	adduser igem sudo

data: domain = none
data:
	ncbi-genome-download \
		--assembly-levels complete \
		--debug \
		--formats genbank \
		--output-folder "/root/drive/Shareddrives/mGEM/3 - Dry lab/Research Development/GenBank" \
		--parallel 16 \
		--progress-bar \
		--retries 9999 \
		$(domain)
