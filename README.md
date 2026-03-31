# B.Tech Grade Predictor Project

**Author:** Atharv Khale

## Project Overview

I created a Python tool to help students figure out their academic standing. It also predicts the marks they need in the End-Term exam to get their desired grade.

## The Logic (30-40-30 Rule)

This project uses the VIT Bhopal grading system:

1. **Mid-Term marks (30%):** These are, out of 50. Scaled down to 30.

2. **Assignment marks (40%):** These are directly taken out of 40.

3. **End-Term marks (30%):** I calculate these out of 100 to help users reach their target grade.

## Key Features (v2.0 Update)

* We have ** Scaling**. It helps convert a 50-mark Mid-term into a 30% weightage.

* Our system includes **Safety Buffer Analysis**. It works like a "Fail-Safe". It figures out the marks you need to avoid a backlog, which is 50%.

* With **Goal Setting** you can set a target, like an S or A grade. The system then calculates what you need to achieve at the end of the term.

* We also have **Validation Logic**. It checks if your goal is possible. If you need, than 100% it will tell you that it's not possible.

## Environment

* **Language:** I used Python 3.x for this project.

* **IDE:** I worked on it using VS Code.

* **Libraries:** I did not use any libraries; it's Python logic.
