traindt

Perfect 👌 You want to see how a **Decision Tree (like J48)** is constructed *manually* using **Information Gain (IG)** and **Gini Index (GI)**. Let’s do this step by step with the **German Credit dataset idea**, but I’ll show you the calculation process clearly so you can repeat it for any attribute.

---

# 🔹 Step 1: Recall the formulas

### (a) **Entropy & Information Gain**

* Entropy of dataset $S$:

$$
Entropy(S) = - \sum_{i=1}^{c} p_i \log_2 p_i
$$

where $p_i$ = proportion of class $i$.

* Information Gain of attribute $A$:

$$
IG(S, A) = Entropy(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} \times Entropy(S_v)
$$

where $S_v$ = subset with attribute $A = v$.

### (b) **Gini Index**

* For dataset $S$:

$$
Gini(S) = 1 - \sum_{i=1}^{c} p_i^2
$$

* For attribute $A$:

$$
Gini\_index(A) = \sum_{v \in Values(A)} \frac{|S_v|}{|S|} \times Gini(S_v)
$$

---

# 🔹 Step 2: Take a sample (mini German Credit subset)

Suppose we have **10 applicants** with `checking_status` and `class (good/bad)`:

| Applicant | checking\_status | Class |
| --------- | ---------------- | ----- |
| 1         | <0 DM            | Bad   |
| 2         | <0 DM            | Bad   |
| 3         | <0 DM            | Good  |
| 4         | 0–200 DM         | Good  |
| 5         | 0–200 DM         | Good  |
| 6         | 0–200 DM         | Bad   |
| 7         | no checking      | Good  |
| 8         | no checking      | Good  |
| 9         | no checking      | Bad   |
| 10        | no checking      | Good  |

👉 Totals: **6 Good, 4 Bad**.

---

# 🔹 Step 3: Calculate Entropy of the whole dataset

$$
p_{good} = 6/10 = 0.6, \quad p_{bad} = 4/10 = 0.4
$$

$$
Entropy(S) = -(0.6 \log_2 0.6 + 0.4 \log_2 0.4)
$$

$$
= -(0.6 \times -0.737 + 0.4 \times -1.322)
= 0.971
$$

So, **Entropy(S) = 0.971**.

---

# 🔹 Step 4: Entropy of subsets for `checking_status`

### Case 1: `<0 DM` (3 samples: 1 Good, 2 Bad)

$$
p_{good} = 1/3, \; p_{bad} = 2/3
$$

$$
Entropy = -(1/3 \log_2 1/3 + 2/3 \log_2 2/3)
= 0.918
$$

### Case 2: `0–200 DM` (3 samples: 2 Good, 1 Bad)

$$
p_{good} = 2/3, \; p_{bad} = 1/3
$$

Entropy = same as above = **0.918**.

### Case 3: `no checking` (4 samples: 3 Good, 1 Bad)

$$
p_{good} = 3/4, \; p_{bad} = 1/4
$$

$$
Entropy = -(0.75 \log_2 0.75 + 0.25 \log_2 0.25)
= 0.811
$$

---

# 🔹 Step 5: Weighted Entropy for attribute

$$
Entropy(A) = \frac{3}{10}(0.918) + \frac{3}{10}(0.918) + \frac{4}{10}(0.811)
$$

$$
= 0.275 + 0.275 + 0.324
= 0.874
$$

---

# 🔹 Step 6: Information Gain

$$
IG(S, checking\_status) = Entropy(S) - Entropy(A)
$$

$$
= 0.971 - 0.874 = 0.097
$$

So, **IG(checking\_status) ≈ 0.10**.

---

# 🔹 Step 7: Gini Index

### Parent node (whole dataset):

$$
Gini(S) = 1 - (0.6^2 + 0.4^2) = 1 - (0.36 + 0.16) = 0.48
$$

### Subsets:

* `<0 DM` (1 Good, 2 Bad):

$$
Gini = 1 - ((1/3)^2 + (2/3)^2) = 0.444
$$

* `0–200 DM` (2 Good, 1 Bad):

$$
Gini = 0.444
$$

* `no checking` (3 Good, 1 Bad):

$$
Gini = 1 - (0.75^2 + 0.25^2) = 0.375
$$

### Weighted Gini:

$$
Gini(A) = \frac{3}{10}(0.444) + \frac{3}{10}(0.444) + \frac{4}{10}(0.375)
$$

$$
= 0.133 + 0.133 + 0.150 = 0.416
$$

### Gini Gain = Parent – Child

$$
= 0.480 - 0.416 = 0.064
$$

---

# ✅ Final Notes

* For our toy example:

  * **Information Gain (IG) = 0.10**
  * **Gini Gain = 0.064**
* In building a Decision Tree, Weka’s J48 uses **Information Gain Ratio**, while CART (not J48) uses **Gini Index**.

---

👉 Do you want me to **repeat this manual calculation for another attribute** (like `credit_history` or `savings_status`) using a mini subset of your dataset, so you see how attributes are compared and the **best split chosen**?
