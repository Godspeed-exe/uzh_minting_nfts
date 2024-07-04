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

- A Cardano mnemonic - this can be any 24 word mnemonic

## How to Run?

Clone the repo
```bash
git clone https://github.com/Godspeed-exe/uzh_minting_nfts
```

Move into the folder
```bash
cd uzh_minting_nfts
```
Copy .env-example to .env
```bash
cp .env-example .env
```

Update .env - only wallet_mnemonic
```bash
wallet_mnemonic='your_wallet_mnemonic_here'
```

Generate some random assets based on the content of [all_assets.json](all_assets.json)
```bash
python generate_assets.py
```
Mint the assets to your wallet
```bash
python main.py
```

## Possible errors

- Python not installed
```bash
1. Install python 3.x for your OS
2. Make sure Python executable is in your PATH - Google: "adding Python to PATH [your OS here]"
3. Restart your terminal to reload PATH variable
```

- PyCardano not installed
```bash
pip install pycardano
```
- Blockfrost not installed
```bash
pip install blockfrost-python
```

## NFT details
Our NFT's will have the following attributes: 
- type
- health
- speed
- defense
- attack

See example on Cardano Preprod: https://preprod.cexplorer.io/tx/2094d4a9ffd8b8633d73a2c282ba287b89ddf511a5dd478c7ca13c90e7938152/metadata#data