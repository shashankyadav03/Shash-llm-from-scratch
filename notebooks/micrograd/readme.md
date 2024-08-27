

# Micrograd

A tiny Autograd engine (with a bite! 😊). This project implements backpropagation (reverse-mode autodiff) over a dynamically built Directed Acyclic Graph (DAG) and includes a small neural networks library on top of it with a PyTorch-like API. Both components are minimalistic, with about 100 and 50 lines of code respectively. The DAG operates over scalar values, breaking down each neuron into its individual tiny adds and multiplies. Despite its simplicity, this is sufficient to build entire deep neural networks capable of performing binary classification, as demonstrated in the provided notebook. This project is potentially useful for educational purposes.

## Installation

To install the package, use:

```bash
pip install micrograd
```

## Example Usage

Below is a slightly contrived example showcasing several supported operations:

```python
from micrograd.engine import Value

a = Value(-4.0)
b = Value(2.0)
c = a + b
d = a * b + b**3
c += c + 1
c += 1 + c + (-a)
d += d * 2 + (b + a).relu()
d += 3 * d + (b - a).relu()
e = c - d
f = e**2
g = f / 2.0
g += 10.0 / f
print(f'{g.data:.4f}') # prints 24.7041, the outcome of this forward pass
g.backward()
print(f'{a.grad:.4f}') # prints 138.8338, i.e. the numerical value of dg/da
print(f'{b.grad:.4f}') # prints 645.5773, i.e. the numerical value of dg/db
```

## Training a Neural Network

The notebook `nn_propogation_auto.ipynb` provides a full demonstration of training a 2-layer neural network (MLP) for binary classification. This is achieved by:

1. Initializing a neural network from the `micrograd.nn` module.
2. Implementing a simple SVM "max-margin" binary classification loss.
3. Using Stochastic Gradient Descent (SGD) for optimization.


```python
from micrograd import nn
n = nn.Neuron(2)
x = [Value(1.0), Value(-2.0)]
y = n(x)
dot = draw_dot(y)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
