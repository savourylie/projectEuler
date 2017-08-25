# Value Iteration in Caveman's World Test Code

# def caveman_iteration_v1(h, g, f, d):
#     vh = h
#     vg = g
#     vf = f
#     vd = d
#
#     gamma = 0.9
#
#     print(0, vh, vg, vf, vd)
#
#     for k in range(100):
#         vh = h + gamma * (0.5 * vh + 0.4 * vg + 0.1 * vd)
#         vg = g + gamma * (0.2 * vh + 0.1 * vg + 0.6 * vf + 0.1 * vd)
#         vf = f + gamma * (0.9 * vh + 0.1 * vd)
#         vd = d + gamma * vd
#         print(k + 1, vh, vg, vf, vd)
#
# def caveman_iteration_v2(rh, rg, rf, rd):
#     vh = rh
#     vg = rg
#     vf = rf
#     vd = rd
#
#     gamma = 0.9
#
#     print(0, vh, vg, vf, vd)
#
#     for k in range(100):
#         vh = rh + gamma * (0.9 * vg + 0.1 * vd)
#         vg = rg + gamma * (0.8 * vf + 0.2 * vh)
#         vf = rf + gamma * vh
#         vd = rd + gamma * vd
#         print(k + 1, vh, vg, vf, vd)
#
# caveman_iteration_v2(0, 1, 10, -10)