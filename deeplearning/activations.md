
深度网络中激活函数的选择对训练过程和任务性能有很大影响。目前，最成功、使用最广泛的激活函数是修正线性单元（Rectified Linear Unit，ReLU）。尽管出现了很多修正 ReLU 的激活函数，但是无一可以真正替代它。我们提出了一种新型激活函数 **Swish：f(x) = x · sigmoid(x), 其中sigmoid(x)=1/(1+exp(-x))** 。我们在多个难度较高的数据集上进行实验，证明 Swish 在深层模型上的效果优于 ReLU。例如，仅仅使用 Swish 单元替换 ReLU 就能把 Mobile NASNetA 在 ImageNet 上的 top-1 分类准确率提高 0.9%，Inception-ResNet-v 的分类准确率提高 0.6%。Swish 的简洁性及其与 ReLU 的相似性使从业者可以在神经网络中使用 Swish 单元替换 ReLU。不过在 Reddit 论坛上，该激活函数的性能与优点还是有些争议的，有的开发者发现该激活函数很多情况下可以比标准的 ReLU 获得更高的性能，而有些开发者则认为 Swish 激活函数并没有什么新意，我们应该关注于更加基础的研究。  

### swish函数图像:  
![](https://github.com/weiweia92/pictures/blob/master/Screen-Shot-2017-10-18-at-2.39.55-PM.png)
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-10-21.png)
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-11-29.png)
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-06-16%2020-23-42.png)

我们的实验证明 Swish 在多个深度模型上的性能持续优于或与 ReLU 函数相匹配。由于训练会受多种因素的影响，我们很难证明为什么一个激活函数会优于另一个。但是我们认为 Swish 无上界有下界、非单调且平滑的特性都是优势  

### 


