from dotenv import load_dotenv
from pycardano import *
from blockfrost import BlockFrostApi, ApiError, ApiUrls,BlockFrostIPFS
import os
from os.path import exists
import requests
import time
import json



########################################################
#######           Loading ENV                    #######
########################################################
load_dotenv()
network = os.getenv('network')
wallet_mnemonic = os.getenv('wallet_mnemonic')
your_wallet_address = os.getenv('your_wallet_address')

########################################################
#######           Define Network                 #######
########################################################

if network=="uzh":
    base_url = "http://cardano20.ifi.uzh.ch"
    cardano_network = Network.TESTNET

# print(base_url)

########################################################
#######           Initiate Blockfrost API        #######
########################################################

api = BlockFrostApi(project_id="testing", base_url=base_url)        
cardano = BlockFrostChainContext(project_id="testing", base_url=base_url)

# cardano.url = base_url


########################################################
#######           Initiate wallet                #######
#######           Derive Address 1               #######
########################################################
new_wallet = crypto.bip32.HDWallet.from_mnemonic(wallet_mnemonic)
payment_key = new_wallet.derive_from_path(f"m/1852'/1815'/0'/0/0")
staking_key = new_wallet.derive_from_path(f"m/1852'/1815'/0'/2/0")
payment_skey = ExtendedSigningKey.from_hdwallet(payment_key)
staking_skey = ExtendedSigningKey.from_hdwallet(staking_key)

main_address=Address(payment_part=payment_skey.to_verification_key().hash(), staking_part=staking_skey.to_verification_key().hash(),network=cardano_network)

print(f"Your main minting address: {main_address}")

try:
    address_balance = api.address(address=main_address)
except Exception as e:
    if e.status_code == 404:
        print("Your wallet is empty, please fund it with ADA")
        exit(1)

    print(str(e))





########################################################
#######           Generate Policy keys           #######
#######           IF it doesn't exist            #######
########################################################
if not exists(f"keys/policy.skey") and not exists(f"keys/policy.vkey"):
    payment_key_pair = PaymentKeyPair.generate()
    payment_signing_key = payment_key_pair.signing_key
    payment_verification_key = payment_key_pair.verification_key
    payment_signing_key.save(f"keys/policy.skey")
    payment_verification_key.save(f"keys/policy.vkey")


########################################################
#######           Initiate Policy                #######
########################################################
policy_signing_key = PaymentSigningKey.load(f"keys/policy.skey")
policy_verification_key = PaymentVerificationKey.load(f"keys/policy.vkey")
pub_key_policy = ScriptPubkey(policy_verification_key.hash())


policy = ScriptAll([pub_key_policy])

policy_id = policy.hash()
policy_id_hex = policy_id.payload.hex()
native_scripts = [policy]


########################################################
#######         Get assets from JSON file        #######
########################################################

if os.path.isfile('assets.json') == False:
    print("Please run 'generate_assets.py' first.")
    exit()


with open('assets.json') as f:
    assets = json.load(f)
    print(assets)

base_name = "CHARACTER"


while len(assets) > 0:
    print("still nft's to mint: {}".format(len(assets)))

    ########################################################
    #######           Initiate TxBuilder             #######
    ########################################################
    builder = TransactionBuilder(cardano)



    ########################################################
    #######           Create empty metadata          #######
    ########################################################
    metadata = {
                721: {  
                    policy_id_hex: {
                        
                    }
                }
            }
    
    my_asset = Asset()
    my_nft = MultiAsset()

    ########################################################
    #######           Loop over assets               #######
    ########################################################

    asset_minted = []

    for asset in assets:

        
        asset_id = asset['id']
        asset_type = asset['type']
        asset_attack = asset['attack']
        asset_speed = asset['speed']
        asset_defense = asset['defense']
        asset_health = asset['health']
        asset_ipfs = asset['ipfs']

        asset_name = f"{base_name}{asset_id:04d}"
        asset_name_bytes = asset_name.encode("utf-8")

        file_name = f"assets/{asset_type}.png"
        mime = "image/png"

        ########################################################
        #######           Fill metadata for asset        #######
        ########################################################
        metadata[721][policy_id_hex][asset_name] = {
                                "name": asset_name,
                                "image": f"ipfs://{asset_ipfs}",
                                "mediaType": mime,
                                "type": asset_type,
                                "attack": asset_attack,
                                "speed": asset_speed,
                                "defense": asset_defense,
                                "health": asset_health                                
                            }
    
        nft1 = AssetName(asset_name_bytes)
        my_asset[nft1] = 1

        asset_minted.append(asset)

    ########################################################
    #######           Add minting asset to TxBiulder #######
    ########################################################
    my_nft[policy_id] = my_asset

    auxiliary_data = AuxiliaryData(AlonzoMetadata(metadata=Metadata(metadata)))

    builder.native_scripts = native_scripts
    builder.auxiliary_data = auxiliary_data
    builder.mint = my_nft   


    ########################################################
    #######         Estimate min-ADA required        #######
    ########################################################
    min_val = min_lovelace(
        cardano, output=TransactionOutput(your_wallet_address, Value(0, my_nft))
    )

    ########################################################
    #######         Add inputs & outputs             #######
    ########################################################
    builder.add_output(TransactionOutput(your_wallet_address, Value(min_val, my_nft)))
    builder.add_input_address(main_address)
    
    try: 

        ########################################################
        #######       Build, Balance, Sign and Submit TX #######
        ########################################################
        signed_tx = builder.build_and_sign([payment_skey, policy_signing_key],change_address=main_address)
        txid = str(signed_tx.id)        
        headers = {'Content-Type': 'application/cbor'}
        response = requests.post("http://cardano20.ifi.uzh.ch:8090/api/submit/tx", data=signed_tx.to_cbor(), headers=headers)
        
        print(f"Submitted TX ID: {txid}")

        for asset in asset_minted:
            assets.remove(asset)

    ########################################################
    #######       Some error handling                #######
    ########################################################        
    except Exception as e:   
        if "BadInputsUTxO" in str(e):
            print("Previous transaction still settling")
        else:
            print("Transaction failed, sleeping 10")
            print(str(e))
        print("If this keeps happening, call for support!")
        time.sleep(10)  


########################################################
#######       ALL DONE!                          #######
########################################################
print(f"Finished minting all NFT's")