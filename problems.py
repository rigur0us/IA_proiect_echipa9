# diagnostic hardware 
def hardware_sources(temp_def1, temp_def2, temp_func, temp_uncertain1, temp_uncertain2,
                     log_def1, log_def2, log_func, log_uncertain1, log_uncertain2):
    """
    Creează dicționarele de masă pentru sursele hardware cu 5 stări
    valorile între 0 și 1
    """
    m_temp = {
        set({"DEFECT_ELECTRONIC"}): temp_def1,
        set({"DEFECT_MECHANIC"}): temp_def2,
        set({"FUNCTIONAL"}): temp_func,
        set({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC"}): temp_uncertain1,
        set({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC", "FUNCTIONAL"}): temp_uncertain2
    }

    m_logs = {
        set({"DEFECT_ELECTRONIC"}): log_def1,
        set({"DEFECT_MECHANIC"}): log_def2,
        set({"FUNCTIONAL"}): log_func,
        set({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC"}): log_uncertain1,
        set({"DEFECT_ELECTRONIC", "DEFECT_MECHANIC", "FUNCTIONAL"}): log_uncertain2
    }

    return m_temp, m_logs


# diagnostic situație de urgență
def emergency_sources(smoke_em, smoke_heat, smoke_normal, smoke_uncertain1, smoke_uncertain2,
                      heat_em, heat_heat, heat_normal, heat_uncertain1, heat_uncertain2):
    """
    Creeaza dicționarele de masa pentru sursele de urgenta cu 5 stari
    """
    m_smoke = {
        set({"EMERGENCY_FIRE"}): smoke_em,
        set({"EMERGENCY_HEAT"}): smoke_heat,
        set({"NORMAL"}): smoke_normal,
        set({"EMERGENCY_FIRE", "EMERGENCY_HEAT"}): smoke_uncertain1,
        set({"EMERGENCY_FIRE", "EMERGENCY_HEAT", "NORMAL"}): smoke_uncertain2
    }

    m_heat = {
        set({"EMERGENCY_FIRE"}): heat_em,
        set({"EMERGENCY_HEAT"}): heat_heat,
        set({"NORMAL"}): heat_normal,
        set({"EMERGENCY_FIRE", "EMERGENCY_HEAT"}): heat_uncertain1,
        set({"EMERGENCY_FIRE", "EMERGENCY_HEAT", "NORMAL"}): heat_uncertain2
    }

    return m_smoke, m_heat
