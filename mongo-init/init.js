db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);

db.createCollection("clients");

db.clients.createIndex(
    { email: 1 },
    { unique: true }
);

db.clients.createIndex(
    { document: 1},
    { unique: true }
);