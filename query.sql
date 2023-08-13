SELECT SEQUENCE, FROM_UNIXTIME(TIMESTAMP), EMPLOYEE_ID, INET_NTOA(S_IP),
 CONCAT(
        RIGHT(CONV(S_MAC >> 40 & 255, 10, 16), 2),":",
        RIGHT(CONV(S_MAC >> 32 & 255, 10, 16), 2),":",
        RIGHT(CONV(S_MAC >> 24 & 255, 10, 16), 2),":",
        RIGHT(CONV(S_MAC >> 16 & 255, 10, 16), 2),":",
        RIGHT(CONV(S_MAC >> 8 & 255, 10, 16), 2), ":",
        RIGHT(CONV(S_MAC & 255, 10, 16), 2)) AS S_MAC,
S_PORT,
INET_NTOA(D_IP),
 CONCAT(
        RIGHT(CONV(D_MAC >> 40 & 255, 10, 16), 2),":",
        RIGHT(CONV(D_MAC >> 32 & 255, 10, 16), 2),":",
        RIGHT(CONV(D_MAC >> 24 & 255, 10, 16), 2),":",
        RIGHT(CONV(D_MAC >> 16 & 255, 10, 16), 2),":",
        RIGHT(CONV(D_MAC >> 8 & 255, 10, 16), 2), ":",
        RIGHT(CONV(D_MAC & 255, 10, 16), 2)) AS D_MAC,
D_PORT,
SIZE
FROM log.log 
WHERE
	D_PORT NOT IN (4552,2553,6221,6222,6743,6744,10530,15636,12375,12378,20105,32051,53243,54443,
    57432,2053,2078,10532,1385,2053,4375,8537,10375,20157,30572,10132,10367)
