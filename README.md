# streaming_demo

🚀 Overcoming Azure Free Tier Limits for Real-Time Data Streaming!
Building a real-time data streaming pipeline on Azure Free Tier came with challenges, but I improvised to make it work! Here’s how:

🔹 Data Ingestion:
✔ Created Azure Event Hub & Namespace for streaming data.
✔ Free Tier doesn’t support "Generate Data", so I:

Built an external Python script to generate random weather data.
Sent data to Event Hub using Shared Key authentication.
🔹 Databricks Setup:
✔ No Unity Catalog in Free Tier → Couldn’t create temp schemas.
✔ Workaround: Used Hive Metastore and created:

Bronze Layer → Stores raw streaming data (bronze.weather).
Silver Layer → Cleans & transforms data (silver.weather).
Gold Layer → Computes 50-second rolling averages (gold.weather).
🔹 Processing & Visualization Challenges:
✔ Power BI does not support Databricks Free Tier → No direct integration.
✔ Solution: Wrote Silver Layer data to Azure SQL Server, then connected Power BI via DirectQuery.
✔ Issue: Power BI refreshes every 5 minutes, but data arrived every 10 seconds → Manual refresh needed to see updates.

💡 Key Takeaway:
Even with Azure Free Tier limitations, I built a fully functional real-time streaming pipeline using Azure Event Hubs, Databricks, and Power BI.

Would love to connect with professionals working on real-time data processing & cloud engineering! 🚀

#Azure #Databricks #DataEngineering #Streaming #PowerBI #RealTimeData
