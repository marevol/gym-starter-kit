# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import, unicode_literals


class GymKitAgent(object):
    def __init__(self, env):
        self.env = env

    def act(self, observation):
        return self.env.action_space.sample()

    def fit(self, observation, reward, done, info):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass
