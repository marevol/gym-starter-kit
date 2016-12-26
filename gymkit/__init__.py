import argparse
import logging
import sys

import gym
from gym import wrappers
import os


def parse_args(args):
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('--env-id', dest='env_id', action='store',
                        default='CartPole-v0', help='Select the environment to run')
    parser.add_argument('--try-count', dest='episode_count', action='store',
                        default=10, type=int, help='Specify episode count')
    parser.add_argument('--output', dest='outdir', action='store',
                        default='/tmp/my-agent-results', help='Specify output directory')
    parser.add_argument('--api-key', dest='api_key', action='store',
                        default=None, help='Specify API key for OpenAI')
    parser.add_argument('--agent', dest='agent_name', action='store',
                        default='gymkit.agent.RandomAgent', help='Specify agent class name')
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true',
                        default=False, help='Display debug messages')
    return parser.parse_args(args=args)


def configure_logging(options):
    gym.undo_logger_setup()
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if options.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    return logger


def create_gym_env(options):
    env = wrappers.Monitor(directory=options.outdir, force=True)(gym.make(options.env_id))
    env.seed(0)
    return env


def create_agent(env, options):
    sys.path.insert(0, os.getcwd())
    agent_values = options.agent_name.split('.')
    agent_module = '.'.join(agent_values[:-1])
    agent_name = agent_values[-1]
    mod = __import__(agent_module, globals(), locals(), fromlist=[agent_name])
    class_def = getattr(mod, agent_name)
    return class_def(env.action_space)


def main(args=None):
    options = parse_args(args)

    logger = configure_logging(options)
    env = create_gym_env(options)
    agent = create_agent(env, options)

    logger.info('Observation Space: %s', str(env.observation_space))
    logger.info('Action Space: %s', str(env.action_space))

    # environment loop
    for i in range(options.episode_count):
        reward = 0
        done = False
        ob = env.reset()
        with agent:
            logger.info('Episode %d', i + 1)
            while not done:
                env.render()
                logger.debug('O: %s', str(ob))
                action = agent.act(ob)
                logger.debug('A: %s', str(action))
                ob, reward, done, info = env.step(action)
                agent.fit(ob, reward, done, info)

    env.close()

    if options.api_key is not None:
        logger.info('Upload results from %s', options.outdir)
        gym.upload(options.outdir, api_key=options.api_key)


if __name__ == '__main__':
    sys.exit(main())
