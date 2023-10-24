# teiko-technical
Data:
File cell-count.csv contains cell count information for various immune cell populations of each patient sample. There are five populations: b_cell, cd8_t_cell, cd4_t_cell, nk_cell, and monocyte. Each row in the file corresponds to a biological sample.

Python:
1. Please write a python program to convert cell count in cell-count.csv to relative frequency (in percentage) of total cell count for each sample. Total cell count of each sample is the sum of cells in the five populations of that sample. Please return an output file in csv format with cell count and relative frequency of each population of each sample per line. The output file should have the following columns:

sample: the sample id as in column sample in cell-count.csv
total_count: total cell count of sample
population: name of the immune cell population (e.g. b_cell, cd8_t_cell, etc.)
count: cell count
percentage: relative frequency in percentage

```
pip install panda
python freq_converter.py
```

2. Among patients who have treatment tr1, we are interested in comparing the differences in cell population relative frequencies of melanoma patients who respond (responders) to tr1 versus those who do not (non-responders), with the overarching aim of predicting response to treatment tr1. Response information can be found in column response, with value y for responding and value n for non-responding. Please only include PBMC (blood) samples. 

a. For each immune cell population, please generate a boxplot of the population relative frequencies comparing responders versus non-responders.

```
pip install matplotlib
pip install seaborn
pip install scipy
```

b. Which cell populations show a difference between responders and non-responders? Please include statistics to support your conclusion.

Please return both the code and the outputs. Please also specify any dependencies that you use and instructions on how to run your code to reproduce the outputs.

Database:
1. How would you design a database to capture the type of information and data in cell-count.csv? Imagine that you’d have hundreds of projects, thousands of samples and various types of analytics you’d want to perform, including the example analysis of responders versus non-responders comparisons above. Please provide a rough prototype schema.
- Projects (id, project)
- Subjects (id, subject)
- Samples (id, project_id, subject_id, sample, sample_type)
- Patients (id, sample_id, condition, age, sex)
- Treatments (id, patient_id, treatment, time_from_treatment_start)
- Responses (id, patient_id, response)
- ImmuneCellCounts (id, patient_id, b_cell_count, cd8_t_cell_count, cd4_t_cell_count, nk_cell_count, monocyte_count)
p.s.: id in every schema is the primary key, {}+_id format is foreign key corresponding to some primary key.

2. What would be some advantages in capturing these information in a database?
- Each table represents a specific entity related to cell counts. So to reduce data redundancy. For example, if a patient has different response to same treatment (due to different time_from_treatment_start), in csv, multiple rows of same patient information needs to be recorded, such as sex, etc; where in the above table schedule, only Responses or ImmuneCellCounts would require additional rows. 
- Data could be efficiently retrieved and analyzed using SQL without worrying about unnecesary columns. If even more complicated, things such as index could be used to improve efficiency, as well as a lot of other SQL keywords. 
- Easier to understand and visualize data because the relationship are established through primary key and foreign key. 

3. Based on the schema you provide in (1), please write a query to summarize the number of subjects available for each condition.
```
SELECT p.condition, COUNT(DISTINCT s.subject_id) AS subject_count
FROM Patients p
INNER JOIN Samples s ON p.sample_id = s.id
GROUP BY p.condition
ORDER BY p.condition;
```
4. Please write a query that returns all melanoma PBMC samples at baseline (time_from_treatment_start is 0) from patients who have treatment tr1.
```
SELECT s.sample, p.condition, p.age, p.sex
FROM Samples s
INNER JOIN Patients p ON s.id = p.sample_id
INNER JOIN Treatments t ON p.id = t.patient_id
WHERE s.sample_type = 'PBMC'
    AND p.condition = 'melanoma'
    AND t.treatment = 'tr1'
    AND t.time_from_treatment_start = 0;
```
5. Please write queries to provide these following further breakdowns for the samples in (4): 

a. How many samples from each project 
```
SELECT s.project, COUNT(*) AS sample_count
FROM Samples s
WHERE s.sample IN (4)
GROUP BY s.project;
```
b. How many responders/non-responders
```
SELECT r.response, COUNT(*) AS count
FROM Responses r
WHERE r.patient_id IN (4)
GROUP BY r.response;
```
c. How many males, females
```
SELECT p.sex, COUNT(*) AS count
FROM Patients r
WHERE r.patient_id IN (4)
GROUP BY p.sex;
```
