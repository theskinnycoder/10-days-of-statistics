# STATISTICS: Day 0

## 1) Mean, Median, and Mode

### A) Intro and Conventions

- Let **X** be a set of numbers, of length **n**. Hence, **x<sub>i</sub>** is the i<sup>th</sup> element in the set **X**.

- Let **W** be the set of weights of each element **x<sub>i</sub>** in **X**. Hence, **w<sub>i</sub>** is the i<sup>th</sup> element in the set **W**, which is the weight of **x<sub>i</sub>**.

- We assume 0-based indexing in our set of elements.

### B) Mean

<!-- $$\mu = \frac{\sum_{i=0}^{n-1} {x_i}}{n}$$ -->

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_cs&space;\LARGE&space;\mu&space;=&space;\frac{\sum_{i=0}^{n-1}&space;{x_i}}{n}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\fn_cs&space;\LARGE&space;\mu&space;=&space;\frac{\sum_{i=0}^{n-1}&space;{x_i}}{n}" title="\LARGE \mu = \frac{\sum_{i=0}^{n-1} {x_i}}{n}" /></a>

### C) Median

<!-- $$
Median =
\begin{cases}
 \left(\frac{n}{2}\right)^{th} \text{term} & \text{if $n$ is odd} \\[2ex]
\frac{{\left(\frac{n}{2}\right)}^{th} \text{term} + {\left(\frac{n}{2}-1\right)}^{th}\text{term}}{2}  & \text{if $n$ is even}
\end{cases}
$$ -->

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_cs&space;\LARGE&space;Median&space;=&space;\begin{cases}&space;\left(\frac{n}{2}\right)^{th}&space;\text{term}&space;&&space;\text{if&space;$n$&space;is&space;odd}&space;\\[2ex]&space;\frac{{\left(\frac{n}{2}\right)}^{th}&space;\text{term}&space;&plus;&space;{\left(\frac{n}{2}-1\right)}^{th}\text{term}}{2}&space;&&space;\text{if&space;$n$&space;is&space;even}&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\fn_cs&space;\LARGE&space;Median&space;=&space;\begin{cases}&space;\left(\frac{n}{2}\right)^{th}&space;\text{term}&space;&&space;\text{if&space;$n$&space;is&space;odd}&space;\\[2ex]&space;\frac{{\left(\frac{n}{2}\right)}^{th}&space;\text{term}&space;&plus;&space;{\left(\frac{n}{2}-1\right)}^{th}\text{term}}{2}&space;&&space;\text{if&space;$n$&space;is&space;even}&space;\end{cases}" title="\LARGE Median = \begin{cases} \left(\frac{n}{2}\right)^{th} \text{term} & \text{if $n$ is odd} \\[2ex] \frac{{\left(\frac{n}{2}\right)}^{th} \text{term} + {\left(\frac{n}{2}-1\right)}^{th}\text{term}}{2} & \text{if $n$ is even} \end{cases}" /></a>

### D) Mode

- The element(s) that occur(s) most frequently in a data set, is called as **Mode**.

- A set is known as **multi-modal** if it has more than 1 mode.

## 2) Weighted Mean

<!-- $$\mu_w = \frac{\sum_{i=0}^{n-1} \left({x_i \times w_i}\right)}{\sum_{i=0}^{n-1}{w_i}}$$ -->

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_cs&space;\LARGE&space;\mu_w&space;=&space;\frac{\sum_{i=0}^{n-1}&space;\left({x_i&space;\times&space;w_i}\right)}{\sum_{i=0}^{n-1}{w_i}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\fn_cs&space;\LARGE&space;\mu_w&space;=&space;\frac{\sum_{i=0}^{n-1}&space;\left({x_i&space;\times&space;w_i}\right)}{\sum_{i=0}^{n-1}{w_i}}" title="\LARGE \mu_w = \frac{\sum_{i=0}^{n-1} \left({x_i \times w_i}\right)}{\sum_{i=0}^{n-1}{w_i}}" /></a>

## 3) Precision and Scale

### A) Precision

Precision refers to the number of significant digits in a number, as a total.

### B) Scale

Scale refers to the number of significant digits in a number, but that are only to the right of the decimal point, i.e., in the fractional part.
