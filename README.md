🚀 Overcoming Azure Free Tier Limits for Real-Time Data Streaming!
Building a real-time data stream processing pipeline on Azure Free Tier comes with challenges, but as a Data Engineer, adaptability is key! Here’s how I improvised and replaced missing services to make it work:
![Book Cover](main/project_overview.png)
🔹 Data Ingestion: Created an Azure Event Hub & Namespace for streaming data ingestion. However, the Free Tier doesn’t support the "Generate Data" feature, so I built an external Python script that used the Event Hub shared key and the random library to generate & send real-time weather data.

🔹 Databricks Setup: Due to no Unity Catalog in Free Tier, I couldn’t create temp schemas for data processing. Instead, I used Hive Metastore and created three databases (bronze, silver, gold) to store and process streaming data.

🔹 3-Layer Data Processing Architecture:
✔ Bronze Layer – Receives raw streaming data, previews it, and writes to bronze.weather.
✔ Silver Layer – Parses the event body into JSON, typecasts fields, and writes clean data to silver.weather.
✔ Gold Layer – Uses watermarking & windowing to compute 50-second rolling averages (temperature, humidity, precipitation).

🔹 Visualization Challenge & Workaround:

The Free Tier does not allow direct Power BI integration with Databricks.
Solution: Wrote Silver Layer data to Azure SQL Server, then connected Power BI via DirectQuery.
Issue: Power BI refreshes data every 5 minutes, but new messages arrived every 10 seconds. Manual refresh was needed to see real-time updates.
💡 Takeaway: Constraints fuel innovation! Even with Azure Free Tier limitations, I was able to build, test, and optimize a real-time streaming pipeline using Azure Event Hubs, Databricks, and Power BI.

Would love to connect with professionals working on real-time data processing & cloud engineering! 🚀

#Azure #Databricks #DataEngineering #Streaming #PowerBI #RealTimeData
