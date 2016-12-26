# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import, unicode_literals

from gymkit.agent.gym_agent import GymKitAgent


class RandomAgent(GymKitAgent):
    def __init__(self, env):
        super().__init__(env)

    def act(self, observation):
        return self.env.action_space.sample()
