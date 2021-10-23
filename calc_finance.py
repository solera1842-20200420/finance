# 会計関連の計算式

# library
import os
import numpy as np
import numpy_financial as npf
import pandas as pa
import matplotlib.pyplot as plt
import seaborn as sns

#複利計算 1年間運用して4%の複利を得て、追加で100万円の元本を積立した場合

principal = 100  # 元本
compound_interest = 0.04  # 複利

# tsumitate = 100
accumulation = 100  #  積立
# total = ganpon*(1+fukuri)+tsumitate
total = principal*(1+compound_interest)
print(str(total))

# 現在価値から将来価値を計算
"""
将来価値の計算
numpy.fv(rate, nper, pmt, pv, when='end')
rate: 利率
nper: 複利計算期間値(支払い回数)
pmt: 毎回の支払い額
pv: 現在価値
when: 支払い期日(endなら期末、startなら期首)
現在価値は、例えば返済なら「借入金額」、貯蓄の場合は「積立済金額」が相当
・年利1%（5年間）
・毎月2万円支払い
・現在価値2万円
の場合の将来価値。
"""

fv = npf.pv(0.01/12, 5*12, -20000, -20000)
print("将来価値:", fv)

# 将来価値から現在価値の計算
"""
現在価値の計算
numpy.fv(rate, nper, pmt, fv, when='end')
"""
pv = npf.fv(0.01/12, 5*12, -20000, 2000000)
print("将来価値から現在価値の計算:", pv)
