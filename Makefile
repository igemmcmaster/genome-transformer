ASPERA_CONNECT = ibm-aspera-connect-3.11.1.58-linux-g2.12-64
GENBANK_DATA_DIR = "/home/drive/Shareddrives/mGEM R&D/genomes/genbank"
NONROOT = igem

aspera: domain = none
aspera:
	/home/$(NONROOT)/.aspera/connect/bin/ascp -k1 -drT -l128m --overwrite=never \
		-i /home/$(NONROOT)/.aspera/connect/etc/asperaweb_id_dsa.openssh \
		anonftp@ftp.ncbi.nlm.nih.gov:/genomes/genbank/$(domain) $(GENBANK_DATA_DIR)

colab:
	apt install vim htop iftop --yes
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
	wget https://raw.githubusercontent.com/pirovc/genome_updater/master/genome_updater.sh
	chmod +x genome_updater.sh

genome_updater: group = none, jobs = 1
genome_updater:
	./genome_updater.sh \
		-i -m -p \
		-c all \
		-d refseq,genbank \
		-f genomic.gbff.gz,protein.gpff.gz \
		-g $(group) \
		-j taxids:1 \
		-l "Complete Genome" \
		-o $(GENBANK_DATA_DIR)/$(group) \
		-t $(jobs)

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
