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
        return this_sample

    def _sample_one_parameter(self):
        """Sample an ensemble specified by a single parameter"""
        logging.info('sampling along a parameter axis')

        # determine whether we are on a gamma, beta, theta, or alpha axis
        param_id = [p is not None for p in self._get_param_list()].index(True)

        if param_id==0:
            this_sample = self._sample_one_parameter_gamma()
        elif param_id<=4:
            this_sample = self._sample_one_parameter_beta()
        elif param_id<=7:
            this_sample = self._sample_one_parameter_theta()
        else:
            this_sample = self._sample_one_parameter_alpha()
            
        return this_sample

    def _sample_one_parameter_gamma(self):
        sample = np.random.rand(self.L, self.L)
        return sample < (1+self.gamma)/2
        
    def _get_param_list(self):
        return [self.gamma, self.beta1, self.beta2, self.beta3, self.beta4,
                self.theta1, self.theta2, self.theta3, self.alpha]
