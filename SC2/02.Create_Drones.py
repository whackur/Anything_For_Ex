# unit_typeid.py 참고

import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import HATCHERY, DRONE, LARVA, OVERLORD, LARVATRAIN_DRONE

class MyBot(sc2.BotAI):
    hello = True
    async def on_step(self, iteration): # 모든 step마다 행동을 취함
        if self.hello:
            await self.chat_send("Hello SC2!!!")
            self.hello = False

        larva = self.units(LARVA)

        #대군주 생산
        if self.supply_left < 2 :
            if self.can_afford(OVERLORD):
                await self.do(larva.random.train(OVERLORD))

        # 일벌레 생산
        if self.supply_left >= 1 and self.can_afford(DRONE):
            await self.do(larva.random.train(DRONE))
            

players = [Bot(Race.Zerg,MyBot()), \
    Computer(Race.Terran, Difficulty.Easy)]
sc2.run_game(maps.get("Simple64"), players, realtime = True)