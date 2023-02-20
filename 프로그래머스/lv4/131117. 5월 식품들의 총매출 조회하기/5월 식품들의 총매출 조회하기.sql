-- 코드를 입력하세요
SELECT t1.PRODUCT_ID, PRODUCT_NAME, SUM(t2.AMOUNT * t1.PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT AS t1
INNER JOIN FOOD_ORDER AS t2 ON t1.PRODUCT_ID = t2.PRODUCT_ID
WHERE
    YEAR(PRODUCE_DATE) = 2022
    AND MONTH(PRODUCE_DATE) = 05
GROUP BY PRODUCT_ID
ORDER BY
    TOTAL_SALES DESC,
    t1.PRODUCT_ID;