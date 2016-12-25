import argparse
import logging
import sys

import gym


def main(args):
    # logging setup
    gym.undo_logger_setup()
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if args.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Gym environment setup
    env = gym.make(args.env_id)
    env.seed(0)
    env.monitor.start(args.outdir, force=True)

    logger.info('Observation Space: %s', str(env.observation_space))
    logger.info('Action Space: %s', str(env.action_space))

    # Create Agent
    mod = __import__('agent', fromlist=[args.agent_name])
    class_def = getattr(mod, args.agent_name)
    agent = class_def(env.action_space)

    # Environment loop
    for i in range(args.episode_count):
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

    env.monitor.close()

    if args.api_key is not None:
        logger.info('Upload results from %s', args.outdir)
        gym.upload(args.outdir, api_key=args.api_key)


if __name__ == '__main__':
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
                        default='RandomAgent', help='Specify agent class name')
    parser.add_argument('--verbose', '-v', dest='verbose', action='store_true',
                        default=False, help='Display debug messages')
    args = parser.parse_args()

    main(args)
