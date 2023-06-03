# import re
#
# inp = "<TradingApplication><Name>trading_app_spy_1</Name><LogPath>/mnt/logs</LogPath><TradingStrategies><TradingStrategy enabled='true'><Symbols><Symbol>SPY</Symbol></Symbols><Multiplier>5000</Multiplier></TradingStrategy></TradingStrategies></TradingApplication>"
#
result = {
    'name': None,  #re.findall(r'Name', inp),
    'strategies': [],
}
# for element in re.findall(r'<TradingStrategies>', inp):
#     print(element)
    ##result['strategies'].append({'enabled': element.attrib['enabled'],})

import xml.etree.ElementTree as ET
tree = ET.parse('input001.txt')
root = tree.getroot()
name_cnt = 0
strategies_cnt = 0
strategies = None
values = [elem for elem in list(root)]
print(values)
for elem in list(root):
    if elem.tag == "name":
        name_cnt += 1
        if name_cnt > 1:
            print("ERROR")
    elif elem.tag == "TradingStrategies":
        strategies_cnt += 1
        strategies = elem
        if strategies_cnt > 1:
            print("ERROR")


if len(root.findall('Name')) != 1:
    raise IndexError()
if len(root.findall('TradingStrategies')) == 0:
    raise IndexError()

name = root.findall('Name')[0].text
trading_strategies = root.findall('TradingStrategies')[0].findall('TradingStrategy')
result['name'] = str(name)

for trading_strategy in trading_strategies:
    isEnabled = trading_strategy.attrib['enabled']
    if not isEnabled or isEnabled not in "TrueFalse":
        raise IndexError()
    isEnabled = bool(isEnabled)
    symbol_list = trading_strategy.findall('Symbols')[0].findall('Symbol')
    multipliers = trading_strategy.findall('Multiplier')
    if len(multipliers) > 1:
        raise IndexError()
    multiplier = int(multipliers[0].text) if len(multipliers) > 0 else 100
    if int((multiplier//10)*10) != float(multiplier):
        raise IndexError()

    curSymbols = [s.text for s in symbol_list]
    result['strategies'].append({
    'enabled': isEnabled,
    'symbols': curSymbols,
    'multiplier': multiplier
    })
print(result)

# for s in strategies:

























# inp = "date, process, host, log, bytes"
# csv_input = "date,process,host,log,bytes\n20140206,cme_trader_2,cme0001,0345-cme_trader_2.log.gz,15400000\n20140206,phlx_trader_1,phlx0001,0651-phlx_trader_1.log.gz,14100000\n20140206,phlx_trader_2,phlx0001,0645-phlx_trader_2.log.gz,13800000\n20140207,cme_trader_2,cme0001,0345-cme_trader_2.log.gz,15800000\n20140207,cme_trader_3,cme0001,0345-cme_trader_3.log.gz,14200000\n20140207,phlx_trader_1,phlx0001,0651-phlx_trader_1.log.gz,24100000"
#
# h = {}
# csv_input = csv_input.split('\n')
# lastDate = None
# # for inp1 in csv_input[1:]:
# #     inp1 = inp1.split(',')
# #     date = inp1[0]
# #     trader = inp1[1].split('_')[0]
# #     bytes = inp1[4]
# #     h[date] = h.get(date, {})
# #     h[date][trader] = h[date].get(trader, 0) + int(bytes)
# #
# # for date in h.keys():
# #     for trader in h[date].keys():
# #         print(f"{date},{trader},{h[date][trader]}")
#
# h, lastDate, finalDate = {}, None, None
# lastSwitchVal = 0
# for inp1 in csv_input[1:]:
#     inp1 = inp1.split(',')
#     date = inp1[0]
#     trader = inp1[1].split('_')[0]
#     otherVal = inp1[4]
#     h[trader] = h.get(trader, 0) + int(otherVal)
#     if lastDate == None:
#         lastDate = date
#     elif lastDate != date:
#         for curTrader in h.keys():
#             if curTrader == trader:
#                 print(f"{lastDate},{curTrader},{h[curTrader]-int(otherVal)}")
#             else:
#                 print(f"{lastDate},{curTrader},{h[curTrader]}")
#         lastDate = date
#         h = {trader: int(otherVal)}
#     finalDate = date
#
# for trader in h.keys():
#     print(f"{finalDate},{trader},{h[trader]}")
#
# titles = csv_input[0]
# print(f"{titles[0]}, {titles[1]}, {titles[4 ]}")
#===========================================================
