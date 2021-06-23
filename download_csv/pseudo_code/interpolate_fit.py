import math   # This will import math module

def interpolate_fit(XP5_speed, XP5_delta_side_DividedBy_main, temperature):
    multi_P_main=0.14098955779328007
    multi_P_side=0.1695240837743458
    multi_T_main=0.25053404360183934
    multi_T_side=0.28074314221003555

    # =====
    # Equation 2.19 (Dvorak, 2013) (National Aeronautics and Space Administration (NASA), 2021 a)
    y_subscript_a=
    R_subscript_a=
    T=
    c = math.sqrt(y_subscript_a * R_subscript_a * T)
    tau=
    n=
    D_subscript_prop=
    M_subscript_tip = (tau * n * D_subscript_prop) / c
    M_tip=M_subscript_tip

    # =====
    # Equation 2.18 (Spakovszky, n.d.)
    # J=V_subscript_infinite / (n * D_subscript_prop) =>
    V_subscript_infinite=
    n=
    D_subscript_prop=
    equation_2_18=V_subscript_infinite / (n * D_subscript_prop)

    # =====
    # Equation 3.3 (Stokkermans & Veldhuis, 2021)or Equation 3.4 (Stokkermans & Veldhuis, 2021)
    # 𝑦(M_subscript_tip) = (𝑝_subscript_1 ∗ (M_subscript_tip)superscript_3) +
    #                       (𝑝_subscript_2 ∗ (M_subscript_tip)superscript_2) +
    #                       (𝑝_subscript_3 ∗ (M_subscript_tip)) +
    #                       𝑝_subscript_4
    𝑝_subscript_1=1
    M_subscript_tipExp3=M_subscript_tip**3
    𝑝_subscript_2=1
    M_subscript_tipExp2=M_subscript_tip**2
    𝑝_subscript_3=1
    equation_3_3=𝑝_subscript_1 * M_subscript_tipExp3 + 𝑝_subscript_2 * M_subscript_tipExp2 + 𝑝_subscript_3 * M_subscript_tip + 𝑝_subscript_4
    𝑝_subscript_4=1
    C_t=equation_3_3        # (Stokkermans & Veldhuis, 2021)or Equation 3.4 (Stokkermans & Veldhuis, 2021)
    C_p=equation_3_3        # (Stokkermans & Veldhuis, 2021)or Equation 3.4 (Stokkermans & Veldhuis, 2021)
    C_F_Y=equation_3_3      # (Stokkermans & Veldhuis, 2021)or Equation 3.4 (Stokkermans & Veldhuis, 2021)
    C_F_Z=equation_3_3      # (Stokkermans & Veldhuis, 2021)or Equation 3.4 (Stokkermans & Veldhuis, 2021)

    if 0 <= XP5_delta_side_DividedBy_main <= 15:
        # Filter thrust_fit on delta_
        side_main=[0,15]
    elif 15 <= XP5_delta_side_DividedBy_main <= 30:
        # Filter thrust_fit on delta_
        side_main=[15,30]
    elif 30 <= XP5_delta_side_DividedBy_main <= 45:
        # Filter thrust_fit on delta_
        side_main=[30,45]
    elif 45 <= XP5_delta_side_DividedBy_main <= 60:
        # Filter thrust_fit on delta_
        side_main=[45,60]
    elif 60 <= XP5_delta_side_DividedBy_main <= 75:
        # Filter thrust_fit on delta_
        side_main=[60,75]
    elif 75 <= XP5_delta_side_DividedBy_main <= 90:
        # Filter thrust_fit on delta_
        side_main=[75,90]


    if 0 <= XP5_speed <= 6:
        # Filter thrust_fit on
        V_inf=[0,6]
    elif 6 <= XP5_speed <= 12:
        # Filter thrust_fit on
        V_inf=[6,12]
    elif 12 <= XP5_speed <= 18:
        # Filter thrust_fit on
        V_inf=[12,18]


    # Means that thrust is <= 6 m/s
    if length of thrust_fit == 2:
#         F_Y_interp1=interpolated F_Y value for XP5_delta_side_DividedBy_main, higher speed border
#         F_Z_interp1=interpolated F_Z value for XP5_delta_side_DividedBy_main, higher speed border
#         thrust_interp1=interpolated thrust value for XP5_delta_side_DividedBy_main, higher speed border
#         power_interp1 interpolated power value for XP5_delta_side_DividedBy_main, higher speed border
#         F_Y_output=multi_T_main/side * interpolated F_Y value for XP5_speed between speed 0 m/s
#         and F_Y_interp1
#         F_Z_output=multi_T_main/side * interpolated F_Z value for XP5_speed between speed 0 m/s
#         and F_Z_interp1
#         thrust_output=multi_T_main/side * interpolated thrust value for XP5_speed between speed 0
#         m/s and thrust_interp1
#         power_output=multi_P_main/side * interpolated power value for XP5_speed between speed 0
#         m/s and power_interp1
#         57
#     ELIF length of thrust_fit == 4:
#         # Means that thrust is > 6 m/s
#         F_Y_interp1=interpolated F_Y value for XP5_delta_side_DividedBy_main, lower speed border
#         F_Z_interp1=interpolated F_Z value for XP5_delta_side_DividedBy_main, lower speed border
#         thrust_interp1=interpolated thrust value for XP5_delta_side_DividedBy_main, lower speed border
#         power_interp1=interpolated power value for XP5_delta_side_DividedBy_main, lower speed border
#         F_Y_interp2=interpolated F_Y value for XP5_delta_side_DividedBy_main, higher speed border
#         F_Z_interp2=interpolated F_Z value for XP5_delta_side_DividedBy_main, higher speed border
#         thrust_interp2=interpolated thrust value for XP5_delta_side_DividedBy_main, higher speed border
#         power_interp2=interpolated power value for XP5_delta_side_DividedBy_main, higher speed border
#         F_Y_output=multi_T_main/side * interpolated F_Y value for XP5_speed between
#         F_Y_interp1 and F_Y_interp2
#         F_Z_output=multi_T_main/side * interpolated F_Z value for XP5_speed between
#         F_Z_interp1 and F_Z_interp2
#         thrust_output=multi_T_main/side * interpolated thrust value for XP5_speed between
#         thrust_interp1 and thrust_interp2
#         power_output=multi_P_main/side * interpolated power value for XP5_speed between
#         power_interp1 and power_interp2
#     ELSE:
#         print("Interpolation error")

#     # To pessimistically compensate for F_Y_output
#     thrust_provided=thrust_output- F_Y_output
#     IF power_output <= 0:
#         # to prevent negative powers
#         power_required=2
#     ELSE:
#         power_required=power_output


    if __name__ == '__main__':
        XP5_speed=2.0
        # pseudocode: XP5_delta_side/main
        XP5_delta_side_DividedBy_main= 6.0/3
        temperature=273
        result=interpolate_fit(XP5_speed, XP5_delta_side_DividedBy_main, temperature)
        print(f'{result=}')
