# Hello DBMS

## Technology Watch

A. Data is a collection of facts or figures that can be used to provide information or insights. It can be collected from a variety of sources, including surveys, experiments, and observations. Data can be presented in a variety of formats, including text, numbers, images, and audio.

Here are some examples of data:

* The population of a city
* The average price of a gallon of gasoline
* The weather forecast for tomorrow
* The results of a scientific experiment
* The lyrics of a song
* A photograph of a person

Data can be used for a variety of purposes, including:

* Making decisions: Data can be used to help people make informed decisions. For example, a company might use data to determine where to open a new store.
* Solving problems: Data can be used to solve problems. For example, a scientist might use data to develop a new drug.
* Understanding the world: Data can be used to understand the world around us. For example, a historian might use data to study the history of a particular event.

Data can be classified into two main types:

* Quantitative data: Quantitative data is data that can be measured or counted. For example, the population of a city is quantitative data.
* Qualitative data: Qualitative data is data that cannot be measured or counted. For example, the lyrics of a song are qualitative data.

Data can also be classified by its source. For example, data collected from a survey is called survey data. Data collected from an experiment is called experimental data.

Data is a valuable resource that can be used for a variety of purposes. It is important to understand the different types of data and how they can be used.

B. Data quality criteria are characteristics that can be used to assess the quality of a dataset. They are used to ensure that the data is reliable and relevant to the user's needs.

Data quality criteria can be classified into two categories:

* Intrinsic criteria are characteristics of the data itself. They measure the accuracy, completeness, consistency, validity, timeliness, integrity, and clarity of the data.
* Extrinsic criteria are characteristics of the data in relation to its use. They measure the relevance, usefulness, reliability, and security of the data.

Intrinsic criteria

* Accuracy: Measures the conformity of the data to the real facts.
* Completeness: Measures the presence of all necessary information.
* Consistency: Measures the agreement between different data.
* Validity: Measures the relevance of the data to its purpose.
* Timeliness: Measures the freshness of the data.
* Integrity: Measures the absence of unauthorized modification of the data.
* Clarity: Measures the ease of understanding the data.

Extrinsic criteria

* Relevance: Measures the suitability of the data to the user's needs.
* Usefulness: Measures the ability of the data to meet the user's needs.
* Reliability: Measures the probability that the data is correct.
* Security: Measures the protection of the data against unauthorized access, modification, or destruction.

Measuring data quality is an important process that ensures the reliability and relevance of the data. It also helps to detect errors and anomalies in the data, so that they can be corrected or deleted.

There are many tools and techniques that can be used to measure data quality. These tools can be used manually or automatically.

Data quality measurement should be done regularly to ensure that the data is always of high quality.

C. Data Lake, Data Warehouse, and Lake House are three distinct concepts used to store and manage data for analytics and business intelligence purposes. Here's a brief definition and comparison of each:

Data Lake: A Data Lake is a centralized repository that stores raw, unprocessed data in its native format. It's designed to hold large amounts of data, including structured, semi-structured, and unstructured data, making it ideal for big data and IoT applications. Data Lakes are schema-on-read, meaning the schema is applied when the data is queried or analyzed.

![Data Lake](https://www.qlik.com/us/-/media/images/global-us/site-content/data-lakes/datalakediagram022x.png?rev=d3dc9ec541e944fe96a216ea801389a7&h=588&w=1276&hash=182DB8FBFE8EB782971633C03DAA5BBE "Data Lake")

Data Warehouse: A Data Warehouse is a structured repository that stores data in a predefined schema. It's designed for querying and reporting, and it's optimized for fast query performance. Data Warehouses are typically used for business intelligence, analytics, and reporting, and they're often fed by data from various sources, such as transactional databases, log files, and APIs.

![Data Warehouse](https://www.snaplogic.com/wp-content/uploads/2023/04/Classic-data-warehouse-diagram-1-1024x673.png "Data Warehouse")

Lake House: A Lake House combines the benefits of Data Lakes and Data Warehouses, offering a hybrid approach to data management. It's designed to provide the scalability and flexibility of a Data Lake with the structure and management capabilities of a Data Warehouse. Lake Houses enable data scientists and analysts to work with raw data in a flexible schema-on-read environment while still providing the governance and security of a Data Warehouse.

Here's a diagram illustrating the differences between Data Lakes, Data Warehouses, and Lake Houses:

![Data Lake vs Data Warehouse vs Lake House](https://www.qlik.com/us/-/media/images/global-us/site-content/data-lakes/data-lakehouse/data-lakehouse-diagram.png?rev=78cd0b1132d94245beb0239bb0982e8f&h=674&w=1276&hash=F22AA1EBC7AF29D32F6AF742670A261E "Data Lake vs Data Warehouse vs Lake House")

D. A database management system (DBMS) is a software suite that allows organizations to create, read, update, and delete records within a database. The records represent information that needs to be stored, such as product prices, customer names, and inventory levels.

The three primary types of DBMS are:

Relational DBMS: These DBMSs use tables to represent and store data. The tables consist of rows (records) and columns (attributes). They support operations such as retrieving records that meet certain conditions (queries), inserting new records, updating existing records, and deleting records. Microsoft SQL Server, MySQL, and Oracle Database are examples of relational DBMSs.

![Relational DBMS](https://www.redswitches.com/wp-content/uploads/2023/08/Fig-3_-Relational-database-management-system.jpg "Relational DBMS")

NoSQL DBMS: NoSQL DBMSs were developed to address the limitations of traditional relational DBMSs, especially when dealing with large volumes of unstructured or semi-structured data. Instead of using tables, NoSQL DBMSs use alternative data structures like key-value pairs, documents, or wide-column stores. Some examples of NoSQL DBMSs are MongoDB, Cassandra, and Amazon DynamoDB.

![NoSQL DBMS](https://media.geeksforgeeks.org/wp-content/uploads/20220131094632/TypesofNoSQLgraph.jpg "NoSQL DBMS")

Object-Oriented DBMS: In object-oriented DBMSs, data is organized into objects. These DBMSs allow applications to work with objects directly, which can simplify the development process. However, they have not gained as much popularity as the previous two types. ObjectDB is an example of an object-oriented DBMS.

![Object-Oriented DBMS](https://upload.wikimedia.org/wikipedia/commons/7/7c/Object-Oriented_Model.svg "Object-Oriented DBMS")

In addition to managing data, DBMSs also provide tools to maintain and secure the database. This includes tasks such as backup and recovery, performance tuning, and implementing access control and data security measures.

E. Relational Databases:

A relational database is a database that uses the relational model to organize data. The relational model is a data model that organizes data into tables, consisting of rows and columns. Rows represent individual records, and columns represent the attributes of these records.

Relational databases are the most common types of databases and are used in a wide variety of applications, including Content Management Systems (CMS), Customer Relationship Management (CRM) systems, and Database Management Systems (DBMS).

Examples of applications of relational databases:

* Content Management Systems (CMS): CMSs use relational databases to store website content, including pages, articles, and images.
* Customer Relationship Management (CRM) systems: CRMs use relational databases to store information about customers, including their contact details, purchases, and interactions with the company.
* Database Management Systems (DBMS): DBMSs are software that allows the creation, management, and use of relational databases.

Non-relational Databases:

A non-relational database is a database that does not follow the relational model. Non-relational databases are generally more flexible than relational databases, but they may be less performant for certain operations.

There are many different types of non-relational databases, each with its own advantages and disadvantages. Some common types of non-relational databases include:

* Key-Value Databases: Key-value databases store data in the form of a key-value pair. The key is used to identify the record, and the value is the data itself.
* Document-oriented Databases: Document-oriented databases store data in the form of documents. Documents can contain data of different types, including text, images, and videos.
* Graph Databases: Graph databases store data in the form of a graph, which is a data structure composed of nodes and edges. Nodes represent entities, and edges represent the relationships between these entities.

Examples of applications of non-relational databases:

* Data storage applications: Non-relational databases are often used to store large amounts of data, including unstructured or semi-structured data.
* Search applications: Non-relational databases are often used for data search, especially for unstructured or semi-structured data.
* Streaming applications: Non-relational databases are often used for streaming data, particularly for unstructured or semi-structured data.

Difference between Relational and Non-relational Databases:

The main difference between relational and non-relational databases is how they store data. Relational databases store data in tables, while non-relational databases store data in different ways, depending on the type of database.

Relational databases are generally better for search and join operations, while non-relational databases are generally more flexible and can be better for storing and retrieving unstructured or semi-structured data.

| Characteristic            | Relational Database           | Non-relational Database            |
|--------------------------|-------------------------------|------------------------------------|
| Data Model               | Relational                    | Non-relational                     |
| Data Organization        | Tables                        | Various ways, depending on the type of database |
| Performance              | Better for search and join operations | Better for storage and retrieval of unstructured or semi-structured data |
| Flexibility              | Less flexible                 | More flexible                      |

F. In a relational database:

* Primary Key: A primary key is a unique identifier for each record in a table. It must contain unique values, and no two records in the table can have the same primary key. The primary key is used to uniquely identify each record and is often associated with the index to enhance search performance.

* Foreign Key: A foreign key is a field in a relational table that is used to establish a link between the data in two tables. It creates a relationship between the tables by referencing the primary key of another table. The foreign key in one table typically refers to the primary key in another table, creating a connection between the two tables. This relationship is crucial for maintaining data integrity and ensuring that references between tables remain valid.


G. In the context of database transactions, the ACID properties are a set of characteristics that ensure the reliability and consistency of transactions. ACID stands for:

* Atomicity: This property ensures that a transaction is treated as a single, indivisible unit of work. Either all the changes made by the transaction are committed to the database, or none of them are. If any part of the transaction fails, the entire transaction is rolled back.

* Consistency: Consistency ensures that a transaction brings the database from one valid state to another. The database must satisfy a set of integrity constraints before and after the transaction. If a transaction violates any integrity constraints, the entire transaction is rolled back.

* Isolation: Isolation ensures that the execution of one transaction is isolated from the execution of other transactions. Even though multiple transactions may be executing concurrently, the result should be as if the transactions were executed in some sequential order. Isolation prevents interference between transactions.

* Durability: Durability guarantees that once a transaction is committed, its effects will persist even in the case of a system failure. The changes made by a committed transaction are permanent and survive any subsequent failures.

These ACID properties collectively ensure the reliability, integrity, and consistency of database transactions in various scenarios, making them a fundamental concept in database management systems.

H.     1. Merise Method:

* Definition: Merise is a methodology used in information systems engineering for the analysis and design of information systems. It provides a structured and organized approach to modeling data, processes, and the relationships between them. Merise consists of several models, including the Conceptual Data Model (MCD), Data Flow Diagrams (DFD), and others.

* Usefulness: Merise is useful for designing and developing information systems in a methodical and systematic way. It helps in understanding the data requirements, defining processes, and ensuring that the resulting system aligns with the business needs.

* Specific Use Case: Consider a library management system. The Merise methodology can be applied to create a Conceptual Data Model (MCD) that represents entities like "Book," "Author," and "Library Member" and their relationships. Data Flow Diagrams (DFD) can then illustrate the flow of information between processes such as "Borrow Book" and "Return Book."

![Merise](https://ineumann.developpez.com/tutoriels/merise/initiation-merise/images/id_relative.png "Merise")

2. UML (Unified Modeling Language):

* Definition: UML is a standardized modeling language used in software engineering for visualizing, specifying, constructing, and documenting software systems. It provides a set of graphical notations for representing object-oriented analysis and design concepts.

* Usefulness: UML is widely used for modeling software systems and is valuable throughout the software development life cycle. It helps in communication between stakeholders, understanding system requirements, and designing software architecture.

* Specific Use Case: Consider the development of an online shopping system. UML can be applied to create a Use Case Diagram to identify and define various user interactions, a Class Diagram to represent classes like "Product" and "ShoppingCart," and a Sequence Diagram to illustrate the flow of interactions between objects during a purchase.

![Unified Modeling Language](https://landing.moqups.com/img/covers/diagrams/uml-diagrams/UML.png "Unified Modeling Language")


In summary, both the Merise method and UML play crucial roles in information technology. Merise is often employed for data-oriented system design, while UML is a versatile modeling language widely used in software engineering for visualizing and designing complex systems. The specific use cases mentioned demonstrate how these methodologies can be applied in practical scenarios with the help of visual representations.

I. SQL (Structured Query Language) Definition:

SQL is a standardized programming language used to manage and manipulate relational databases. It enables various operations such as creating, modifying, and deleting data, as well as managing access permissions to the database.

SELECT: Retrieves data from a table.

    SELECT column1, column2 FROM table_name WHERE condition; 

INSERT: Inserts new rows into a table.

    INSERT INTO table_name (column1, column2) VALUES (value1, value2);   

UPDATE: Modifies existing data in a table.

    UPDATE table_name SET column1 = value1 WHERE condition;  

DELETE: Deletes rows from a table.

    DELETE FROM table_name WHERE condition;  

CREATE: Creates a new table, view, or index.

    CREATE TABLE table_name (column1 datatype, column2 datatype);    

ALTER: Modifies the structure of an existing table.

    ALTER TABLE table_name ADD column_name datatype; 

DROP: Deletes a table or a database.

    DROP TABLE table_name;   

GRANT: Grants access permissions to a user or role.

    GRANT SELECT, INSERT ON table_name TO user_name; 

 Joins are used to combine data from two or more tables based on a specified relationship condition.

INNER JOIN: Returns rows when matches are found in both tables.

    SELECT * FROM table1 INNER JOIN table2 ON table1.column = table2.column;    

LEFT JOIN (or LEFT OUTER JOIN): Returns all rows from the left table and the matching rows from the right table.

    SELECT * FROM table1 LEFT JOIN table2 ON table1.column = table2.column; 

RIGHT JOIN (or RIGHT OUTER JOIN): Returns all rows from the right table and the matching rows from the left table.

    SELECT * FROM table1 RIGHT JOIN table2 ON table1.column = table2.column;    

FULL JOIN (or FULL OUTER JOIN): Returns all rows when there is a match in either of the tables.

    SELECT * FROM table1 FULL JOIN table2 ON table1.column = table2.column; 

CROSS JOIN: Returns the Cartesian product of the two tables (all possible combinations).

    SELECT * FROM table1 CROSS JOIN table2; 

## Project Context

## Conclusion

