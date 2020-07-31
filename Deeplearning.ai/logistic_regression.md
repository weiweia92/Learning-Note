Logistic regression is binary classification.

## Logistic loss function

$ L(\hat{y}, y)=-(y\log{\hat{y}}+(1-y)\log{(1-\hat{y})}) $  
If y=1: $L(\hat{y}, y)=-\log \hat{y}$ $\longleftarrow$ want $\log \hat{y}$ large, want $\hat{y}$ large  

If y=0: $L(\hat{y}, y)=-\log (1-\hat{y})$ $\longleftarrow$ want $\log 1-\hat{y}$ large, want $\hat{y}$ small   

### Why cost function use cross entropy instead of MSE?
Because MSE is not convex function,it has multiple local optimal solution,but cross entropy is convex function,it has only one optimal solution.

### What is the difference between the cost function and the loss function for logistic regression?
The loss function computes the error for a single training example; the cost function is the average of the loss functions of the entire training set.  
Want to find w,b that minimize cost function(J(w, b)).

$ Cost function: J(W, b)=\frac{1}{m}\sum_i^m L(\hat{y}^{(i)}, y^{(i)})=-\frac{1}{m}\sum_i^m [y^{(i)} \log \hat{y}^{(i)}+(1-y^{(i)}\log(1-\hat{y}^{(i)}))] $  

## Gradient Descent

Repeat  
$$
\begin{cases}
W=W - \alpha \times \frac{\partial J(W,b)}{\partial W} \\\\
b=b - \alpha \times \frac{\partial J(W,b)}{\partial b}
\end{cases}
$$

$\alpha : learningrate$

### Note!
When writing code, we use dW instead of $\frac{\partial J(W,b)}{\partial W}$, db instead of $\frac{\partial J(W,b)}{\partial b}$  

## Logistic regression derivatives(求导)

### Backpropagation of one sample 
$$z=w_1x_1+w_2x_2+b\rightarrow a=\sigma{z} \rightarrow L(a,y)$$  
Because logistic regression is binary classification,so loss function is $$ L(a,y)=-(y\log{a}+(1-y)\log{(1-a)}) $$ 
`da` =$\frac{L(a,y)}{da}$  

`dz` =$\frac{dL(a,y)}{dz}=\frac{dL(a,y)}{da} \frac{da}{dz}=(-\frac{y}{a}+\frac{1-y}{1-a}) a(1-a)=a-y$  

`dw1` =$\frac{\partial L}{\partial w_1}=\frac{dL}{dz} \frac{dz}{dw_1}=x_1 \frac{dL(a,y)}{dz}$  

`dw2` =$\frac{\partial L}{\partial w_2}=\frac{dL}{dz} \frac{dz}{dw_2}=x_2 \frac{dL(a,y)}{dz}$  

`db` =$\frac{\partial L}{\partial b}=\frac{dL}{dz} \frac{dz}{db}=1*\frac{dL(a,y)}{dz}$  

so repeat:  
$w_1:=w_1-\alpha dw_1$  
$w_2:=w_2-\alpha dw_2$  
$b:=b-\alpha db$

### Backpropagation of m samples

$J(W, b)=\frac{1}{m}\sum_i^m L(a^{(i)}, y^{(i)})$  
$a^{(i)}=\hat{y}^{(i)}=\sigma{(z^{(i)})}=\sigma(w^Tx^{(i)}+b)$,$x^{(i)}=\left[
\begin{matrix}
x_1 \\
x_2 \\
\vdots \\
x_n \\
\end{matrix}
\right]
$  
$\frac{J(w,b)}{w_1}=\frac{1}{m}\sum_{i=1}^m \frac{\partial L(a^{(i)},y^{(i)})}{\partial w_1}$, $code:dw_1^{(i)}= \frac{\partial L(a^{(i)},y^{(i)})}{\partial w_1}$  

$\frac{J(w,b)}{w_2}=\frac{1}{m}\sum_{i=1}^m \frac{\partial L(a^{(i)},y^{(i)})}{\partial w_2}$, $code:dw_2^{(i)}= \frac{\partial L(a^{(i)},y^{(i)})}{\partial w_2}$

$\frac{J(w,b)}{b}=\frac{1}{m}\sum_{i=1}^m \frac{\partial L(a^{(i)},y^{(i)})}{\partial b}$, $code:db^{(i)}= \frac{\partial L(a^{(i)},y^{(i)})}{\partial b}$  

Pseudo code  
$J=0;dw_1=0;dw_2=0;db=0$  

$for　i=1　to　m:$  
　　$z^{(i)}=W^Tx^{(i)}+b$
　　$a^{(i)}=\sigma(z^{(i)})$  
　　$J+=-(y^{(i)}\log{a^{(i)}}+(1-y^{(i)})\log{(1-a^{(i)})})$  
　　$dz^{(i)}=a^{(i)}-y^{(i)}$  
　　$dw_1+=x_1^{(i)}dz^{(i)}$  
　　$dw_2+=x_2^{(i)}dz^{(i)}$  
　　$db+=dz^{(i)}$ 
  
$J/=m$

$dw_1/=m$  

$dw_2/=m$  

$db/=m$  

$dw_1=\frac{\partial J}{\partial w_1}$    

repeat:

$w_1:=w_1-\alpha dw_1$  

$w_2:=w_2-\alpha dw_2$  

$b:=b-\alpha db$
