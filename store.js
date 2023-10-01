import { NFTStorage, File, Blob } from 'nft.storage'

const NFT_STORAGE_TOKEN = process.env.NFT_STORAGE_KEY;
const client = new NFTStorage({ token: NFT_STORAGE_TOKEN })

