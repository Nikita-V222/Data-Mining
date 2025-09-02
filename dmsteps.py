dmsteps
---

# 🔹 Week 1

**Q1. List categorical vs real-valued attributes**

**Steps:**

1. Open Weka → Explorer.
2. Go to **Preprocess tab**.
3. Click **Open file** → load `credit-g.arff` (German Credit dataset).
4. On the left panel, select each attribute → below, Weka shows *Type* (Nominal/Numeric).

   * Nominal = categorical.
   * Numeric = real-valued.

👉 Write them into 2 lists.

---

# 🔹 Week 2

**Q2. Crucial attributes & simple rules**

**Steps:**

1. In Explorer → go to **Select attributes tab**.
2. Choose **Attribute Evaluator = InfoGainAttributeEval**.
3. Choose **Search Method = Ranker**.
4. Click **Start**.
5. Weka will rank attributes by importance.

👉 Use the top-ranked ones to make simple rules (e.g., “If checking\_status = no checking → high chance of bad credit”).

---

# 🔹 Week 3

**Q3. Train Decision Tree (J48) on full data**

**Steps:**

1. Go to **Classify tab**.
2. Choose **Classifier → trees → J48**.
3. Test options → select **Use training set**.
4. Click **Start**.
5. In the results pane:

   * See the **Decision Tree output**.
   * Accuracy on training set is shown.

---

# 🔹 Week 4

**Q4. Training accuracy & explanation**

**Steps:**

1. Repeat steps of Q3 (J48 with *Use training set*).
2. Note the **Correctly Classified Instances (%)**.
3. Compare to 100% → explain why it’s lower (noise, overlap).

---

# 🔹 Week 5

**Q5. Cross-validation**

**Steps:**

1. In **Classify tab**.
2. Classifier = **J48**.
3. Test options = **Cross-validation**, folds = 10.
4. Click **Start**.
5. Check accuracy % (slightly lower than training set).

---

# 🔹 Week 6

**Q6. Reduce attributes**

**Steps:**

1. Go to **Preprocess tab**.
2. Select unwanted attributes → click **Remove**. Keep only attributes: 2, 3, 5, 7, 10, 17, and class.
3. Go to **Classify tab** → J48 → Cross-validation.
4. Click **Start** → Check new accuracy.

---

# 🔹 Week 7

**Q7. Train with reduced attributes & compare**

**Steps:**

1. Continue from Q6 (reduced attributes dataset).
2. Run J48 with Cross-validation.
3. Compare tree size + accuracy vs full dataset (Q5).

---

# 🔹 Week 8

**Q8. Simple vs complex Decision Trees (bias vs variance)**

**Steps:**

1. In **Classify tab → J48**.
2. Click on J48 → set **Confidence factor (C)**:

   * Default = 0.25.
   * Try lower (e.g., 0.1) → more complex tree.
   * Try higher (e.g., 0.5) → simpler tree.
3. Run both models → compare tree size + accuracy.

---

# 🔹 Week 9

**Q9. Reduced Error Pruning**

**Steps:**

1. In **Classify tab → J48**.
2. Click J48 → enable option **-R (Reduced error pruning)**.
3. Test option = **Cross-validation (10 folds)**.
4. Click **Start**.
5. Check pruned tree + accuracy.

---

# 🔹 Week 10

**Q10. Convert tree to rules / Compare J48, PART, OneR**

**Steps:**

1. **Decision tree to rules (manual)**: Take your J48 output and rewrite splits as “if–then rules”.
2. **Train PART classifier**:

   * Classifier = `rules → PART`.
   * Cross-validation (10 folds).
   * Click **Start**.
   * Weka shows rules directly.
3. **Train OneR classifier**:

   * Classifier = `rules → OneR`.
   * Cross-validation.
   * Click **Start** → Weka shows rule based on single attribute.
4. Compare accuracies of J48, PART, OneR.

---

# 🔹 Week 11

**Q11. K-Means clustering**

**Steps:**

1. Go to **Cluster tab**.
2. Choose **Clusterer → SimpleKMeans**.
3. Click on it → set `numClusters = 2`.
4. Evaluation → select **Classes to clusters evaluation** (so Weka compares clusters with class labels).
5. Click **Start**.
6. Output: cluster assignment + % correctly matched.

---

# 🔹 Week 12

**Q12. SVM (SMO in Weka)**

**Steps:**

1. Go to **Classify tab**.
2. Choose Classifier = **functions → SMO**.
3. Test option = **Cross-validation (10 folds)**.
4. Click **Start**.
5. Output: Accuracy + confusion matrix.
6. Compare with J48 (Week 5 results).

---

✅ That’s a **clear Weka workflow for all 12 questions**.

Do you want me to also **make a single summary table (Q → Weka Menu Steps → Expected Output)** so you can paste it directly into your report?
