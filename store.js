require('dotenv').config();
const { NFTStorage, File, Blob } = require('nft.storage')
const fs = require('fs');

const client = new NFTStorage({ token: process.env.NFT_STORAGE_KEY })

const totalNfts = 200;


// store directory

async function storeNftDirectory(files) {
    const cid = await client.storeDirectory(files);
    return cid;
}


async function storeNftImages() {
    const files = [];
    for (let i = 0; i < totalNfts; i++) {
        const imagePath = `./images/${i}.png`;
        const imageName = i; //tokenId    ---------> Will be shown in ipfs url
        const imageFile = new File([await fs.promises.readFile(imagePath)], `${imageName}.png`, { type: 'image/png' });
        files.push(imageFile);
    }
    const imageCid = await storeNftDirectory(files);
    console.log(`nft images published successfully! ${imageCid}`);
    return imageCid;
}

async function storeNfts() {
    const imgsCid = await storeNftImages();
    // update 'images' inside meta files
    const files = [];
    for (let i = 0; i < totalNfts; i++) {
        const metaPath = `./metadata/${i}.json`;
        const metaName = i; //tokenId
        const data = await fs.promises.readFile(metaPath, 'utf-8');
        const nftMetadata = JSON.parse(data);
        nftMetadata.image = `ipfs://${imgsCid}/${metaName}.png`;
        const updatedNftMetadata = JSON.stringify(nftMetadata, null, 2);

        await fs.promises.writeFile(metaPath, updatedNftMetadata, 'utf-8');

        const metaFile = new File([await fs.promises.readFile(metaPath)], `${metaName}.json`);
        files.push(metaFile);
    }
    const metaCid = await storeNftDirectory(files);
    console.log(`metadata published successfully! ${metaCid}`);
}

storeNfts();


