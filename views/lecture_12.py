import streamlit as st

from config import ASSETS_DIR


def render_lecture_12():
    st.title("Lecture 12 Summary")
    st.write("---")
    st.subheader("Intro to SQL")
    st.write(
        """
    A database is any organized collection of data. A relational database specifically 
    stores data in tables where relationships between entities are expressed through 
    shared keys. The underlying theory comes from relational algebra — the idea that you
    can query any data by specifying what you want, not how to retrieve it.
    A DBMS handles storage, access control, transactions, and query execution. Data is stored
    in tabular form and has identifiers such as Primary Keys and Foreign Keys which make the connection between
    tables in the database more structured and lowers redundancy.
    """
    )
    st.write("---")
    st.subheader("DB Relationships")
    st.write("""Relationships are enforced at the schema level using foreign key 
            and primary key to allow the link between two tables. There are three types of relationships:
            One-to-One is actually the rarest in practice. It is mostly refered to enforce that a piece of data belongs to exactly one entity — like a passport to a person.
            One-to-Many is the most common relation. An order has many line items. A user has many posts. A department has many employees.
            Many-to-Many relationship between two entities is a relationship where each instance of the parent entity corresponds to zero or more instances of the child entity.                       
             """)
    st.write("---")
    st.subheader("Database Normalization")
    st.write("""
             The goal of normalization is to make every piece of data exist in exactly one place. When data exists in multiple places, updates create inconsistency. Normalization forces you to decompose large tables into smaller, more focused ones.
             1NF (First Normal Form) — three rules: each cell holds a single atomic value (no lists or arrays in a cell), no repeating column groups 
             2NF (Second Normal Form) — builds on 1NF and adds: every non-key column must depend on the entire primary key, not just part of it. This only applies when you have a composite primary key. If your primary key is (order_id, product_id), a column like product_name depends only on product_id — that's a partial dependency, which violates 2NF. The fix is to move product_name to a separate products table.
             3NF (Third Normal Form) — builds on 2NF and adds: no non-key column can depend on another non-key column. This is called a transitive dependency. Example: if you have employee_id → department_id → department_name, then department_name depends on department_id, not directly on employee_id. The fix is to extract department_id and department_name into their own table.
             """)
    st.write("---")
    st.subheader("OLAP vs OLTP")
    st.write("""OLAP (Online Analytical Processing) and OLTP (Online Transaction Processing) are both integral parts of data management, but they have different functionalities.
             OLTP — Online Transaction Processing
            Handles many small, fast transactions in real time. Optimized for writes. Supports ACID properties. Examples: banking transactions, e-commerce orders, booking systems.
            Goal: speed & reliability for day-to-day operations.
            """)
    st.write("""OLAP — Online Analytical Processing
                Handles complex queries across large historical datasets. Optimized for reads. Part of data warehousing. Examples: Netflix recommendations, Spotify personalization, financial forecasting.
                Goal: insight & analysis for decision-making.
            """)
    st.write("---")
    st.subheader("Data Lakes & Data Warehouses")
    st.write("""Stores raw, unprocessed data in any format (structured, semi-structured, unstructured). Schema is applied on read. Cheap storage. Used by data scientists for exploration and ML.
            Like a giant raw storage dump. Flexible but messy if ungoverned.
            """)
    st.write("""Data Warehouse
             Stores processed, structured data organized for querying and reporting. Schema applied on write. Optimized for OLAP workloads. Used by analysts and BI tools.
             A clean, organized library. Structured but less flexible.
            """)
    st.write("---")
    st.subheader("Star & Snowflake Schema")
    st.image(ASSETS_DIR / "dbschemas.jpg")
    st.write("""Star Schema
             Fact table connects directly to dimension tables. Dimension tables are denormalized — flat and redundant. Fewer joins = faster queries. Simpler to understand.
             Snowflake Schema
             Dimension tables are further normalized into sub-dimension tables (like a snowflake shape). Less redundancy, less storage, but more complex joins.
            """)
