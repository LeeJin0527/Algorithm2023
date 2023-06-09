-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, IF(STATUS = "DONE", "거래완료", IF(STATUS = "RESERVED", "예약중","판매중")) AS STATUS
FROM USED_GOODS_BOARD
WHERE YEAR(CREATED_DATE) = 2022 AND MONTH(CREATED_DATE) = 10 AND DAY(CREATED_DATE) = 05
ORDER BY BOARD_ID DESC;