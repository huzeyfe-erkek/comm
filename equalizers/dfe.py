import numpy as np

class Dfe:
    '''
    Decision Feedback Equalizer
    '''

    def __init__(self, feedforwardTapNum : int, feedbackTapNum : int) -> None:
        self.b = np.zeros(feedforwardTapNum) # Feedforward (FF) taps zero init
        self.a = np.zeros(feedbackTapNum) # Feedback (FB) taps zero init
        self.xOlds = np.zeros(feedbackTapNum)
        return;

    def tapSolutionMmse(self, channelTaps: np.array):
        # Concatenate FF and FB taps
        t = np.r_[self.b, self.a]
        return
