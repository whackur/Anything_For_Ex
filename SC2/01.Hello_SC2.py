import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

class MyBot(sc2.BotAI):
    hello = True
    async def on_step(self, iteration): # 모든 step마다 행동을 취함
        if self.hello:
            await self.chat_send("Hello SC2!!!")
            self.hello = False

players = [Bot(Race.Protoss,MyBot()), \
    Computer(Race.Zerg, Difficulty.Easy)]
sc2.run_game(maps.get("Simple64"), players, realtime = True)