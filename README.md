# Gym Starter Kit

This repository is Agent Development Environment for OpenAI Gym.

## Getting Started

### Install gym-starter-kit

    $ pip install gym-starter-kit

If you want to install development version, run as below:

    $ git clone https://github.com/marevol/gym-starter-kit.git
    $ pip install .

### Create Your Agent

Gym Starter Kit runs your agent in OpenAI Gym.
For example, you can write the following agent in my\_agent.py:

    class MyAgent(object):
        def __init__(self, action_space):
            self.action_space = action_space

        # Return your action for the observation
        def act(self, observation):
            return self.action_space.sample()

        # Learn your action for the observation of act method
        def fit(self, observation, reward, done, info):
            pass

        # Called on Episode start
        def __enter__(self):
            return self

        # Called on Episode end
        def __exit__(self, exception_type, exception_value, traceback):
            pass

### Run Your Agent

    $ gym-start --agent my_agent.MyAgent

