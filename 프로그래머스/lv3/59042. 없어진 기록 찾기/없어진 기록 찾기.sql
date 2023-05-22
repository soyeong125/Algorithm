select ANIMAL_ID, NAME
from ANIMAL_OUTS
where ANIMAL_ID not in (
select o.ANIMAL_ID
from ANIMAL_INS i , ANIMAL_OUTS o
where o.ANIMAL_ID = i.ANIMAL_ID
    )