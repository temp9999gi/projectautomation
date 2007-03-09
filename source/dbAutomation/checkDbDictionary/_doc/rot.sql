#--------------------------------------------------------------------#
# 수정일 : 2007.01.30
# 수정자 : 박승도
#--------------------------------------------------------------------#
# dS_ABA01TN_001:예산배정계획내역 조회
#--------------------------------------------------------------------#
dS_ABA01TN_001:
    SELECT
        [CHAR]T1.PBENT_CD            ,  /*공기업코드*/
        [CHAR]T1.ACCYEAR             ,  /*회계년도*/
        [CHAR]T1.BGT_GB_CD           ,  /*예산구분코드*/
        [CHAR]T1.BA_PLAN_SEQ         ,  /*배정계획일련번호*/
        [CHAR]T1.EX_ITEM_CD          ,  /*지출세항코드*/
        [CHAR]T1.EX_NATURE_CD        ,  /*지출목코드*/
        [CHAR]T1.EX_SNATURE_CD       ,  /*지출세목코드*/
        [CHAR]T1.PRJ_CD              ,  /*사업코드*/
        [CHAR]T1.DEPT_CD             ,  /*부서코드*/
        [CHAR]T1.BGT_GB_CDID         ,  /*예산구분코드ID*/
        [CHAR]T1.PLAN_DATE           ,  /*계획일자*/
        [CHAR]T1.PLAN_AMT            ,  /*계획금액*/
        [CHAR]T1.ASGN_GB_CDID        ,  /*배정구분코드ID*/
        [CHAR]T1.ASGN_GB_CD          ,  /*배정구분코드*/
        [CHAR]T1.BA_YN               ,  /*예산배정여부*/
        [CHAR]T1.REG_DT              ,  /*등록일시*/
        [CHAR]T1.REGR_ID             ,  /*등록자ID*/
        [CHAR]T1.CHG_DT              ,  /*변경일시*/
        [CHAR]T1.CHGR_ID             ,  /*변경자ID*/
    FROM ABA01TN T1
    WHERE T1.PBENT_CD                       = $IN_PBENT_CD                      [CHAR]   /*공기업코드*/
    AND   T1.ACCYEAR                        = $IN_ACCYEAR                       [CHAR]   /*회계년도*/
    AND   T1.BGT_GB_CD                      = $IN_BGT_GB_CD                     [CHAR]   /*예산구분코드*/
    AND   T1.BA_PLAN_SEQ                    = $IN_BA_PLAN_SEQ                   [CHAR]   /*배정계획일련번호*/
;
#--------------------------------------------------------------------#
# 수정일 : 2007.01.30
# 수정자 : 박승도
#--------------------------------------------------------------------#
# dI_ABA01TN_001:예산배정계획내역 등록
#--------------------------------------------------------------------#
dI_ABA01TN_001:
    INSERT INTO ABA01TN
        (
        PBENT_CD            ,   /*공기업코드*/
        ACCYEAR             ,   /*회계년도*/
        BGT_GB_CD           ,   /*예산구분코드*/
        BA_PLAN_SEQ         ,   /*배정계획일련번호*/
        EX_ITEM_CD          ,   /*지출세항코드*/
        EX_NATURE_CD        ,   /*지출목코드*/
        EX_SNATURE_CD       ,   /*지출세목코드*/
        PRJ_CD              ,   /*사업코드*/
        DEPT_CD             ,   /*부서코드*/
        BGT_GB_CDID         ,   /*예산구분코드ID*/
        PLAN_DATE           ,   /*계획일자*/
        PLAN_AMT            ,   /*계획금액*/
        ASGN_GB_CDID        ,   /*배정구분코드ID*/
        ASGN_GB_CD          ,   /*배정구분코드*/
        BA_YN               ,   /*예산배정여부*/
        REG_DT              ,   /*등록일시*/
        REGR_ID             ,   /*등록자ID*/
        CHG_DT              ,   /*변경일시*/
        CHGR_ID             ,   /*변경자ID*/
        )
    VALUES
        (
        $IN_PBENT_CD            [CHAR],   /*공기업코드*/
        $IN_ACCYEAR             [CHAR],   /*회계년도*/
        $IN_BGT_GB_CD           [CHAR],   /*예산구분코드*/
        $IN_BA_PLAN_SEQ         [CHAR],   /*배정계획일련번호*/
        $IN_EX_ITEM_CD          [CHAR],   /*지출세항코드*/
        $IN_EX_NATURE_CD        [CHAR],   /*지출목코드*/
        $IN_EX_SNATURE_CD       [CHAR],   /*지출세목코드*/
        $IN_PRJ_CD              [CHAR],   /*사업코드*/
        $IN_DEPT_CD             [CHAR],   /*부서코드*/
        $IN_BGT_GB_CDID         [CHAR],   /*예산구분코드ID*/
        $IN_PLAN_DATE           [CHAR],   /*계획일자*/
        $IN_PLAN_AMT            [CHAR],   /*계획금액*/
        $IN_ASGN_GB_CDID        [CHAR],   /*배정구분코드ID*/
        $IN_ASGN_GB_CD          [CHAR],   /*배정구분코드*/
        $IN_BA_YN               [CHAR],   /*예산배정여부*/
        $IN_REG_DT              [CHAR],   /*등록일시*/
        $IN_REGR_ID             [CHAR],   /*등록자ID*/
        $IN_CHG_DT              [CHAR],   /*변경일시*/
        $IN_CHGR_ID             [CHAR],   /*변경자ID*/
        )
;
#--------------------------------------------------------------------#
# 수정일 : 2007.01.30
# 수정자 : 박승도
#--------------------------------------------------------------------#
# dU_ABA01TN_001:예산배정계획내역 수정
#--------------------------------------------------------------------#
dU_ABA01TN_001:
    UPDATE ABA01TN
    SET
        EX_ITEM_CD           = $IN_EX_ITEM_CD          [CHAR],   /*지출세항코드*/
        EX_NATURE_CD         = $IN_EX_NATURE_CD        [CHAR],   /*지출목코드*/
        EX_SNATURE_CD        = $IN_EX_SNATURE_CD       [CHAR],   /*지출세목코드*/
        PRJ_CD               = $IN_PRJ_CD              [CHAR],   /*사업코드*/
        DEPT_CD              = $IN_DEPT_CD             [CHAR],   /*부서코드*/
        BGT_GB_CDID          = $IN_BGT_GB_CDID         [CHAR],   /*예산구분코드ID*/
        PLAN_DATE            = $IN_PLAN_DATE           [CHAR],   /*계획일자*/
        PLAN_AMT             = $IN_PLAN_AMT            [CHAR],   /*계획금액*/
        ASGN_GB_CDID         = $IN_ASGN_GB_CDID        [CHAR],   /*배정구분코드ID*/
        ASGN_GB_CD           = $IN_ASGN_GB_CD          [CHAR],   /*배정구분코드*/
        BA_YN                = $IN_BA_YN               [CHAR],   /*예산배정여부*/
        REG_DT               = $IN_REG_DT              [CHAR],   /*등록일시*/
        REGR_ID              = $IN_REGR_ID             [CHAR],   /*등록자ID*/
        CHG_DT               = $IN_CHG_DT              [CHAR],   /*변경일시*/
        CHGR_ID              = $IN_CHGR_ID             [CHAR],   /*변경자ID*/
    WHERE PBENT_CD                       = $IN_PBENT_CD                      [CHAR]   /*공기업코드*/
    AND   ACCYEAR                        = $IN_ACCYEAR                       [CHAR]   /*회계년도*/
    AND   BGT_GB_CD                      = $IN_BGT_GB_CD                     [CHAR]   /*예산구분코드*/
    AND   BA_PLAN_SEQ                    = $IN_BA_PLAN_SEQ                   [CHAR]   /*배정계획일련번호*/
;
#--------------------------------------------------------------------#
# 수정일 : 2007.01.30
# 수정자 : 박승도
#--------------------------------------------------------------------#
# dD_ABA01TN_001:예산배정계획내역 삭제
#--------------------------------------------------------------------#
dD_ABA01TN_001:
    DELETE FROM ABA01TN
    WHERE PBENT_CD                       = $IN_PBENT_CD                      [CHAR]   /*공기업코드*/
    AND   ACCYEAR                        = $IN_ACCYEAR                       [CHAR]   /*회계년도*/
    AND   BGT_GB_CD                      = $IN_BGT_GB_CD                     [CHAR]   /*예산구분코드*/
    AND   BA_PLAN_SEQ                    = $IN_BA_PLAN_SEQ                   [CHAR]   /*배정계획일련번호*/
;
