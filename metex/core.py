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

import os.path
import numpy as np
from matplotlib import pyplot as plt

import logging

class Texture():
    def __init__(self, height, width=None, gamma=None, beta1=None, beta2=None, beta3=None, beta4=None,
                 theta1=None, theta2=None, theta3=None, theta4=None, alpha=None):

        self.height = height
        if width is None:
            logging.info('only one dimension was specified. Defining a square texture.')
            self.width = height
        else:
            self.width = width
        
        self.gamma = gamma
        self.beta1 = beta1 # β—
        self.beta2 = beta2 # β|
        self.beta3 = beta3 # β\
        self.beta4 = beta4 # β/
        self.theta1 = theta1 # θ◢
        self.theta2 = theta2 # θ◤
        self.theta3 = theta3 # θ◥
        self.theta4 = theta4 # θ◣
        self.alpha = alpha

        n_nonzero_params = sum([param is not None for param in self._get_param_list()])
        if n_nonzero_params == 0:
            self.gamma = 0
        elif n_nonzero_params > 1:
            raise NotImplementedError()


        
    def sample(self):
        this_sample = self._sample_one_parameter()
        return TextureSample(this_sample)

    def generate_sample_batch(self, n_samples, folder, prefix='', **kwargs):
        for n in range(n_samples):
            s = self.sample()
            s.saveplot(fname='{}{}.png'.format(os.path.join(folder, prefix), n), **kwargs)

    def _sample_one_parameter(self):
        """Sample an ensemble specified by a single parameter"""
        logging.info('sampling along a parameter axis')

        # determine whether we are on a gamma, beta, theta, or alpha axis
        param_id = [p is not None for p in self._get_param_list()].index(True)

        if param_id==0:
            this_sample = self._sample_gamma()
        elif param_id<=4:
            beta = self._get_param_list()[param_id]
            if param_id == 1:
                this_sample = self._sample_beta_horizontal(beta)
            elif param_id==2:
                this_sample = self._sample_beta_vertical(beta)
            elif param_id in [3,4]:
                this_sample = self._sample_beta_diagonal(beta)
                if param_id==4:
                    this_sample = this_sample[:,::-1]
            return this_sample
        elif param_id<=8:
            theta = self._get_param_list()[param_id]
            # baseline is θ◢
            this_sample = self._sample_theta(theta)
            if param_id==6:
                # this is the case θ◤
                this_sample = this_sample[::-1,::-1]
            if param_id==7:
                # this is θ◥
                this_sample = this_sample[::-1,:]
            if param_id==8:
                # this is θ◣
                this_sample = this_sample[:,::-1]
        else:
            this_sample = self._sample_alpha()
            
        return this_sample

    def _sample_gamma(self):
        sample = np.random.rand(self.height, self.width)
        return sample < (1+self.gamma)/2

    def _sample_beta_horizontal(self, beta, swap_dims=False):
        """Generate sample for beta—
        
        The swap_dims argument is only used internally to generate
        textures where height and width are swapped. This is necessary
        to reuse this function to generate beta| textures too.

        """
        (height, width) = (self.height, self.width)
        if swap_dims:
            (height, width) = (width, height)
        sample = np.random.randint(2, size=(height,1)).astype('bool')
        for j in range(1, width):
            # the parity array tells us if the number of ones in a
            # given glider is even (in which case the corresponding
            # value of parity is False) or odd (in which case it's
            # True)
            parity = np.random.rand(height, 1) < (1 + beta)/2
            new_column = ~ np.logical_xor(sample[:,j-1].reshape(height,1),parity)
            sample = np.concatenate((sample, new_column), axis=1)
        return sample

    def _sample_beta_vertical(self, beta):
        """Generate sample for beta|.

        This is done by sampling for beta— for a texture with swapped
        height and width, and then transposing the resulting array.

        """
        sample = self._sample_beta_horizontal(beta, swap_dims=True).T
        return sample

    def _sample_beta_diagonal(self, beta):
        """Generate sample for beta\ """
        sample = np.random.randint(2, size=(self.height,1)).astype('bool')
        for j in range(1, self.width):
            parity = np.random.rand(self.height-1, 1) < (1 + beta)/2
            new_column = np.zeros((self.height,1), dtype='bool')
            new_column[0] = np.random.randint(2) # elements of the first row do not complete any glider, hence they are always generated randomly
            new_column[1:] = ~ np.logical_xor(sample[:-1,j-1].reshape(self.height-1,1),parity)
            sample = np.concatenate((sample, new_column), axis=1)
        return sample

    def _sample_theta(self, theta):
        """Generate sample for theta◿"""
        sample = np.random.randint(2, size=(self.height,self.width)).astype('bool')
        for j in range(1, self.width):
            for i in range(1, self.height):
                parity = np.random.rand() < (1+theta)/2
                sample[i,j] = sample[i,j-1] ^ sample[i-1,j] ^ parity
        return sample

    def _sample_alpha(self):
        sample = np.random.randint(2, size=(self.height,self.width)).astype('bool')
        for j in range(1, self.width):
            for i in range(1, self.height):
                parity = np.random.rand() < (1+self.alpha)/2
                sample[i,j] = ~ sample[i,j-1] ^ sample[i-1,j-1] ^ sample[i-1,j] ^ parity
        return sample

        
    def _get_param_list(self):
        return [self.gamma, self.beta1, self.beta2, self.beta3, self.beta4,
                self.theta1, self.theta2, self.theta3, self.theta4, self.alpha]


class TextureSample(np.ndarray):
    """Maximum entropy texture sample

    This is implemented as a subclass of ndarray - see
    https://numpy.org/doc/stable/user/basics.subclassing.html for the
    technical details.

    """

    def __new__(cls, input_array):
        # Input array is an ndarray instance
        
        # Cast to be our class type
        obj = np.asarray(input_array).view(cls)

        # Add any attributes specific to our class

        # Return the newly created object
        return obj

    def __array_finalize__(self, obj):
        if obj.ndim == 2:
            self.proportions = obj.shape[1]/obj.shape[0]
        else:
            self.proportions = None

    def __str__(self):
        """Standard method for string representation

        Note that Unicode characters are used to support
        pretty-printing of the texture, even in the terminal.

        """
        character_conversion = np.where(self, '⬜', '⬛')
        string = ''
        for i,row in enumerate(character_conversion):
            string = '\n'.join((string, ''.join(row)))
        return string

    def plot(self, ax=None, figsize=None):
        if ax is None:
            if figsize is None:
                figsize = (10*self.proportions, 10) # note this is (width, height), while in the rest of the code we typically put height before width
            fig = plt.figure(figsize=figsize)
            ax = plt.Axes(fig, [0, 0, 1, 1]) # note that this is [left, bottom, with, height]
            fig.add_axes(ax)
            
        ax.imshow(self, interpolation='None', cmap='binary_r', vmin=0, vmax=1)
        ax.axis('off')

        return fig, ax

    def saveplot(self, fname, resolution=3000):
        """Save texture sample to png file on disk.

        resolution is the number of total pixels per side of the image
        (i.e. the image will be saved at resolution x resolution
        pixels).

        """
        if plt.rcParams['interactive']:
            was_interactive = True
            plt.ioff()
        else:
            was_interactive = False

        fig, ax = self.plot(figsize=(self.proportions, 1))
        fig.savefig(fname, dpi=resolution)
        plt.close(fig)

        if was_interactive:
            plt.ion()
    


    

        
