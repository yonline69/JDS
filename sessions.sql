-- Write only the SQL statement that solves the problem and nothing else.
select userid, avg(duration) AverageDuration
	from sessions
	group by 1
	having count(*)>1