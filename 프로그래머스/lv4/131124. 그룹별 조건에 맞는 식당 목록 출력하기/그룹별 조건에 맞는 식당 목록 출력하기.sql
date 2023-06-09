-- 코드를 입력하세요
SELECT PRO.MEMBER_NAME, REV.REVIEW_TEXT, DATE_FORMAT(REV.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE PRO INNER JOIN  REST_REVIEW REV
ON PRO.MEMBER_ID = REV.MEMBER_ID 
WHERE REV.MEMBER_ID = (SELECT REV.MEMBER_ID FROM REST_REVIEW REV GROUP BY REV.MEMBER_ID ORDER BY COUNT(*) DESC LIMIT 1)

ORDER BY REV.REVIEW_DATE, REV.REVIEW_TEXT;