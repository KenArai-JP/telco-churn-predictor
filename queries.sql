-- Top genres on Netflix
SELECT listed_in, COUNT(*) AS count
FROM netflix_titles
GROUP BY listed_in
ORDER BY count DESC
LIMIT 10;

-- Average movie duration by country
SELECT country, AVG(CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED)) AS avg_duration
FROM netflix_titles
WHERE type = 'Movie' AND duration LIKE '%min%'
GROUP BY country
ORDER BY avg_duration DESC
LIMIT 10;

-- Number of titles released each year
SELECT release_year, COUNT(*) AS total
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year;


-- Top 10 Countries with Most Content
SELECT 
  CASE 
    WHEN country IS NULL OR country = '' THEN 'Unknown'
    ELSE country
  END AS country_label,
  COUNT(*) AS total
FROM netflix_titles
GROUP BY country_label
ORDER BY total DESC
LIMIT 10;