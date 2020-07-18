# STATISTICS: Day 0

## 1) Mean, Median, and Mode

### A) Intro and Conventions

- Let **$X$** be a set of numbers, of length **$n$**. Hence, **$x_i$** is the $i^{th}$ element in the set **$X$**.

- Let **$W$** be the set of weights of each element **$x_i$** in **$X$**. Hence, **$w_i$** is the $i^{th}$ element in the set **$W$**, which is the weight of **$x_i$**.

- We assume 0-based indexing in our set of elements.

### B) Mean

$$\mu = \frac{\sum_{i=0}^{n-1} {x_i}}{n}$$

### C) Median

$$
Median =
\begin{cases}
 \left(\frac{n}{2}\right)^{th} \text{term} & \text{if $n$ is odd} \\[2ex]
\frac{{\left(\frac{n}{2}\right)}^{th} \text{term} + {\left(\frac{n}{2}-1\right)}^{th}\text{term}}{2}  & \text{if $n$ is even}
\end{cases}
$$

### D) Mode

- The element(s) that occur(s) most frequently in a data set, is called as **Mode**.

- A set is known as **multi-modal** if it has more than 1 mode.

## 2) Weighted Mean

$$\mu_w = \frac{\sum_{i=0}^{n-1} \left({x_i \times w_i}\right)}{\sum_{i=0}^{n-1}{w_i}}$$

## 3) Precision and Scale

### A) Precision

Precision refers to the number of significant digits in a number, as a total.

### B) Scale

Scale refers to the number of significant digits in a number, but that are only to the right of the decimal point, i.e., in the fractional part.
