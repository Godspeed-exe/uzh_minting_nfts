## About The Repo

This repo contains an example of minting NFT's on Cardano with PyCardano. In this example we'll also use the flexibility of Cardano's metadata to add extra attributes to our NFT's. The goal could be to create game characters.

For this example we'll be minting X amount of NFT's. We'll:
1. generate and store the collection on a MySQL database.
2. loop over the records in the database and create NFT's.

## Requirements
- A MySQL database 
- A Blockfrost API key (https://blockfrost.io/dashboard)
- A Blockfrost IPFS API key
- A Cardano mnemonic

## NFT details
Our NFT's will have attributes: 
- type
- health
- speed
- defense
- attack