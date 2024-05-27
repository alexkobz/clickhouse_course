CREATE database shurik;

USE shurik;

CREATE table test (
a int, b String, c Enum('hello', 'world')
) Engine = Log();

SELECT *
FROM test
WHERE b LIKE '%abc%' AND a > 10;

INSERT INTO test
SELECT
	floor(randUniform(5, 50)) AS a,
	randomPrintableASCII(10) AS b,
	['hello', 'world'][randBernoulli(0.5)+1] AS c
FROM numbers(10000);

SELECT *
FROM test
WHERE b LIKE '%abc%' AND a > 10;
