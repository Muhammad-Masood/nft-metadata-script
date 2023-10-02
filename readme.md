# Nft metadata generator script

## This is an ALL-IN-ONE NFT SCRIPT which can help you in:

1. Generating complete custom metadata, including attributes or adding rarity.
2. Generating 100% different images/nfts from the indivisual components based upon the rarity.
3. Publishing both of your metadata and collection on-chain in a completely decentralized way, without worrying about third party services.

### Follow the below steps in order to publish your nft collection successfully on-chain:

#### Pre-requisites

We are using nft.storage to store our collection.

1. Visit and login
2. Create your api key and copy that
3. Inside your root folder, create a _.env_ file, create a variable **NFT_STORAGE_KEY**, and store your api key in it.

4. Replace the existing components with yours' inside the **components** directory. Rename the traits folders names inside components.
5. Replace the existing traits, and weights (rarity percentage) inside **traits.py** with the ones of your nft collection.
6. Assign your traits with the related component file name (inside components) in **traits_file.py**.
7. Replace the paths of traits files in **generate.py**.
8. Run **generate.py** script to generate the metadata and images collection for your nfts, Running this script will create a new _metadata_ and _images_ folder.
9. Run **node .\store.js** script to publish your whole collection.
