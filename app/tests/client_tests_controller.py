from datetime import datetime

import pytest
from bson import ObjectId
from httpx import AsyncClient, ASGITransport
from pymongo import AsyncMongoClient
from testcontainers.mongodb import MongoDbContainer

from app.database_conn.database_conn_mongodb import get_session_mongo
from app.main import app

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope="session")
def mongo_container():
    with MongoDbContainer("mongo:7") as mongo:
        yield mongo


@pytest.fixture
async def mongo_db(mongo_container):
    uri = mongo_container.get_connection_url()

    client = AsyncMongoClient(uri)
    db = client["test_db"]

    await db.clients.create_index("email", unique=True)
    await db.clients.create_index("document", unique=True)

    yield db

    await client.drop_database("test_db")
    await client.close()


@pytest.fixture
async def client(mongo_db):
    async def override_get_db():
        yield mongo_db

    app.dependency_overrides[get_session_mongo] = override_get_db

    transport = ASGITransport(app=app)

    async with AsyncClient(
            transport=transport,
            base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_create_client_success(client):
    response = await client.post("/clients", json={
        "name": "Davi",
        "email": "davi@email.com",
        "document": "123231546"
    })

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_client_invalid_document(client):
    response = await client.post("/clients", json={
        "name": "Davi",
        "email": "davi@email.com",
        "document": "a123231546"
    })

    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'Value error, Tamanho do campo é inválido'


@pytest.mark.asyncio
async def test_create_client_duplicated_document(client, mongo_db, caplog):
    await mongo_db.clients.insert_one({
        "name": "Davi",
        "email": "davi@email.com",
        "document": "123231546",
        "active": True,
        "created_at": datetime.now()
    })

    response = await client.post(
        "/clients",
        json={
            "name": "Davi",
            "email": "davi@email.com",
            "document": "123231546"
        }
    )

    assert response.status_code == 500


@pytest.mark.asyncio
async def test_get_all_clients_returns_two(client, mongo_db):
    await mongo_db.clients.insert_many([
        {
            "name": "Cliente 1",
            "email": "cliente1@email.com",
            "document": "123456789",
            "active": True,
            "created_at": datetime.now()
        },
        {
            "name": "Cliente 2",
            "email": "cliente2@email.com",
            "document": "222",
            "active": True,
            "created_at": datetime.now()
        }
    ])

    response = await client.get("/clients")

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, list)
    assert len(body) == 2

@pytest.mark.asyncio
async def test_get_client_by_id(client, mongo_db):
    inserted = await mongo_db.clients.insert_one({
        "name": "Cliente Teste",
        "email": "teste@email.com",
        "document": "123456789",
        "active": True,
        "created_at":datetime.now()
    })

    client_id = str(inserted.inserted_id)

    response = await client.get(f"/clients/{client_id}")

    assert response.status_code == 200

    body = response.json()
    assert body["name"] == "Cliente Teste"
    assert body["email"] == "teste@email.com"
    assert body["document"] == "123456789"
    assert body["active"] is True

@pytest.mark.asyncio
async def test_update_client_by_id(client, mongo_db):
    inserted = await mongo_db.clients.insert_one({
        "name": "Nome Antigo",
        "email": "antigo@email.com",
        "document": "123456789",
        "active": True,
        "created_at": datetime.now()
    })

    client_id = str(inserted.inserted_id)

    response = await client.put(
        f"/clients/{client_id}",
        json={
            "name": "Nome Novo",
            "email": "novo@email.com",
            "document": "987654321"
        }
    )

    assert response.status_code == 200

    updated = await mongo_db.clients.find_one(
        {"_id": ObjectId(client_id)}
    )

    assert updated["name"] == "Nome Novo"
    assert updated["email"] == "novo@email.com"
    assert updated["document"] == "987654321"
    assert updated["active"] is True

@pytest.mark.asyncio
async def test_change_client_activation_status(client, mongo_db):
    inserted = await mongo_db.clients.insert_one({
        "name": "Cliente",
        "email": "cliente@email.com",
        "document": "123456789",
        "active": True,
        "created_at": datetime.now()
    })

    client_id = str(inserted.inserted_id)

    response = await client.patch(f"/clients/{client_id}")

    assert response.status_code == 200

    updated = await mongo_db.clients.find_one(
        {"_id": ObjectId(client_id)}
    )

    assert updated["active"] is False

@pytest.mark.asyncio
async def test_delete_client_by_id(client, mongo_db):
    inserted = await mongo_db.clients.insert_one({
        "name": "Cliente",
        "email": "delete@email.com",
        "document": "123456789",
        "active": True,
        "created_at": datetime.now()
    })

    client_id = str(inserted.inserted_id)

    response = await client.delete(f"/clients/{client_id}")

    assert response.status_code == 200

    deleted = await mongo_db.clients.find_one(
        {"_id": ObjectId(client_id)}
    )

    assert deleted is None
