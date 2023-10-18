SELECT * FROM
(SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME)
WHERE ROWNUM<=3

-- select *
-- from 
-- (
-- select i.name, i.datetime
-- from animal_ins i left join animal_outs o on i.animal_id = o.animal_id
-- and o.animal_id is null
-- order by i.datetime
-- )
-- where rownum < 4
