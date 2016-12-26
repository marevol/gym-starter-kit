# Gym Starter Kit

Gym Starter Kit simplifies Agent development for OpenAI Gym.
Using gym-start command, you can run your agent quickly(do not have to write codes for environment).
Therefore, you can foucus on agent development.

## Getting Started

### (Preparetion) Install OpenAI Gym

See [Gym Installation](https://github.com/openai/gym#installation).

### Install gym-starter-kit

    $ pip install gym-starter-kit

If you want to install development version, run as below:

    $ git clone https://github.com/marevol/gym-starter-kit.git
    $ cd gym-starter-kit
    $ pip install .

### Create Your Agent

Gym Starter Kit runs your agent in OpenAI Gym.
For example, you can write the following agent in my\_agent.py:

    class MyAgent(object):
        def __init__(self, env):
            self.env = env

        # Return your action for the observation
        def act(self, observation):
            return self.env.action_space.sample()

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

To specify an environment, use --env-id option:

    $ gym-start --env-id Pong-v0

To check available options, run as below:

    $ gym-start -h

## Examples

See [Gym Starter Kit Example](https://github.com/marevol/gym-starter-kit-example).
