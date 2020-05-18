import json
import os
import unittest

import utils
from dispatch import Sarsa

SAMPLE_DIR = os.path.abspath('../samples')


class DispatchTest(unittest.TestCase):
    def setUp(self):
        self.alpha = 2 / (5 * 60)
        self.gamma = 0.9
        self.idle_reward = -2 / (60 * 60)

        with open(os.path.join(SAMPLE_DIR, 'dispatch_observ'), 'r') as f:
            self.dispatch_observ = json.load(f)

    def test_sarsa(self):
        drivers, requests, candidates = utils.parse_dispatch(self.dispatch_observ)
        dispatcher = Sarsa(self.alpha, self.gamma, self.idle_reward)
        for _ in range(3):
            d = dispatcher.dispatch(drivers, requests, candidates)
            assert d

    def test_dql(self):
        drivers, requests, candidates = utils.parse_dispatch(self.dispatch_observ)
        dispatcher = Sarsa(self.alpha, self.gamma, self.idle_reward)
        for _ in range(3):
            d = dispatcher.dispatch(drivers, requests, candidates)
            assert d