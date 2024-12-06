const express = import('express');
import { app } from 'kue';
import { createClient, print } from 'redis';
import { promisify } from 'util';

const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];

function getItemById(id) {
  for (const obj in listProducts) {
    if (obj.id === id) {return obj}
  }
}

// create an app
app = express();

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const stock = getCurrentReservedStockById(req.params.itemId);
  if (stock !== null) {res.json(stock)}
  else {res.json({'status': "Product not found"})}
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.param.itemId;
  obj = getItemById(req.params.itemId);
  if (obj === null) {return res.json({'status': 'Product not found'})}
  if (obj.stock <= 1) {return res.json({'status': "Not enough stock available", 'itemId': itemId})}
  const stock = getCurrentReservedStockById(itemId);
  obj.id = obj.id - 1;
  reserveStockById(itemId, stock);
  return res.json({'status': 'Reservation confirmed', 'itemId': itemId})
});

app.listen(1245);

const client = createClient()

client.on('error', (err) => {
  console.log(`Not conneted with error: ${err}`);
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock, print);
}
// Promisify the client.get function to make it a promise
const get = promisify(client.get).bind(client);

async function getCurrentReservedStockById(itemId) {
  const stock = await get(`item.${itemId}`);
  return stock;
}
