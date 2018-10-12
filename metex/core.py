import numpy as np
import logging

class Texture():
    def __init__(self, L, gamma=None, beta1=None, beta2=None, beta3=None, beta4=None,
                 theta1=None, theta2=None, theta3=None, alpha=None):

        self.L = L
        
        self.gamma = gamma
        self.beta1 = beta1
        self.beta2 = beta2
        self.beta3 = beta3
        self.beta4 = beta4
        self.theta1 = theta1
        self.theta2 = theta2
        self.theta3 = theta3
        self.alpha = alpha

        n_nonzero_params = sum([param is not None for param in self._get_param_list()])
        if n_nonzero_params == 0:
            self.gamma = 0
        elif n_nonzero_params > 1:
            raise NotImplementedError()


        
    def sample(self):
        this_sample = self._sample_one_parameter()
        return TextureSample(this_sample)

    def _sample_one_parameter(self):
        """Sample an ensemble specified by a single parameter"""
        logging.info('sampling along a parameter axis')

        # determine whether we are on a gamma, beta, theta, or alpha axis
        param_id = [p is not None for p in self._get_param_list()].index(True)

        if param_id==0:
            this_sample = self._sample_gamma()
        elif param_id<=4:
            beta = self._get_param_list()[param_id]
            if param_id in [1,2]:
                this_sample = self._sample_beta_horizontal(beta)
                if param_id==2:
                    this_sample = this_sample.T
            if param_id in [3,4]:
                this_sample = self._sample_beta_diagonal(beta)
                if param_id==4:
                    this_sample = this_sample[:,::-1]
            return this_sample
        elif param_id<=7:
            theta = self._get_param_list()[param_id]
            this_sample = self._sample_theta(theta)
            if param_id==6:
                # this is the case theta◤
                this_sample = this_sample[::-1,::-1]
            if param_id==7:
                # this is theta◥
                this_sample = this_sample[::-1,:]
        else:
            this_sample = self._sample_alpha()
            
        return this_sample

    def _sample_gamma(self):
        sample = np.random.rand(self.L, self.L)
        return sample < (1+self.gamma)/2

    def _sample_beta_horizontal(self, beta):
        sample = np.random.randint(2, size=(self.L,1)).astype(np.bool)
        for j in range(1, self.L):
            # the parity array tells us if the number of ones in a
            # given glider is even (in which case the corresponding
            # value of parity is False) or odd (in which case it's
            # True)
            parity = np.random.rand(self.L, 1) > (1 + beta)/2
            new_column = np.logical_xor(sample[:,j-1].reshape(self.L,1),parity)
            sample = np.concatenate((sample, new_column), axis=1)
        return sample

    def _sample_beta_diagonal(self, beta):
        """Generate sample for beta\ """
        sample = np.random.randint(2, size=(self.L,1)).astype(np.bool)
        for j in range(1, self.L):
            parity = np.random.rand(self.L-1, 1) > (1 + beta)/2
            new_column = np.zeros((self.L,1), dtype=np.bool)
            new_column[0] = np.random.randint(2) # elements of the first row do not complete any glider, hence they are always generated randomly
            new_column[1:] = np.logical_xor(sample[:-1,j-1].reshape(self.L-1,1),parity)
            sample = np.concatenate((sample, new_column), axis=1)
        return sample

    def _sample_theta(self, theta):
        """Generate sample for theta◿"""
        sample = np.random.randint(2, size=(self.L,self.L)).astype(np.bool)
        for j in range(1, self.L):
            for i in range(1, self.L):
                parity = np.random.rand() > (1+theta)/2
                sample[i,j] = sample[i,j-1] ^ sample[i-1,j] ^ parity
        return sample

    def _sample_alpha(self):
        sample = np.random.randint(2, size=(self.L,self.L)).astype(np.bool)
        for j in range(1, self.L):
            for i in range(1, self.L):
                parity = np.random.rand() > (1+self.alpha)/2
                sample[i,j] = sample[i,j-1] ^ sample[i-1,j-1] ^ sample[i-1,j] ^ parity
        return sample

        
    def _get_param_list(self):
        return [self.gamma, self.beta1, self.beta2, self.beta3, self.beta4,
                self.theta1, self.theta2, self.theta3, self.alpha]


class TextureSample(np.ndarray):

    def __new__(cls, input_array):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None: return

    def __str__(self):
        character_conversion = np.where(self, '⬜', '⬛')
        string = ''
        for i,row in enumerate(character_conversion):
            string = '\n'.join((string, ''.join(row)))
        return string

    

        
