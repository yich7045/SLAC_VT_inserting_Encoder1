import gym
import minitouch.env

def make_dmc():
    env = gym.make("Pushing-v1")
    return env
