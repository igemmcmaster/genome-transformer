ASPERA_CONNECT = ibm-aspera-connect-3.11.1.58-linux-g2.12-64
GENBANK_DATA_DIR = "/home/drive/Shareddrives/mGEM/3 - Dry lab/Research Development/genomes/genbank"
NONROOT = igem

aspera: domain = none
aspera:
	/home/$(NONROOT)/.aspera/connect/bin/ascp \
		-i /home/$(NONROOT)/.aspera/connect/etc/asperaweb_id_dsa.openssh -k1 -Tr -l128m \
		--overwrite=never \
		anonftp@ftp.ncbi.nlm.nih.gov:/genomes/genbank/$(domain) $(GENBANK_DATA_DIR)

colab:
	apt install vim htop --yes
	curl -fsSL https://code-server.dev/install.sh | sh
	pip3 install -r requirements.txt
	git clone https://github.com/kblin/ncbi-genome-download.git ../ncbi-genome-download
	cd ../ncbi-genome-download && pip3 install .
	rm -rf ../ncbi-genome-download
	wget https://ak-delivery04-mul.dhe.ibm.com/sar/CMA/OSA/09ff1/0/$(ASPERA_CONNECT).tar.gz
	tar -xzvf $(ASPERA_CONNECT).tar.gz
	rm $(ASPERA_CONNECT).tar.gz
	useradd -m -s /bin/bash $(NONROOT)
	su $(NONROOT) -c "./$(ASPERA_CONNECT).sh"
	rm -rf $(ASPERA_CONNECT).sh

ncbi-genome-download: domain = none
ncbi-genome-download:
	ncbi-genome-download \
		--assembly-levels complete \
		--debug \
		--formats genbank \
		--output-folder $(GENBANK_DATA_DIR) \
		--parallel 16 \
		--progress-bar \
		--retries 9999 \
		$(domain)
