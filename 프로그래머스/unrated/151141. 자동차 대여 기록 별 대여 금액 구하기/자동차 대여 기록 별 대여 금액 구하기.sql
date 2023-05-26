-- 코드를 입력하세요
SELECT  HISTORY_ID,
        (PIREOD * ROUND(DAILY_FEE - (DAILY_FEE*DISCOUNT_RATE), 0)) AS FEE
FROM(
   SELECT *,
   CASE WHEN PIREOD >= 90 THEN (SELECT DISCOUNT_RATE / 100
                                  FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                  WHERE CAR_TYPE = "트럭"
                                  AND DURATION_TYPE = "90일 이상")
        WHEN PIREOD >= 30 THEN (SELECT DISCOUNT_RATE / 100
                                   FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                  WHERE CAR_TYPE = "트럭"
                                  AND DURATION_TYPE = "30일 이상")
        WHEN PIREOD >= 7 THEN (SELECT DISCOUNT_RATE / 100
                                   FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                  WHERE CAR_TYPE = "트럭"
                                  AND DURATION_TYPE = "7일 이상")
        ELSE 0.00 END AS DISCOUNT_RATE
                
FROM (
SELECT *, DATEDIFF(END_DATE, START_DATE) + 1 AS 'PIREOD'
FROM (
SELECT CAR.car_id, CAR.car_type, daily_fee, history_id, start_date, end_date
FROM CAR_RENTAL_COMPANY_CAR CAR JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY HIS
ON CAR.CAR_ID = HIS.CAR_ID
WHERE CAR.CAR_TYPE = "트럭") TBL1) TBL2) TBL3
ORDER BY FEE DESC, HISTORY_ID DESC;
;