def construct_model(self, qc, qp1, qp2, q0, Protocol):
    """
    Construct a model based on which parameters are present in the parameter
    dictionary

    Inputs:
    qc: a variable representing the quantity of drug q in the central
    compartment
    qp1: a variable representing the quantity of drug q in the first
    peripheral compartment
    qp2: a variable representing the quantity of drug q in the second
    peripheral compartment
    q0: a variable representing the initial quantity of drug used in
    subcutaneous dosing
    Protocol: an instance of class Protocol stating which dosing protocol is
    being used

    Returns:
    Between one and four rate equations, depending on the input parameters for
    the model describing the rate of drug flow in the central compartment
    """
    param_dict = self.construct_param_dict()
    Dose_t = Protocol
    dqc_dt = Dose_t - ((qc / param_dict['V_c']) * param_dict['CL'])
    if 'Q_p1' and 'K_a' not in param_dict:
        return dqc_dt
    if 'Q_p1' in param_dict:
        dqp1_dt = param_dict['Q_p1'] * (
            (qc / param_dict['V_c']) - (qp1 / param_dict['V_p1']))
        dqc_dt_single_peripheral = dqc_dt - dqp1_dt
        if 'K_a' and 'Q_p2' not in param_dict:
            return [dqc_dt_single_peripheral, dqp1_dt]
    if 'Q_p2' in param_dict:
        dqp2_dt = param_dict['Q_p2'] * (
            (qc / param_dict['V_c']) - (qp2 / param_dict['V_p2']))
        dqc_dt_two_peripherals = dqc_dt_single_peripheral - dqp2_dt
        if 'K_a' not in param_dict:
            return [dqc_dt_two_peripherals, dqp1_dt, dqp2_dt]
    if 'K_a' in param_dict:
        dq0_dt = Dose_t - (param_dict['K_a'] * q0)
        dqc_dt = (param_dict['K_a'] * q0) - (
            (qc / param_dict['V_c']) * param_dict['CL'])
        if 'Q_p1' in param_dict:
            dqc_dt_single_peripheral = dqc_dt - dqp1_dt
            if 'Q_p2' not in param_dict:
                return [dq0_dt, dqc_dt_single_peripheral, dqp1_dt]
            else:
                dqc_dt_two_peripherals = dqc_dt_single_peripheral - dqp2_dt
                return [dq0_dt, dqc_dt_two_peripherals, dqp1_dt, dqp2_dt]
        else:
            return [dq0_dt, dqc_dt]
