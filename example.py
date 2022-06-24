import asyncio
import aiohttp

from custom_components.sodexo.api import SodexoAPI

async def main():
    async with aiohttp.ClientSession() as session:
        api = SodexoAPI(session)

        username = input("Enter your username/nif...: ")
        password = input("Enter your password.......: ")

        token = await api.login(username, password)
        details = await api.getAccountDetails(token)
        print(details.amount)
        print(details.updated)
        
asyncio.get_event_loop().run_until_complete(main())