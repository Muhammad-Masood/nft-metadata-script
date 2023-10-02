# Nft metadata generator script
## This is an ALL-IN-ONE NFT SCRIPT which can help you in:
1. Generating complete custom metadata, including attributes or adding rarity.
2. Generating 100% different images/nfts from the indivisual components based upon the rarity.
3. Publishing both of your metadata and collection on-chain in a completely decentralized way, without worrying about third party services.

### Follow the below steps in order to publish your nft collection successfully on-chain:

1. Replace the existing components with yours inside the **components** directory.
2. Replace the existing traits, and weights (rarity percentage) inside **traits.py** with the ones of your nft collection.
2. Assign your traits with the related component file name (inside components) in **traits_file.py**.
3. 
4. Run **generate.py** script to generate the metadata and images collection for your nfts, Running this script will create a new *metadata* and *images*  folder.
5. Run **node .\store.js** script to publish your whole collection.
