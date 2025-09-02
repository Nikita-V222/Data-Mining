
# WEKA Step‑by‑Step Guide for Credit Assessment Lab (12 Tasks)

**Dataset assumed:** `credit-g.arff` (German Credit) – bundled with WEKA (`data/credit-g.arff`).  
**Tool:** WEKA Explorer (GUI).  
**Target (class) attribute:** `class` (values: `good`, `bad`).

---

## Quick Setup (Do this once)
1. Open **WEKA** → **Explorer**.
2. **Preprocess** tab → **Open file…** → select `credit-g.arff`.
3. Bottom-right **Class** drop-down → choose `class`.
4. (Optional but recommended for numeric models) Click **Choose** (Filter) → `unsupervised` → `attribute` → `Standardize` → **Apply**.  
   *When classification is used, you can skip Standardize; for SVM and K-means it helps.*

---

## Q1 — List categorical vs real-valued attributes
**In WEKA**
- **Preprocess** tab → look at **Type** column.

**Answer (for `credit-g.arff`):**
- **Categorical (Nominal):** `checking_status`, `credit_history`, `purpose`, `savings_status`, `employment`, `personal_status`, `other_debtors` (aka `debtors`), `property_magnitude` (aka `property`), `installment_plans`, `housing`, `job`, `telephone`, `foreign_worker`.
- **Real-valued (Numeric):** `duration`, `credit_amount`, `residence_since` (aka `residence`), `age`, `existing_credits`, `num_dependents`.

**What to record:** the two lists above for your report.

---

## Q2 — Pick crucial attributes & write simple English rules
**In WEKA**
1. Go to **Select attributes** tab.
2. **Attribute Evaluator:** choose `InfoGainAttributeEval`.
3. **Search Method:** choose `Ranker` (default).
4. Click **Start** → note the ranked list.

**How to write rules (example)**
- *If `checking_status` is “<0” and `duration` > 24 then risk is higher (bad).*  
- *If `savings_status` is “>=1000” and `credit_history` is “all paid” then risk is lower (good).*

**What to record:** Top 5–7 attributes and 3–5 plain-English rules based on the ranking and common sense.

---

## Q3 — Train a Decision Tree on the full training set (J48)
**In WEKA**
1. **Classify** tab.
2. **Classifier → Choose** → `trees` → `J48`.
3. **Test options:** `Use training set`.
4. Click **Start**.

**What to record**
- `Correctly Classified Instances` (%)
- `Kappa statistic`
- `Confusion Matrix`
- The **tree** (right‑click the run in **Result list** → *Visualize tree* or *Save model*).

**Example output (illustrative)**
```
Correctly Classified Instances       795               79.5 %
Kappa statistic                       0.38
=== Confusion Matrix ===
 a  b   <-- classified as
620  80 | a = good
125 175 | b = bad
```

---

## Q4 — Why not 100% training accuracy?
**In WEKA**
- You already trained on the training set in Q3. The `%` you saw is your training accuracy.

**What to record**
- The training accuracy from Q3 and a short reason: noise/overlap in features, pruning in J48, limited signal, and avoiding overfit.

---

## Q5 — 10‑fold Cross‑Validation with J48
**In WEKA**
1. **Classify** tab with `J48` selected.
2. **Test options:** `Cross-validation` with `10` folds.
3. Click **Start**.

**What to record**
- CV accuracy, Kappa, confusion matrix, tree size.
- Compare with Q3: CV accuracy is usually lower than training accuracy.

**Example output (illustrative)**
```
Correctly Classified Instances       735               73.5 %
Kappa statistic                       0.28
```

---

## Q6 — Do you need many attributes? Try a few subsets
**In WEKA**
1. **Preprocess** → select attributes you want to drop → **Remove**.
   - Try subsets such as:  
     S1: {`checking_status`, `duration`, `credit_amount`, `age`, `credit_history`, `savings_status`}  
     S2: {`checking_status`, `duration`, `purpose`, `housing`, `employment`}
2. **Classify** → `J48` → **Cross-validation (10)** → **Start**.

**What to record**
- For each subset: list, CV accuracy, tree size (number of leaves/size).

---

## Q7 — Train again on your best subset & compare
**In WEKA**
1. Keep the best subset from Q6.
2. **Classify** → `J48` → `Cross-validation (10)` → **Start**.

**What to record**
- CV accuracy and tree; discuss whether it’s different from Q5 (all features).

---

## Q8 — Simple vs complex trees; link to bias
**In WEKA (control complexity via J48 options)**
- Click the **J48** name to open options:
  - `-C` (Confidence factor) **lower** → **larger** tree (less pruning). Default `0.25`.
  - `-M` (minNumObj) **smaller** → **larger** tree. Default `2`.
  - `-U` (unpruned) makes the largest tree.
- Run with:
  - **Simple:** `-C 0.4 -M 10` (more pruning)
  - **Complex:** `-C 0.05 -M 1` (less pruning)
- Use **10‑fold CV** for each.

**What to record**
- For simple vs complex: CV accuracy and tree size; relate: simpler tree → higher bias, lower variance; complex → lower bias, higher variance.

---

## Q9 — Reduced‑Error Pruning (REP)
**In WEKA**
1. **Classifier:** `J48`.
2. Click **J48** options → check `-R` (Use reduced error pruning) and set `-N` (e.g., `3` or `10` folds for pruning).
3. **Test options:** `Cross-validation (10)`.
4. **Start**.

**What to record**
- CV accuracy, tree size, and whether pruned model improves over Q8.

**Example output (illustrative)**
```
Scheme: weka.classifiers.trees.J48 -R -N 3
Correctly Classified Instances       742               74.2 %
```

---

## Q10 — Rules: hand‑convert a tiny tree; PART & OneR
**A) Convert a tiny tree to rules**
- Take a 2–3 level portion of your J48 tree. Write rules like:  
  *IF checking_status in {<0, 0<=X<200} AND duration > 24 THEN class = bad.*

**B) Train PART (rules from partial trees)**
1. **Classifier → Choose** → `rules` → `PART`.
2. Test with **Cross-validation (10)** → **Start**.
3. **Record:** rules printed, CV accuracy.

**C) Train OneR (1‑attribute rule)**
1. **Classifier → Choose** → `rules` → `OneR`.
2. (Optionally set `-B` min bucket size, e.g., `6`)
3. **Cross-validation (10)** → **Start**.
4. **Record:** the single rule, CV accuracy.

**D) Rank performances**
- Put CV accuracies side‑by‑side for **J48**, **PART**, **OneR**.

**Example PART snippet (illustrative)**
```
Rule 1: checking_status=<0 AND duration>24 => class=bad (123.0/45.0)
Rule 2: savings_status=>=1000 => class=good (80.0/20.0)
...
```

---

## Q11 — K‑means clustering (SimpleKMeans)
**In WEKA**
1. **Preprocess:** (Recommended) `Filter → unsupervised → attribute → NominalToBinary` then `Standardize`.
2. **Cluster** tab.
3. **Clusterer → Choose** → `SimpleKMeans`.
4. Click clusterer name to set:
   - `-N 2` clusters (you can try 3–5 as well).
   - `DistanceFunction: EuclideanDistance` (default).
5. **Classes to clusters evaluation:** check **Use training set** and **Classes to clusters evaluation**. Ensure **class** is set to `class` at bottom.
6. **Start**.

**What to record**
- Cluster centroids; size of clusters; **Classes to clusters** mapping and % correct (unsupervised agreement with labels).

**Example snippet (illustrative)**
```
Cluster 0: size 690
Cluster 1: size 310
Classes to Clusters:
 good -> Cluster 0 (78%)
 bad  -> Cluster 1 (52%)
```

---

## Q12 — SVM (SMO) and compare with Decision Tree
**In WEKA**
1. **Classify** tab → **Choose** `functions` → `SMO`.
2. Click **SMO** to set the kernel:
   - Start with `RBFKernel` (good baseline). Set `-G` (gamma), e.g., `0.01`.
   - Set complexity `-C`, e.g., `1.0`.
   - Tip: Use `meta → CVParameterSelection` with base `SMO` to auto‑tune `C` and `gamma`.
3. **Test options:** `Cross-validation (10)` → **Start**.

**What to record**
- CV accuracy, Kappa, confusion matrix.
- Compare to your best **J48** result (from Q5/Q8/Q9).

**Example output (illustrative)**
```
SMO (RBFKernel): Correctly Classified Instances  760  76.0 %
Confusion Matrix:
 a   b
640  60 | a = good
140 160 | b = bad
```

---

## Reporting Tips
- Always include: algorithm + key options, evaluation mode (training vs 10‑fold CV), accuracy/Kappa, confusion matrix, and model size (tree leaves or #rules).
- Save runs: right‑click result → **Save result buffer** or **Save model**.
- Visuals: right‑click J48 run → **Visualize tree** → **Save** as PNG.

---

## Blank Results Table (fill in)
| Experiment | Settings | Eval (Train/CV) | Accuracy % | Kappa | Size (leaves/rules) | Notes |
|---|---|---|---:|---:|---:|---|
| Q3 J48 (train set) | default | Train |  |  |  |  |
| Q5 J48 (10‑CV) | default | 10‑CV |  |  |  |  |
| Q6 J48 subset S1 | list S1 | 10‑CV |  |  |  |  |
| Q6 J48 subset S2 | list S2 | 10‑CV |  |  |  |  |
| Q7 J48 best subset | best S? | 10‑CV |  |  |  |  |
| Q8 J48 simple | `-C 0.4 -M 10` | 10‑CV |  |  |  |  |
| Q8 J48 complex | `-C 0.05 -M 1` | 10‑CV |  |  |  |  |
| Q9 J48 REP | `-R -N 3` | 10‑CV |  |  |  |  |
| Q10 PART | default | 10‑CV |  |  |  |  |
| Q10 OneR | default | 10‑CV |  |  |  |  |
| Q11 KMeans | `k=2` | classes↔clusters |  |  |  |  |
| Q12 SMO | RBF (tuned) | 10‑CV |  |  |  |  |

---

> **Note on numbers:** The example numbers above are *illustrative*. Your outputs may differ slightly depending on preprocessing choices, sampling, and WEKA version.
