consultas = {
    'tramobt': """select B.*  FROM
                (
                    select
                        'TRBT_' || LPAD(T.CODIGOTRAMOBT, 7, '0') AS CODIGOELEMENTO,
                        T.CODIGOAPOYO1 || T.CODIGONODOBT1 AS NODO1,
                        T.CODIGOAPOYO2 || T.CODIGONODOBT2 AS NODO2,
                        N1.CODIGOTRAFODIS AS CODTRAFODIS,
                        A1.X, A1.Y,
                        A2.X as X1, A2.Y AS Y1
                    from
                        TRAMOBT T,
                        NODOBT N1,
                        NODOBT N2,
                        APOYO A1,
                        APOYO A2
                    WHERE T.CODIGOAPOYO1 = N1.CODIGOAPOYO
                    AND T.CODIGONODOBT1 = N1.CODIGONODOBT
                    AND T.CODIGOAPOYO2 = N2.CODIGOAPOYO
                    AND T.CODIGONODOBT2 = N2.CODIGONODOBT
                    AND N1.CODIGOAPOYO = A1.CODIGOAPOYO
                    AND N2.CODIGOAPOYO = A2.CODIGOAPOYO
                union
                    select
                        'TRAFO_' || LPAD(T.CODIGOTRAFODIS, 7, '0') AS CODIGOELEMENTO,
                        T.CODIGOAPOYO1 || T.CODIGONODOMT AS NODO1,
                        T.CODIGOAPOYO2 || T.CODIGONODOBT AS NODO2,
                        n2.codigotrafodis AS CODTRAFODIS,
                        A1.X, A1.Y,
                        A2.X as X1, A2.Y AS Y1
                    from
                        TRAFODIS T,
                        NODOMT N1,
                        NODOBT N2,
                        APOYO A1,
                        APOYO A2
                    WHERE T.CODIGOAPOYO1 = N1.CODIGOAPOYO
                    AND T.CODIGONODOMT = N1.CODIGONODOMT
                    AND T.CODIGOAPOYO2 = N2.CODIGOAPOYO
                    AND T.CODIGONODOBT = N2.CODIGONODOBT
                    AND N1.CODIGOAPOYO = A1.CODIGOAPOYO
                    AND N2.CODIGOAPOYO = A2.CODIGOAPOYO
                ) B
                WHERE b.CODTRAFODIS IN (
                    select
                        TR.CODIGOTRAFODIS
                    from
                        TRAFODIS TR,
                        NODOMT N1
                    WHERE TR.CODIGOAPOYO1 = N1.CODIGOAPOYO
                    AND TR.CODIGONODOMT = N1.CODIGONODOMT
                    AND N1.CODIGOCIRCUITO =:CIRCUITO
                    )
                """
    ,
    "tramomt":  """select B.* FROM 
                (   
                    select  
                        'TR_' || LPAD(CODIGOTRAMOMT, 7, '0') AS CODIGOELEMENTO, 
                        CODIGOAPOYO1 || CODIGONODOMT1 AS NODO1, 
                        CODIGOAPOYO2 || CODIGONODOMT2 AS NODO2, 
                        N1.CODIGOCIRCUITO AS CODCTO1, 
                        N2.CODIGOCIRCUITO AS CODCTO2,
                        A1.X, A1.Y,
                        A2.X as X1, A2.Y AS Y1        
                    from 
                        TRAMOMT T, 
                        NODOMT N1, 
                        NODOMT N2,
                        APOYO A1,
                        APOYO A2
                    WHERE T.CODIGOAPOYO1 = N1.CODIGOAPOYO
                    AND T.CODIGONODOMT1 = N1.CODIGONODOMT
                    AND T.CODIGOAPOYO2 = N2.CODIGOAPOYO
                    AND T.CODIGONODOMT2 = N2.CODIGONODOMT
                    AND N1.CODIGOAPOYO = A1.CODIGOAPOYO
                    AND N2.CODIGOAPOYO = A2.CODIGOAPOYO
                    UNION
                    select 
                        'SW_' || LPAD(CODIGOINTERRUPTORDIS, 7, '0') AS CODIGOELEMENTO, 
                        CODIGOAPOYO1 || CODIGONODOMT1 AS NODO1, 
                        CODIGOAPOYO2 || CODIGONODOMT2 AS NODO2,  
                        N1.CODIGOCIRCUITO AS CODCTO1, 
                        N2.CODIGOCIRCUITO AS CODCTO2,
                        A1.X, A1.Y,
                        A2.X as X1, A2.Y AS Y1        
                    from 
                        INTERRUPTORDIS T, 
                        NODOMT N1, 
                        NODOMT N2,
                        APOYO A1,
                        APOYO A2
                    WHERE T.CODIGOAPOYO1 = N1.CODIGOAPOYO
                    AND T.CODIGONODOMT1 = N1.CODIGONODOMT
                    AND T.CODIGOAPOYO2 = N2.CODIGOAPOYO
                    AND T.CODIGONODOMT2 = N2.CODIGONODOMT
                    AND N1.CODIGOAPOYO = A1.CODIGOAPOYO
                    AND N2.CODIGOAPOYO = A2.CODIGOAPOYO
                ) B
                WHERE b.codcto1=:circuito
                """
}