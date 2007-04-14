#--------------------------------------------------------------------#
# ������ : 2007.01.30
# ������ : �ڽµ�
#--------------------------------------------------------------------#
# dS_ABA01TN_001:���������ȹ���� ��ȸ
#--------------------------------------------------------------------#
dS_ABA01TN_001:
    SELECT
        [CHAR]T1.PBENT_CD            ,  /*������ڵ�*/
        [CHAR]T1.ACCYEAR             ,  /*ȸ��⵵*/
        [CHAR]T1.BGT_GB_CD           ,  /*���걸���ڵ�*/
        [CHAR]T1.BA_PLAN_SEQ         ,  /*������ȹ�Ϸù�ȣ*/
        [CHAR]T1.EX_ITEM_CD          ,  /*���⼼���ڵ�*/
        [CHAR]T1.EX_NATURE_CD        ,  /*������ڵ�*/
        [CHAR]T1.EX_SNATURE_CD       ,  /*���⼼���ڵ�*/
        [CHAR]T1.PRJ_CD              ,  /*����ڵ�*/
        [CHAR]T1.DEPT_CD             ,  /*�μ��ڵ�*/
        [CHAR]T1.BGT_GB_CDID         ,  /*���걸���ڵ�ID*/
        [CHAR]T1.PLAN_DATE           ,  /*��ȹ����*/
        [CHAR]T1.PLAN_AMT            ,  /*��ȹ�ݾ�*/
        [CHAR]T1.ASGN_GB_CDID        ,  /*���������ڵ�ID*/
        [CHAR]T1.ASGN_GB_CD          ,  /*���������ڵ�*/
        [CHAR]T1.BA_YN               ,  /*�����������*/
        [CHAR]T1.REG_DT              ,  /*����Ͻ�*/
        [CHAR]T1.REGR_ID             ,  /*�����ID*/
        [CHAR]T1.CHG_DT              ,  /*�����Ͻ�*/
        [CHAR]T1.CHGR_ID             ,  /*������ID*/
    FROM ABA01TN T1
    WHERE T1.PBENT_CD                       = $IN_PBENT_CD                      [CHAR]   /*������ڵ�*/
    AND   T1.ACCYEAR                        = $IN_ACCYEAR                       [CHAR]   /*ȸ��⵵*/
    AND   T1.BGT_GB_CD                      = $IN_BGT_GB_CD                     [CHAR]   /*���걸���ڵ�*/
    AND   T1.BA_PLAN_SEQ                    = $IN_BA_PLAN_SEQ                   [CHAR]   /*������ȹ�Ϸù�ȣ*/
;
#--------------------------------------------------------------------#
# ������ : 2007.01.30
# ������ : �ڽµ�
#--------------------------------------------------------------------#
# dI_ABA01TN_001:���������ȹ���� ���
#--------------------------------------------------------------------#
dI_ABA01TN_001:
    INSERT INTO ABA01TN
        (
        PBENT_CD            ,   /*������ڵ�*/
        ACCYEAR             ,   /*ȸ��⵵*/
        BGT_GB_CD           ,   /*���걸���ڵ�*/
        BA_PLAN_SEQ         ,   /*������ȹ�Ϸù�ȣ*/
        EX_ITEM_CD          ,   /*���⼼���ڵ�*/
        EX_NATURE_CD        ,   /*������ڵ�*/
        EX_SNATURE_CD       ,   /*���⼼���ڵ�*/
        PRJ_CD              ,   /*����ڵ�*/
        DEPT_CD             ,   /*�μ��ڵ�*/
        BGT_GB_CDID         ,   /*���걸���ڵ�ID*/
        PLAN_DATE           ,   /*��ȹ����*/
        PLAN_AMT            ,   /*��ȹ�ݾ�*/
        ASGN_GB_CDID        ,   /*���������ڵ�ID*/
        ASGN_GB_CD          ,   /*���������ڵ�*/
        BA_YN               ,   /*�����������*/
        REG_DT              ,   /*����Ͻ�*/
        REGR_ID             ,   /*�����ID*/
        CHG_DT              ,   /*�����Ͻ�*/
        CHGR_ID             ,   /*������ID*/
        )
    VALUES
        (
        $IN_PBENT_CD            [CHAR],   /*������ڵ�*/
        $IN_ACCYEAR             [CHAR],   /*ȸ��⵵*/
        $IN_BGT_GB_CD           [CHAR],   /*���걸���ڵ�*/
        $IN_BA_PLAN_SEQ         [CHAR],   /*������ȹ�Ϸù�ȣ*/
        $IN_EX_ITEM_CD          [CHAR],   /*���⼼���ڵ�*/
        $IN_EX_NATURE_CD        [CHAR],   /*������ڵ�*/
        $IN_EX_SNATURE_CD       [CHAR],   /*���⼼���ڵ�*/
        $IN_PRJ_CD              [CHAR],   /*����ڵ�*/
        $IN_DEPT_CD             [CHAR],   /*�μ��ڵ�*/
        $IN_BGT_GB_CDID         [CHAR],   /*���걸���ڵ�ID*/
        $IN_PLAN_DATE           [CHAR],   /*��ȹ����*/
        $IN_PLAN_AMT            [CHAR],   /*��ȹ�ݾ�*/
        $IN_ASGN_GB_CDID        [CHAR],   /*���������ڵ�ID*/
        $IN_ASGN_GB_CD          [CHAR],   /*���������ڵ�*/
        $IN_BA_YN               [CHAR],   /*�����������*/
        $IN_REG_DT              [CHAR],   /*����Ͻ�*/
        $IN_REGR_ID             [CHAR],   /*�����ID*/
        $IN_CHG_DT              [CHAR],   /*�����Ͻ�*/
        $IN_CHGR_ID             [CHAR],   /*������ID*/
        )
;
#--------------------------------------------------------------------#
# ������ : 2007.01.30
# ������ : �ڽµ�
#--------------------------------------------------------------------#
# dU_ABA01TN_001:���������ȹ���� ����
#--------------------------------------------------------------------#
dU_ABA01TN_001:
    UPDATE ABA01TN
    SET
        EX_ITEM_CD           = $IN_EX_ITEM_CD          [CHAR],   /*���⼼���ڵ�*/
        EX_NATURE_CD         = $IN_EX_NATURE_CD        [CHAR],   /*������ڵ�*/
        EX_SNATURE_CD        = $IN_EX_SNATURE_CD       [CHAR],   /*���⼼���ڵ�*/
        PRJ_CD               = $IN_PRJ_CD              [CHAR],   /*����ڵ�*/
        DEPT_CD              = $IN_DEPT_CD             [CHAR],   /*�μ��ڵ�*/
        BGT_GB_CDID          = $IN_BGT_GB_CDID         [CHAR],   /*���걸���ڵ�ID*/
        PLAN_DATE            = $IN_PLAN_DATE           [CHAR],   /*��ȹ����*/
        PLAN_AMT             = $IN_PLAN_AMT            [CHAR],   /*��ȹ�ݾ�*/
        ASGN_GB_CDID         = $IN_ASGN_GB_CDID        [CHAR],   /*���������ڵ�ID*/
        ASGN_GB_CD           = $IN_ASGN_GB_CD          [CHAR],   /*���������ڵ�*/
        BA_YN                = $IN_BA_YN               [CHAR],   /*�����������*/
        REG_DT               = $IN_REG_DT              [CHAR],   /*����Ͻ�*/
        REGR_ID              = $IN_REGR_ID             [CHAR],   /*�����ID*/
        CHG_DT               = $IN_CHG_DT              [CHAR],   /*�����Ͻ�*/
        CHGR_ID              = $IN_CHGR_ID             [CHAR],   /*������ID*/
    WHERE PBENT_CD                       = $IN_PBENT_CD                      [CHAR]   /*������ڵ�*/
    AND   ACCYEAR                        = $IN_ACCYEAR                       [CHAR]   /*ȸ��⵵*/
    AND   BGT_GB_CD                      = $IN_BGT_GB_CD                     [CHAR]   /*���걸���ڵ�*/
    AND   BA_PLAN_SEQ                    = $IN_BA_PLAN_SEQ                   [CHAR]   /*������ȹ�Ϸù�ȣ*/
;
#--------------------------------------------------------------------#
# ������ : 2007.01.30
# ������ : �ڽµ�
#--------------------------------------------------------------------#
# dD_ABA01TN_001:���������ȹ���� ����
#--------------------------------------------------------------------#
dD_ABA01TN_001:
    DELETE FROM ABA01TN
    WHERE PBENT_CD                       = $IN_PBENT_CD                      [CHAR]   /*������ڵ�*/
    AND   ACCYEAR                        = $IN_ACCYEAR                       [CHAR]   /*ȸ��⵵*/
    AND   BGT_GB_CD                      = $IN_BGT_GB_CD                     [CHAR]   /*���걸���ڵ�*/
    AND   BA_PLAN_SEQ                    = $IN_BA_PLAN_SEQ                   [CHAR]   /*������ȹ�Ϸù�ȣ*/
;
