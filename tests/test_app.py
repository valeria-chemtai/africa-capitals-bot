import pytest

from app import app


async def test_root(aiohttp_client) -> None:
    client = await aiohttp_client(app)
    resp = await client.get('/api')
    assert resp.status == 200
    text = await resp.text()
    assert text == 'Welcome to African Nations Capitals bot'
