# Day 2

I'm going to do my best to do this day with math, as opposed to converting from `int`s to `str`s for operations such as concatenation and getting the length.

As far as significant Python features used, I did utilize a generator function (`Id.to(self, Id)`).
This was certainly more of an ergonomic choice than anything but still demonstrates the idea well.

## Part 1

We need to be able to find valid IDs in the format `n.n` where `.` represents concatentation of numbers.
Concatentation can also be represented like this: $n.n = n + n * 10^{\lceil\log_{10}(n + 1) \rceil}$, if something more mathematical is valuable.

Note that this representation requires that valid IDs be of even length, which must be true based on the problem statement.

So how do we find valid values for `n` within a range?

Let's call our range `a-b`.

Let's define the set of IDs between $a$ and $b$ as $\Phi(a, b)$.
$$
\Phi(a, b) = \{ n.n ~ | ~ a \leq n.n \leq b ~\land~ n \in \mathbb N\}
$$

If we call our input ranges $R$, then we can express the solution as
$$
S = \sum_{(a, b) \in R} \left[ \sum_{\bar n \in \Phi(a, b)} \bar n \right]
$$

Going through this formalization process helped me reach the following algorithm.

Let's define two functions, `up` and `down` which take a natural number and return the nearest valid ID in the positive and negative directions, respectively.
Note that `down` is not defined for any values below $11$, because that's the lowest valid ID.

Let's also define a function, `kernel`, which takes a valid ID of the form $n.n$ and returns $n$.

Using these helpers, we can write the following function to sum all of the valid IDs within a given range:
```py
def sum_range(a: int, b: int) -> int:
  res = 0
  ap = kernel(up(a))
  bp = 0 if down(b) is None else kernel(down(b))
  for n in range(a, b + 1):
    res += n + n * 10 ** ceil(log10(n + 1))
  return res
```

> Note that iterating over the kernel values between IDs is the same as going through the IDs in increasing order.
> The reasoning for this is pretty simple, but still worth noting.
> *Hint*: consider only the first $n$ in $n.n$.

Now, let's take a look at `up`.

Let's say that the input $x$ can be written as $x_1.x_2$ where $\text{len}(x_1) = \text{len}(x_2)$.
In other words, $x$ is of even length, as all valid IDs are.
We must find a value $n$ such that $n \geq x_1$ and $n \geq x_2$ while maintaining that $\forall n' < n : n'.n' < x_1.x_2$.

If $\text{len}(x)$ is odd, then the next valid ID is just the lowest ID of that length: $n.n \text{ where }n = 10^{(\text{len}(x) + 1) / 2 - 1}$.

The following is a simple implementation of this algorithm.
Proof of correctness is left as an exercise to the reader.

```py
def up(x: int) -> int:
  l = ceil(log10(x))
  if l % 2 == 1:
    # make_id converts a kernel to an ID
    return make_id(10 ** ((l + 1) / 2 - 1))
  
  b = 10 ** ((l + 1) / 2)
  x1 = x // b
  x2 = x % b

  if x2 <= x1:
    return make_id(x1)
  else:
    return make_id(x1 + 1)
```

`down` follows a very similar structure.