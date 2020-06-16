### 激活函数总结  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-50-15.png)
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-50-30.png)

深度网络中激活函数的选择对训练过程和任务性能有很大影响。目前，最成功、使用最广泛的激活函数是修正线性单元（Rectified Linear Unit，**ReLU x = max(0,x)**）。尽管出现了很多修正 ReLU 的激活函数，但是无一可以真正替代它。我们提出了一种新型激活函数 **Swish：f(x) = x · sigmoid(x), 其中sigmoid(x)=1/(1+exp(-x))** 。我们在多个难度较高的数据集上进行实验，证明 Swish 在深层模型上的效果优于 ReLU。例如，仅仅使用 Swish 单元替换 ReLU 就能把 Mobile NASNetA 在 ImageNet 上的 top-1 分类准确率提高 0.9%，Inception-ResNet-v 的分类准确率提高 0.6%。Swish 的简洁性及其与 ReLU 的相似性使从业者可以在神经网络中使用 Swish 单元替换 ReLU。不过在 Reddit 论坛上，该激活函数的性能与优点还是有些争议的，有的开发者发现该激活函数很多情况下可以比标准的 ReLU 获得更高的性能，而有些开发者则认为 Swish 激活函数并没有什么新意，我们应该关注于更加基础的研究。  

### swish函数图像:  
![](https://github.com/weiweia92/pictures/blob/master/Screen-Shot-2017-10-18-at-2.39.55-PM.png)
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-10-21.png)
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-11-29.png)
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-23-42.png)

我们的实验证明 Swish 在多个深度模型上的性能持续优于或与 ReLU 函数相匹配。由于训练会受多种因素的影响，我们很难证明为什么一个激活函数会优于另一个。但是我们认为 Swish 无上界有下界、非单调且平滑的特性都是优势  

### Mish  
ReLU和Mish的对比，Mish的梯度更平滑  
**Mish=x * tanh(ln(1+e^x))**  

为什么Mish表现这么好?  
上无边界(即正值可以达到任何高度)避免了由于封顶而导致的饱和。理论上对负值的轻微允许允许更好的梯度流，而不是像ReLU中那样的硬零边界。更重要的是，平滑的激活函数允许更好的信息深入神经网络，从而得到更好的准确性和泛化。

尽管如此，我测试了许多激活函数，它们也满足了其中的许多想法，但大多数都无法执行。这里的主要区别可能是Mish函数在曲线上几乎所有点上的平滑度。

这种通过Mish激活曲线平滑性来推送信息的能力如下图所示，在本文的一个简单测试中，越来越多的层被添加到一个测试神经网络中，而没有一个统一的函数。随着层深的增加，ReLU精度迅速下降，其次是Swish。相比之下，Mish能更好地保持准确性，这可能是因为它能更好地传播信息  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-59-27.png)
更平滑的激活功能允许信息更深入地流动……注意，随着层数的增加，ReLU快速下降。



