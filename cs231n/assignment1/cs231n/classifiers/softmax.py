from builtins import range
import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_class = W.shape[1]
    num_train = X.shape[0]
    buf_e = np.zeros(num_class) #np.生成的都是array吗?
    
    for i in range(num_train):
        f = np.dot(X[i], W)
        f -= np.max(f) #?
        loss += np.log(np.sum(np.exp(f))) - f[y[i]]
        dW[:, y[i]] -= X[i]
        for j in range(num_class):
            dW[:, j] += np.exp(f[j]) / np.sum(np.exp(f)) * X[i]
    loss = loss / num_train + 0.5 * reg * np.sum(W * W)
    dW = dW / num_train + reg * W
        
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_train = X.shape[0]
    f = np.dot(X, W) # f.shape = N, C
    f -= f.max(axis=1).reshape(num_train,1) #axis=1--->compare each element of row
    s = np.exp(f).sum(axis=1)
    # (np.log(s)-f[range(num_train),y]).sum()
    loss += np.log(s).sum() - f[range(num_train), y].sum()

    counts = np.exp(f) / s.reshape(num_train, 1)
    counts[range(num_train), y] -= 1
    dW = np.dot(X.T, counts)

    loss = loss / num_train + 0.5 * reg * np.sum(W * W)
    dW = dW / num_train + reg * W
    

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
