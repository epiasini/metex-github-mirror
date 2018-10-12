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

        if sum([param is not None for param in self._get_param_list()]) > 1:
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
            this_sample = self._sample_one_parameter_gamma()
        elif param_id<=4:
            this_sample = self._sample_one_parameter_beta(beta=self._get_param_list()[param_id])
            # TODO: rotate if needed
        elif param_id<=7:
            this_sample = self._sample_one_parameter_theta()
            # TODO: rotate if needed
        else:
            this_sample = self._sample_one_parameter_alpha()
            
        return this_sample

    def _sample_one_parameter_gamma(self):
        sample = np.random.rand(self.L, self.L)
        return sample < (1+self.gamma)/2

    def _sample_one_parameter_beta(self, beta, L=None):
        if L is None:
            L = self.L
            
        sample = np.random.randint(2, size=(L,1)).astype(np.bool)
        for j in range(1,L):
            # the parity array tells us if the number of ones in a
            # given glider is even (in which case the corresponding
            # value of parity is False) or odd (in which case it's
            # True)
            parity = np.random.rand(self.L, 1) > (1 + beta)/2
            sample = np.concatenate((sample, np.logical_xor(sample[:,j-1].reshape(L,1),parity)), axis=1)

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

    

        
