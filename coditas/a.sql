-- Difference b/w Where and Group BY and Having
SELECT dept_name, COUNT(emp_id) AS emp_id_male_count 
FROM table t 
WHERE gender = 'male'
GROUP BY dept_name 
HAVING COUNT(emp_id) > 500;


-- Q2. How to get the 1st row of the table
SELECT *, ROW_NUMBER() OVER(PARTITITION BY PRIMARY) as rn FROM table;

id 
2-1 -2
1-2 -1
3-3 -3


10 - 1 - 1
20 - 2 - 2
20 - 2 - 2
30 - 4 - 3

-- Q3. What will be the output of Inner and Left Join
Table A - 
col1
1
1
0
0
null

Table B - 
col1
1
1
1
0
0
null
null
3

-- Result 
-- for INNER JOIN (NULL is not considered as a value for joining)
1 1
1 1
1 1
1 1
1 1
1 1
0 0
0 0 
0 0
0 0

-- for LEFT JOIN (NULL is not considered for joining as a value but in left Table null was present --> It is that null in the output table)
1 1
1 1
1 1
1 1
1 1
1 1
0 0
0 0 
0 0
0 0
null null 
3 null


-- Q. How does a map reduce job is different from a spark Job
-- Transformation  1 2,3,4,5,6 (Transaformations)  9 (Action) 

-- Q. What is the difference b/w Coalesce in Repartition and when should be use it

-- Q. What is Spark Architecture. How does the data gets processed

-- Q. How Executor is different from Driver
-- Q. How partitions are defined in a Spark Job --> Executor Cores
-- Q. About Reshuffing during Joins & default Partition Numbers
-- Q. How Traditional DB and current data warehourse are different?
-- Q. What are the reasons why DW are faster as compare to traditional DBs? 
        -- 1. Data storing format --> Columnar Storage
        -- 2. Does not have to be ACID complaint (are ACID compliant DW are also there with different mechanism)
        -- 3. Data gets processed in different nodes 
        -- 4. DW - Scalable DB - Does not work on multiple nodes
-- Q. AWS services
        -- 1. Where does the metadata gets stored --> Glue Catalogue
        -- 2. How Redshift is different from traditional DBs
        -- 3. What is RDS, Why we use the AWS Crawlers
        -- 4. What do you use to write queries on AWS --> Athena








