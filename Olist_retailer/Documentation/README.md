Olist E-Commerce Analysis: The Psychology of Satisfaction
A Digital Humanities Approach to Customer Sentiment Optimization

Project Overview
This project analyzes 100k+ orders from Olist, a Brazilian e-commerce marketplace, to answer a critical business question: "How can we increase customer satisfaction?"

Instead of focusing solely on operational metrics (like delivery speed), it investigates the human experience behind the timestamps—specifically, how the gap between "Estimated Date" and "Physical Reality" (Actual Delivery) drives sentiment.

The Business Challenge
Olist connects small businesses to major marketplaces. While Olist handles the digital platform, logistics are decentralized. The CEO needed to understand why some customers leave 1-star reviews even when deliveries arrive "on time" according to the system.

Key Objectives:
Identify the root causes of negative reviews.
Determine the "Patience Threshold" for Brazilian consumers.
Detect underperforming sellers and "High Risk" product categories.

Tech Stack & Methodology
Language: Python (Pandas, NumPy, Matplotlib, Seaborn)
Workflow: Google Data Analytics (Ask, Prepare, Process, Analyze, Share, Act)

Key Techniques:
Sentiment Segmentation: Categorizing 1-5 star ratings into "Satisfied," "Neutral," and "Dissatisfied."
Time-Delta Engineering: Calculated delivery_delay (Expectation Gap) vs delivery_time (Absolute Speed).
Behavioral Correlation: Analyzed how product metadata (photos, description length) impacts trust.

Key Insights (The "Aha!" Moments)
1. The "Algorithmic Gaslighting" Paradox
Data revealed that unhappy customers often received their packages 5 days early (relative to the estimate).
Insight: Olist's algorithms are overly conservative. Beating a "safe" estimate does not make a customer happy if the absolute wait time is too long.
The Metric: Customer satisfaction correlates with Absolute Time, not Relative Time.

2. The "2-Week Wall"
There is a distinct psychological tipping point at 14 days.
Orders delivered in < 14 days have stable positive sentiment.
Orders delivered in > 15 days see a skyrocketing dissatisfaction rate, regardless of the promise.

3. The "IKEA Effect" in Categories
The lowest-rated category was Office Furniture (Score: 3.5), despite arriving ~12 days early.
Insight: The dissatisfaction stems from the Physical vs. Digital disconnect. Heavy, complex items often arrive with scratches or missing instructions, leading to a gap between the "pristine" digital image and the "complex" physical reality.

Strategic Recommendations
Based on this analysis, I recommended three concrete actions to the CEO:
Update the App Interface: Implement a "2-Week Warning" or discount offer for products with predicted shipping > 14 days.
The Seller Purge: Automatically offboard the identified "Villain Sellers" (Top 10 list provided) who maintain >40% negative review rates.
Content Audit: For "High Risk" categories (Furniture, Fashion), mandate Size Charts and Assembly Videos to reduce Information Asymmetry.