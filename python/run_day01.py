import duckdb

con = duckdb.connect()

queries = [
    (
        "Create table from CSV",
        """
        CREATE OR REPLACE TABLE leads AS
        SELECT *
        FROM read_csv_auto('data/leads.csv');
        """
    ),
    (
        "Total leads",
        """
        SELECT COUNT(*) AS total_leads
        FROM leads;
        """
    ),
    (
        "Leads by stage",
        """
        SELECT stage, COUNT(*) AS total
        FROM leads
        GROUP BY stage
        ORDER BY total DESC;
        """
    ),
    (
        "Leads by source",
        """
        SELECT source, COUNT(*) AS total
        FROM leads
        GROUP BY source
        ORDER BY total DESC;
        """
    ),
    (
        "Pipeline value",
        """
        SELECT SUM(deal_value) AS total_pipeline_value
        FROM leads;
        """
    ),
    (
        "Average deal size",
        """
        SELECT AVG(deal_value) AS avg_deal_size
        FROM leads;
        """
    ),
]

for title, query in queries:
    print(f"\n=== {title} ===")
    result = con.execute(query)
    if result.description:
        columns = [col[0] for col in result.description]
        rows = result.fetchall()
        print(" | ".join(columns))
        for row in rows:
            print(" | ".join(str(x) for x in row))