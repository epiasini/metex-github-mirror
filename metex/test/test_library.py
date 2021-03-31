# Copyright (C) 2021 Eugenio Piasini.
#
# This file is part of metex.
#
# Metex is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Metex is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Metex. If not, see <https://www.gnu.org/licenses/>.

import unittest
import numpy as np

import metex

stat_names = [
    "gamma",
    "beta1",
    "beta2",
    "beta3",
    "beta4",
    "theta1",
    "theta2",
    "theta3",
    "alpha"
]

class TestTextureManipulation(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng()
        self.n_levels_per_stat = 5
        self.n_samples_per_texture = 5
        self.height = 20
        self.width = 15

    def test_texture_generation(self):
        for stat_name in stat_names:
            with self.subTest(stat_name=stat_name):
                stat_levels = 2*(self.rng.random(self.n_levels_per_stat)-0.5)
                for stat_level in stat_levels:
                    with self.subTest(stat_level=stat_level):
                        texture = metex.Texture(
                            height=self.height,
                            width=self.width,
                            **{stat_name : stat_level})
                        for each in range(self.n_samples_per_texture):
                            sample = texture.sample()
                            self.assertEqual(sample.shape, (texture.height, texture.width))

    def test_texture_slicing(self):
        for stat_name in stat_names:
            with self.subTest(stat_name=stat_name):
                stat_levels = 2*(self.rng.random(self.n_levels_per_stat)-0.5)
                for stat_level in stat_levels:
                    with self.subTest(stat_level=stat_level):
                        texture = metex.Texture(
                            height=self.height,
                            width=self.width,
                            **{stat_name : stat_level})
                        for each in range(self.n_samples_per_texture):
                            sample = texture.sample()
                            self.assertEqual(sample[:,:-5].shape, (texture.height, texture.width-5))
                            self.assertEqual(sample[:-5,:].shape, (texture.height-5, texture.width))

    def test_texture_sum(self):
        for stat_name in stat_names:
            with self.subTest(stat_name=stat_name):
                stat_levels = 2*(self.rng.random(self.n_levels_per_stat)-0.5)
                for stat_level in stat_levels:
                    with self.subTest(stat_level=stat_level):
                        texture = metex.Texture(
                            height=self.height,
                            width=self.width,
                            **{stat_name : stat_level})
                        samples = [texture.sample() for each in range(self.n_samples_per_texture)]
                        sum(samples)
    
        
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
