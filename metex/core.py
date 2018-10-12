import logging

class Texture():
    def __init__(self, L, gamma=None, beta1=None, beta2=None, beta3=None, beta4=None,
                 theta1=None, theta2=None, theta3=None, alpha=None):

        params = [gamma, beta1, beta2, beta3, beta4, theta1, theta2, theta3, alpha]
        
        if sum([not param is None for param in params]) > 1:
            raise NotImplementedError()

        
        self.gamma = gamma
        self.beta1 = beta1
        self.beta2 = beta2
        self.beta3 = beta3
        self.beta4 = beta4
        self.theta1 = theta1
        self.theta2 = theta2
        self.theta3 = theta3
        self.alpha = alpha
        
    def sample(self):
        this_sample = self._sample_one_parameter()
        return this_sample

    def _sample_one_parameter(self):
        """Sample an ensemble specified by a single parameter"""
        logging.info('sampling along a parameter axis')
        
        
