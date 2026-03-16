
# CNN Kernel Lab: From Filters to Features

## Code for this project

Starter code can be found at:

https://github.com/mbardoe-wellington/ConvolutionDemo3

## What We Have Done So Far

So far you have learned that:

- Images can be represented as **arrays of numbers**
- A **kernel (filter)** can be applied to an image using convolution
- The result of applying a kernel is a **feature map**
- **ReLU** removes negative values and keeps only positive responses

This means a kernel acts like a **pattern detector**.

For example:

- Some kernels detect **vertical edges**
- Some detect **horizontal edges**
- Some detect **corners**
- Some detect **texture**

When a pattern appears strongly in an image, the feature map will contain **large values** in those locations.

---

# Why CNNs Use Max Pooling

After applying a kernel, the feature map is usually the **same size as the image**.

Example:

```
128 × 128 image
↓
apply kernel
↓
128 × 128 feature map
```

But neural networks often want to:

- reduce the amount of data
- keep the **most important signals**
- ignore small shifts in position

This is where **max pooling** comes in.

---

## What Max Pooling Does

Max pooling divides the feature map into small blocks (usually **2×2**) and replaces each block with the **largest value in that block**.

Example:

```
Original 2×2 region

[ 1  4 ]
[ 2  3 ]
```

Max pooling keeps the largest value:

```
[ 4 ]
```

So a **128×128 feature map** becomes:

```
64 × 64 pooled feature map
```

Max pooling keeps the **strongest signal** from each region.

---

## Why This Helps

Max pooling does three important things:

1. **Reduces the size of the data**

```
128×128 → 64×64
```

2. **Keeps the strongest features**

If an edge appears anywhere in the region, pooling preserves it.

3. **Makes the model less sensitive to small shifts**

If an object moves slightly, the pooled map may stay almost the same.

This is why pooling is used in almost every **Convolutional Neural Network (CNN)**.

---

# Turning Feature Maps Into Scores

After pooling, we still have a small image.

To summarize how strongly a kernel responded to an image, we compute a **score**.

In this lab we will use:

```
score = max value in the pooled map
```

This score answers the question:

> Did this kernel detect its pattern strongly anywhere in the image?

Large score → strong match  
Small score → weak match

---

# The Pipeline You Will Build

For each image, your program will perform this process:

```
image
↓
kernel
↓
feature map
↓
ReLU
↓
max pooling
↓
score
```

This process converts an **image into a number** that measures the presence of a pattern.

---

# Your Task

You will build a **tiny feature extractor** using convolution and pooling.

## Step 1 — Design Kernels

Create **three 3×3 kernels**.

Suggestions:

- one edge detector
- one corner detector
- one custom kernel of your own

Try to predict what pattern each kernel will detect.

---

## Step 2 — Apply Kernels to Images

For each image:

1. Apply each kernel using convolution
2. Apply ReLU
3. Apply max pooling
4. Compute a score from the pooled map

Each kernel will produce **one score per image**.

---

## Step 3 — Build Feature Vectors

If you have three kernels, each image will produce:

```
[score1, score2, score3]
```

This list of numbers is called a **feature vector**.

---

## Step 4 — Classify the Images

Use the feature vectors to build a simple rule that predicts the class of an image.

Example ideas:

```
if score1 > score2 → predict class A
else → predict class B
```

or

```
prediction = argmax([score1, score2])
```

You decide the rule.

---

## Step 5 — Evaluate Your Model

Test your rule on all images and compute:

```
accuracy = correct predictions / total images
```

Try improving your kernels to increase accuracy.

---

# Questions to Think About

1. What pattern does each kernel detect?
2. How does max pooling change the feature map?
3. Which kernels produce the most useful scores?
4. Why might multiple kernels be better than one?

---

# Big Idea

You have just built the **first stage of a convolutional neural network**.

CNNs automatically learn many kernels that produce useful **features** for classification.

Pooling helps compress the information while keeping the strongest signals.
