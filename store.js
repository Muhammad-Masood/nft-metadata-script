require('dotenv').config();
const { NFTStorage, File, Blob } = require('nft.storage')
const fs = require('fs');

const client = new NFTStorage({ token: process.env.NFT_STORAGE_KEY })

const totalNfts = 200;


// stores indivisual files
// async function storeNft(_nftMetadata) {
//     // async function storeNft() {
//     console.log(_nftMetadata);
//     const metadata = await client.store({ properties: {} });
//     console.log(`Metadata published! ${metadata.url}`);
//     console.log(`Metadata published! ${metadata.data}`);
//     console.log(`Metadata published! ${metadata.ipnft}`);
// }

// store directory

async function storeNftDirectory(files) {
    const cid = await client.storeDirectory(files);
    console.log("cid: ", cid);
    // console.log(files);
}

async function storeNfts() {
    const files = [];
    for (let i = 0; i < totalNfts; i++) {
        const imagePath = `./images/${i}.png`;
        const imageName = i; //tokenId
        const imageFile = new File([await fs.promises.readFile(imagePath)], `${imageName}.png`, { type: 'image/png' });
        files.push(imageFile);
        
        // const data = await fs.promises.readFile(`./metadata/${i}.json`, 'utf-8');
        // const nftMetadata = JSON.parse(data);
        // nftMetadata.image = imageFile;
        // const updatedNftMetadata = JSON.stringify(nftMetadata, null, 2);

        // await fs.promises.writeFile(`./metadata/${i}.json`, updatedNftMetadata, 'utf-8');

        // await storeNft(nftMetadata);
    }
    await storeNftDirectory(files);
    // await update_all_nfts_metadata();
}

async function update_all_nfts_metadata() {
    try {
        for (let i = 0; i < totalNfts; i++) {
            const data = await fs.promises.readFile(`./metadata/${i}.json`, 'utf-8');
            const nftMetadata = JSON.parse(data);
            const image = nftMetadata.image;

            const allNftsMetaData = await fs.promises.readFile('./metadata/all_metadata.json', 'utf-8');
            const allNftsMeta = JSON.parse(allNftsMetaData);
            allNftsMeta[i].image = image;

            const updatedAllNftsMeta = JSON.stringify(allNftsMeta, null, 2);
            await fs.promises.writeFile('./metadata/all_metadata.json', updatedAllNftsMeta, 'utf-8');
        }
        console.log("Updated all_nfts_metadata successfully!");
    } catch (err) {
        console.error(err);
    }
}

storeNfts();

// const imageUri = "ipfs://bafybeibdhcrosn2mwiutuq6ailnumwnjpriocyvogzokybebwaxf5nz3qi";

// (async function () {
//     for (let i = 0; i < totalNfts; i++) {
//         const data = await fs.promises.readFile(`./metadata/${i}.json`, 'utf-8');
//         const meta = JSON.parse(data);
//         meta.image = `${imageUri}/${i}.png`;
//         const updatedMeta = JSON.stringify(meta, null, 2);
//         await fs.promises.writeFile(`./metadata/${i}.json`, updatedMeta, 'utf-8');
//     }
//     await update_all_nfts_metadata();
// })();



