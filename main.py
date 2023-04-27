from pynout import Keys
from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class MyComponent(ApplicationSession):

    async def onJoin(self, details):
        print("Procedure registered")
        registry = Keys()
        key = await self.register(registry)
        for reg in key:
            print("registered", reg.procedure)


if __name__ == '__main__':
    url = environ.get("wick", "ws://localhost:8080/ws")
    realm = "realm1"
    runner = ApplicationRunner(url, realm)
    runner.run(MyComponent)

