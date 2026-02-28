db = db.getSiblingDB(process.env.MONGO_DB_NAME);

db.clients.createIndex(
  { email: 1 },
  { unique: true }
);