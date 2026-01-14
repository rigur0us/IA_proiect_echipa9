# =============================
# PROBLEMA 1 – Diagnostic hardware (5 stari)
# =============================

def hardware_sources(temp_def1, temp_def2, temp_func, temp_uncertain1, temp_uncertain2,
                     log_def1, log_def2, log_func, log_uncertain1, log_uncertain2):
    """
    Creează dicționarele de masă pentru sursele hardware cu 5 stări
    valorile între 0 și 1
    """
    m_temp = {
        frozenset({"DEFECT_ELECTRONIC"}): temp_def1,
        frozenset({"DEFECT_MECHANIC"}): temp_def2,
        frozenset({"FUNCTIONAL"}): temp_func,
        frozenset({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC"}): temp_uncertain1,
        frozenset({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC", "FUNCTIONAL"}): temp_uncertain2
    }

    m_logs = {
        frozenset({"DEFECT_ELECTRONIC"}): log_def1,
        frozenset({"DEFECT_MECHANIC"}): log_def2,
        frozenset({"FUNCTIONAL"}): log_func,
        frozenset({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC"}): log_uncertain1,
        frozenset({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC", "FUNCTIONAL"}): log_uncertain2
    }

    return m_temp, m_logs


# =============================
# PROBLEMA 2 – Situatie de urgentă (5 stari)
# =============================

def emergency_sources(smoke_em, smoke_heat, smoke_normal, smoke_uncertain1, smoke_uncertain2,
                      heat_em, heat_heat, heat_normal, heat_uncertain1, heat_uncertain2):
    """
    Creeaza dicționarele de masa pentru sursele de urgenta cu 5 stari
    """
    m_smoke = {
        frozenset({"EMERGENCY_FIRE"}): smoke_em,
        frozenset({"EMERGENCY_HEAT"}): smoke_heat,
        frozenset({"NORMAL"}): smoke_normal,
        frozenset({"EMERGENCY_FIRE", "EMERGENCY_HEAT"}): smoke_uncertain1,
        frozenset({"EMERGENCY_FIRE", "EMERGENCY_HEAT", "NORMAL"}): smoke_uncertain2
    }

    m_heat = {
        frozenset({"EMERGENCY_FIRE"}): heat_em,
        frozenset({"EMERGENCY_HEAT"}): heat_heat,
        frozenset({"NORMAL"}): heat_normal,
        frozenset({"EMERGENCY_FIRE", "EMERGENCY_HEAT"}): heat_uncertain1,
        frozenset({"EMERGENCY_FIRE", "EMERGENCY_HEAT", "NORMAL"}): heat_uncertain2
    }

    return m_smoke, m_heat
