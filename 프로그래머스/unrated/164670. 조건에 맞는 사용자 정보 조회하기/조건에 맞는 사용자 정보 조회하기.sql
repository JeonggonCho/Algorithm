-- 코드를 입력하세요
SELECT DISTINCT
    USER_ID,
    NICKNAME,
    CONCAT(CITY,' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소',
    CASE LENGTH(A.TLNO)
		WHEN 11 THEN CONCAT(LEFT(A.TLNO, 3), '-', MID(A.TLNO, 4, 4), '-', RIGHT(A.TLNO, 4))
        END AS '전화번호'
FROM USED_GOODS_USER AS A
INNER JOIN USED_GOODS_BOARD AS B ON A.USER_ID = B.WRITER_ID
WHERE WRITER_ID IN (SELECT WRITER_ID FROM USED_GOODS_BOARD GROUP BY WRITER_ID HAVING COUNT(WRITER_ID) >= 3)
ORDER BY USER_ID DESC;