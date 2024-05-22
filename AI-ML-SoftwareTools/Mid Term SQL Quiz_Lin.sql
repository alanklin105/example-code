-----Using  bigquery-public-data.nhtsa_traffic_fatalities dataset and accident tables
select * from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2015` limit 10;
select * from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2016` limit 10;
select * from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2017` limit 10;
select * from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2018` limit 10;
select * from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2019` limit 10;
select * from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2020` limit 10;

--Q1-- Write the SQL to create a view name -->accident<-- under -->Test<-- dataset in your project that combines all records from above 6 public tables
CREATE OR REPLACE VIEW ds-jungle-416001.Test.accident AS
SELECT year_of_crash as year, state_name as state, number_of_fatalities as fatalities, number_of_drunk_drivers as drunk_drivers, atmospheric_conditions_1_name as atmospheric_conditions from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2015`
UNION ALL SELECT year_of_crash, state_name, number_of_fatalities, number_of_drunk_drivers, atmospheric_conditions_1_name from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2016`
UNION ALL SELECT year_of_crash, state_name, number_of_fatalities, number_of_drunk_drivers, atmospheric_conditions_1_name from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2017`
UNION ALL select year_of_crash, state_name, number_of_fatalities, number_of_drunk_drivers, atmospheric_conditions_1_name from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2018`
UNION ALL select year_of_crash, state_name, number_of_fatalities, number_of_drunk_drivers, atmospheric_conditions_1_name from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2019`
UNION ALL select year_of_crash, state_name, number_of_fatalities, number_of_drunk_drivers, atmospheric_conditions_1_name from `bigquery-public-data.nhtsa_traffic_fatalities. accident_2020`
;



--Q2-- Write a SQL to summarize from the view created above - the number of accidents, total drunk drivers involved and total number of fatalities by year 
SELECT year, count(state) as total_accidents, SUM(drunk_drivers) as total_drunk_drivers, SUM(fatalities) as total_fatalities, 
FROM `ds-jungle-416001.Test.accident`
GROUP BY year
ORDER BY year ASC
;

--Q3-- Using the same view, write a SQL to identify and list only top 5 state_names with highest number of accidents over 6 year period that involves drunk driving
SELECT state, count(CASE WHEN drunk_drivers > 0 THEN 1 END) as num_accidents
FROM `ds-jungle-416001.Test.accident`
GROUP BY state
#HAVING num_accidents > 0
ORDER BY num_accidents DESC
LIMIT 5
;

--Q4-- Using the same view, identify the number accidents that occurred when atmospheric_conditions_1_name was either Snow, Blowing Snow, Sleet or Hail
SELECT a.snow, a.blowing_snow, a.sleet_hail, a.snow + a.blowing_snow + a.sleet_hail AS total FROM 
(SELECT COUNT(CASE WHEN atmospheric_conditions = 'Snow' THEN 1 END) as snow, COUNT(CASE WHEN atmospheric_conditions = 'Blowing Snow' THEN 1 END) as blowing_snow, COUNT(CASE WHEN atmospheric_conditions = 'Sleet or Hail' THEN 1 END) as sleet_hail
FROM `ds-jungle-416001.Test.accident`) as a
;

## OR THIS QUERY TO JUST SEE THE TOTAL

SELECT COUNT(atmospheric_conditions) as winter_conditions
FROM `ds-jungle-416001.Test.accident`
WHERE atmospheric_conditions IN ('Snow','Blowing Snow', 'Sleet or Hail');

--Q5-- Using the same view, identify the accidents when the number of drunk drivers is more than 2
SELECT *
FROM `ds-jungle-416001.Test.accident`
WHERE drunk_drivers > 2
;


-----Using  bigquery-public-data.chicago_taxi_trips.taxi_trips data
select * from `bigquery-public-data.chicago_taxi_trips.taxi_trips`limit 20;

--Q6-- Identify the month having the largest amount for trip_total
select EXTRACT(MONTH from trip_end_timestamp) as Month, trip_total
from `bigquery-public-data.chicago_taxi_trips.taxi_trips`
ORDER BY trip_total DESC
LIMIT 1
;

--Q7-- Identify the company that has recieved maximum tips as percentage of the trip_toal cost

SELECT a.company, max(a.tip_percentage) as max_tip_percentage
FROM (SELECT company, tips/ NULLIF(trip_total,0) as tip_percentage
from `bigquery-public-data.chicago_taxi_trips.taxi_trips`) a
GROUP BY company
ORDER BY max_tip_percentage DESC
LIMIT 10
;

--Q8-- Using below query, select all columns from SUMMARY and add column showiing the Month over Month cgange in trip_total for every company
with SUMMARY as (
SELECT
DATE_TRUNC(EXTRACT(DATE FROM trip_start_timestamp),MONTH) as Month,
company,
SUM(trip_total) as trip_total,
SUM(TIPS)/sum(trip_total) as TIPS_SHARE_OF_TOTAL_REVENUE,
COUNT(IF(TIPS>0,UNIQUE_KEY,NULL))/COUNT(UNIQUE_KEY) as perc_tipping,
COUNT(unique_key) as total_trips,
SUM(trip_total)/sum(trip_miles) as dollar_per_mile
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
where trip_total > 0 and trip_miles > 0
group by 1,2
)
SELECT Month,
       company,
       trip_total,
       trip_total - LAG(trip_total) OVER (PARTITION BY company ORDER BY Month ASC) AS Monthly_Growth
FROM SUMMARY
;

-----Using bigquery-public-data.hacker_news.full 
select * from `bigquery-public-data.hacker_news.full` limit 10;


--Q9-- Create a Bag of Word for the text field in bigquery-public-data.hacker_news.full using Text Analytics functions
SELECT a.text, a.token, BAG_OF_WORDS(a.token) as bag_of_words FROM
(select text, TEXT_ANALYZE(text) as token
FROM `bigquery-public-data.hacker_news.full`

limit 10) a;

--Q10-- using User Defined Function - justfunctions.us.remove_en_stopwords - right a query to retireve text 
-- from after removing stop words and limit results to 10 rows
-- https://justdataplease.com/justfunctions-bigquery/tag/nlp/?function=remove_en_stopwords

SELECT b.text, b.removed_en_stopwords, b.token, BAG_OF_WORDS(b.token) as bag_of_words FROM
(SELECT a.text, a.removed_en_stopwords, TEXT_ANALYZE(removed_en_stopwords) as token FROM
(SELECT text, `justfunctions.us.remove_en_stopwords`(text) as removed_en_stopwords
FROM `bigquery-public-data.hacker_news.full`

limit 10) as a) as b;


