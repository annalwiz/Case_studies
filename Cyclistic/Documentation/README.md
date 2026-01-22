 A Tale of Two Riders: Cyclistic Bike-Share Analysis
 Uncovering Urban Mobility Patterns through Data Science & Digital Humanities

Author: Anna Louise  
Role: Data Analyst & Junior Data Scientist  
Focus: Public Policy, Digital Humanities, and Creative Data Storytelling  
Tech Stack: Python (Pandas, Scikit-Learn, Matplotlib/Seaborn), Inferential Statistics

---

Project Overview
This case study analyzes historical bike-share data from Cyclistic, a fictional company in Chicago. The goal is not merely to increase sales, but to understand the behavioral divergence between two distinct user groups: "Casual" riders (leisure/tourists) and "Annual Members" (commuters/locals). 

As a Data Scientist with a background in History and Public Policy, I approached this dataset as an archive of city life. I used Python to clean and probe the data, applying inferential statistics to prove that these two groups inhabit the city in fundamentally different ways�allowing us to design a strategy that respects their distinct motivations while encouraging membership conversion.

The Business Task
The Problem: The Director of Marketing believes the company�s future growth depends on maximizing the number of annual memberships. Casual riders are already aware of the program but haven't committed to a subscription.

The Question: How do annual members and casual riders use Cyclistic bikes differently? 

---

Tech Stack & Methodology
I chose Python (Pandas) for this project to demonstrate end-to-end data handling without relying on spreadsheet limitations.

Data Cleaning & Manipulation: `Pandas` (merging 12 months of data, datetime conversion, null handling).
Statistical Analysis: `Scipy` / `Scikit-Learn` (T-tests to validate ride duration differences).
 Visualization: `Matplotlib` & `Seaborn` (for statistical plots).
 Creative Output: Custom infographics and data-comics to humanize the insights.

---

Data Source & Preparation
Source: Previous 12 months of Cyclistic trip data (public data provided by Motivate International Inc.).

Process:
1.  Ingestion: Used Python to iterate through 12 separate CSV files and merge them into a single dataframe containing millions of rows.
2.  Feature Engineering:
     Calculated `ride_length` by subtracting `started_at` from `ended_at`.
     Extracted `day_of_week` and `month` to analyze temporal patterns.
3.  Sanity Check & Cleaning:
     Removed "administrative" rides (negative durations or rides < 60 seconds).
     Filtered out data with missing station coordinates to ensure geospatial accuracy.

---

Key Insights & Analysis
Note: This section summarizes the behavioral patterns discovered.

1. The "Pulse" of the City (Temporal Analysis)
 Members: Their usage peaks at 8:00 AM and 5:00 PM on weekdays. They are "Commuters" using the system for efficient, predictable transport.
 Casuals: Usage ramps up slowly throughout the day, peaking on weekends and sunny afternoons. They are "Explorers" using the system for leisure and discovery.

2. Duration vs. Distance
 Statistical Significance: A T-test confirmed that Casual riders take significantly longer rides than Members, despite often covering less "efficient" distances. This suggests they value the experience of the ride over the destination.

3. Station Geography
 Members: Highly concentrated around transit hubs and commercial districts.
 Casuals: Clustered around parks, museums, and the waterfront (the "leisure corridor").

---

Creative Deliverables
To bridge the gap between raw data and stakeholder understanding, I created:

1.  "The Tale of Two Riders" (Infographic): A visual persona guide contrasting the "Commuter" and the "Explorer," using cartoons to illustrate their different pain points and motivations.
2.  The City Flow Map: A visualization showing how the city "breathes" differently on weekdays (Member dominance) vs. weekends (Casual dominance).

---

Recommendations
Based on the data, I propose a strategy that meets Casual riders where they are:

1.  The "Weekend Warrior" Pass: Create a specific membership tier for Fri-Sun usage. Data shows Casuals are heavily active during this window but may feel a full annual pass is "wasted" on workdays.
2.  Gamified "History Hunter" Routes: Leverage the Casuals' desire for exploration. Create curated digital routes (via app) that guide riders to historical landmarks, incentivizing longer rides and deeper engagement with the brand.
3.  Strategic Digital Ads: Shift ad spend to Friday afternoons and Saturday mornings, specifically targeting geofenced areas around museums and parks where Casuals congregate.

