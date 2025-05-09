CREATE TABLE pagina (
	id SERIAL PRIMARY KEY,
	accesTime TIME NOT NULL,
	userip VARCHAR(100),
	visitedPage VARCHAR(200),
	visitTime INTERVAL NOT NULL
)

SELECT DATE_TRUNC('hour', accesTime) AS time, COUNT(*) AS totalOfVisits
FROM pagina
GROUP BY time
ORDER BY totalOfVisits DESC;