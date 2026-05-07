select *
from 
	app_movie_movie m
	join app_people_person p on m.director_id = p.id
where
	p.name= 'Christopher Nolan'
;

select * 
from app_people_person p
where p.name= 'Christopher Nolan'
;


select *
from pg_stats
where tablename = 'app_people_person';

-- Defragmentation
vacuum full ANALYSE;
;

select * from pg_database;
select * from pg_class where relname = 'app_people_person';


SELECT
    relname                                        AS table_name,
    pg_size_pretty(pg_total_relation_size(relid))  AS total_size,
    n_live_tup                                     AS live_tuples,
    n_dead_tup                                     AS dead_tuples,
    ROUND(
        CASE WHEN n_live_tup + n_dead_tup > 0
             THEN 100.0 * n_dead_tup / (n_live_tup + n_dead_tup)
             ELSE 0
        END, 2
    )                                              AS dead_pct,
    last_vacuum,
    last_autovacuum
FROM pg_stat_user_tables
WHERE relname LIKE 'app_%'
ORDER BY pg_total_relation_size(relid) DESC;


