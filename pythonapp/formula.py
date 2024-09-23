# formula = '
# =IF(
#   Predpostavke!C$21 = "Gvaop",
#   IFERROR(
#     INDEX(
#       BS_Gvin!D:D,
#       MATCH(
#         Izkazi!$O6,
#         BS_Gvin!$A:$A,
#         0
#       )
#     ) / 1000,
#     0
#   ) +
#   IFERROR(
#     INDEX(
#       BS_Gvin!D:D,
#       MATCH(
#         Izkazi!$P6,
#         BS_Gvin!$A:$A,
#         0
#       )
#     ) / 1000,
#     0
#   ) +
#   IFERROR(
#     INDEX(
#       BS_Gvin!D:D,
#       MATCH(
#         Izkazi!$Q6,
#         BS_Gvin!$A:$A,
#         0
#       )
#     ) / 1000,
#     0
#   ) +
#   IFERROR(
#     INDEX(
#       BS_Gvin!D:D,
#       MATCH(
#         Izkazi!$R6,
#         BS_Gvin!$A:$A,
#         0
#       )
#     ) / 1000,
#     0
#   ),
#   IFERROR(
#     INDEX(
#       BS_Ajpes!E$17:E$113,
#       MATCH(
#         Izkazi!$S6,
#         BS_Ajpes!$C$17:$C$113,
#         0
#       )
#     ) / 1000,
#     0
#   ) +
#   IFERROR(
#     INDEX(
#       BS_Ajpes!E$17:E$113,
#       MATCH(
#         Izkazi!$T6,
#         BS_Ajpes!$C$17:$C$113,
#         0
#       )
#     ) / 1000,
#     0
#   ) +
#   IFERROR(
#     INDEX(
#       BS_Ajpes!E$17:E$113,
#       MATCH(
#         Izkazi!$U6,
#         BS_Ajpes!$C$17:$C$113,
#         0
#       )
#     ) / 1000,
#     0
#   ) +
#   IFERROR(
#     INDEX(
#       BS_Ajpes!E$17:E$113,
#       MATCH(
#         Izkazi!$V6,
#         BS_Ajpes!$C$17:$C$113,
#         0
#       )
#     ) / 1000,
#     0
#   )
# )


# '