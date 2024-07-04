## About The Repo

This repo contains an example of minting NFT's on Cardano with PyCardano. In this example we'll also use the flexibility of Cardano's metadata to add extra attributes to our NFT's. The goal could be to create game characters like below.
<p float="left">

<img src="assets/artist.png" alt="Artist" width="100"/>
<img src="assets/astrologer.png" alt="Artist" width="100"/>
<img src="assets/blacksmith.png" alt="Artist" width="100"/>
<img src="assets/citizen.png" alt="Artist" width="100"/>
<img src="assets/herbalist.png" alt="Artist" width="100"/>
<img src="assets/hunter.png" alt="Artist" width="100"/>
<img src="assets/jeweler.png" alt="Artist" width="100"/>
</p>


For this example we'll be minting 5 NFT's. We'll:
1. generate and store the collection in a JSON file (assets.json) - generate_assets.py
2. loop over the JSON file and create NFT's - main.py



## Requirements

Keep in mind we'll be using 2 wallets!
1. your Nami wallet to visualize the assets
2. a (minting engine) wallet which will be used by the script

- The UZH Nami wallet - link to internal repo here
- A Cardano mnemonic - this can be any 24 word mnemonic generated from Nami or other sources like https://iancoleman.io/bip39/ -> set dropdown to 24 -> copy BIP38 mnemonic. [ONLY DO THIS IN DEV]

## Install dependencies


### Unix 
Git - package to interact with Github and other source control platforms


```bash
sudo apt install -y git
```

Python + pip - Programming language & package manager

    sudo apt install -y python3 python3-pip

### Windows / Mac

Git 

With Mac you can use Brew if you are familiar with this. If not, go for the download + install. 


```bash
https://git-scm.com/downloads
```
or
```bash
brew install git
```

Python

```
https://www.python.org/downloads/
```
or
```bash
brew install python3
```

### Check if installed correctly (from terminal / CLI):

    git --version
    git version





## How to Run?

Clone the repo
```bash
git clone https://github.com/Godspeed-exe/uzh_minting_nfts
```

Move into the folder
```bash
cd uzh_minting_nfts
```
Install Python libraries (pyCardano & blockfrost & load_dotenv)
```bash
pip3 install -r requirements.txt
```

Copy .env-example to .env
```bash
cp .env-example .env
```

Update .env - only wallet_mnemonic
```bash
wallet_mnemonic='your_wallet_mnemonic_here'
your_wallet_address='the_address_of_your_nami_wallet'
```

Generate some random assets based on the content of [all_assets.json](all_assets.json)
```bash
python3 generate_assets.py
```
Mint the assets to your wallet
```bash
python3 main.py
```

## Possible errors

- Python not installed
```bash
1. Install python 3.x for your OS
2. Make sure Python executable is in your PATH - Google: "adding Python to PATH [your OS here]"
3. Restart your terminal to reload PATH variable
```

- PyCardano / Blockfrost not installed
```bash
pip3 install pycardano
```

- Unfulfilled amount:
 {'coin': 1659643, 'multi_asset': {}}
```bash
This indicates your wallet does not have any ADA available for building the transaction. Make sure you send ADA (ex: 10 ADA) to the address generated in your terminal.

example: Your main minting address: addr_test1q......
```
## NFT details
Our NFT's will have the following attributes: 
- type
- health
- speed
- defense
- attack

See example on Cardano Preprod: https://preprod.cexplorer.io/tx/2094d4a9ffd8b8633d73a2c282ba287b89ddf511a5dd478c7ca13c90e7938152/metadata#data