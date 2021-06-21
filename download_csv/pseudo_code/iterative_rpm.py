# def iterative_rpm(rho_a, XP5_speed, XP5_delta_main, T, thrust_required):
#     IF thrust_required <= 4:
#         rpm = 1000
#     ELIF 4 < thrust_required < 8:
#         rpm = 13000
#     ELIF 8 < thrust_required < 12:
#         rpm = 1632
#     ELIF 12 < thrust_required < 16:
#         rpm = 1900
#     ELIF 16 < thrust_required < 20:
#         rpm = 2200
#     ELIF 20 < thrust_required < 24:
#         rpm = 2500
#     ELIF 24 < thrust_required < 28:
#         rpm = 2800
#     ELIF thrust_required > 28 :
#         rpm = 3090
#     END IF

#     WHILE absolute(thrust_required- thrust_provided) > 0.11:
#         IF thrust_required- thrust_provided > 0:
#             rpm = rpm+ 10
#         ELIF thrust_required- thrust_provided < 0:
#             rpm = rpm -10
#         END IF

#         IF rpm > 3100:
#             raise ValueError("RPM main motors going over maximum")
#         END IF
#         n = rpm/60
#         thrust_provided & power_provided interpolate_fit (XP5_speed, XP5_main, temperature)

#     Iterative_rpm for the side motors:
#     def iterative_rpm(rho_a, XP5_speed, XP5_delta_ side, T, thrust_required):
#         IF thrust_required < 2:
#             rpm = 1900
#         ELIF 2 < thrust_required < 4:
#             rpm = 2300
#         ELIF 4 < thrust_required < 6:
#             rpm =2700
#         ELIF 6 < thrust_required < 8:
#             rpm =3200
#         ELIF 8 < thrust_required < 10:
#             rpm =3700
#         ELIF 10 < thrust_required < 12:
#             rpm =4100
#         59
#         ELIF 12 < thrust_required < 14:
#             rpm = 4520
#         ELIF 14 < thrust_required < 16:
#             rpm = 4980
#         ELIF 16 < thrust_required < 18:
#             rpm = 5400
#         ELIF 18 < thrust_required < 20:
#             rpm = 5830
#         ELIF thrust_required > 20 :
#             rpm = 6250
#         END IF
#         WHILE absolute(thrust_required- thrust_provided) > 0.11:
#             st_provided & power_provided interpolate_fit (XP5_speed, XP5_side, temperature)
