import { createClient } from 'redis';
const RedisStore = require('connect-redis');

const client = createClient()
console.log(client)

client.on('error', (err) => { 
  console.log(`Redis client not connected to the server: ${err.message}`);
})

client.on('connect', () => { console.log('Redis client connected to the server') });

client.connect()
  .then(() => {
    console.log('Redis client connected to the server');
  }).catch((err) => {
    console.error(`Error connecting to Redis: ${err.message}`);
  })

const redisStore = new RedisStore({
    client: client,
    prefix: "prefix:",
});

