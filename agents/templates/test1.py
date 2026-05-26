import random

from arcengine import FrameData, GameAction, GameState

from ..agent import Agent


class Test1(Agent):
    MAX_ACTIONS = 80

    def is_done(self, frames: list[FrameData], latest_frame: FrameData) -> bool:
        return latest_frame.state is GameState.WIN

    def choose_action(
        self, frames: list[FrameData], latest_frame: FrameData
    ) -> GameAction:
        if latest_frame.state in [GameState.NOT_PLAYED, GameState.GAME_OVER]:
            return GameAction.RESET

        action = random.choice([a for a in GameAction if a is not GameAction.RESET])
        if action.is_complex():
            action.set_data({"x": random.randint(0, 63), "y": random.randint(0, 63)})
        return action
