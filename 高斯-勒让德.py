import numpy as np
from numpy import *
import time
def l_change(l_min,l_max,t):            #积分区域变换
    return (t+1)*(l_max-l_min)/2+l_min
n=[     # n=0
   { 'x1':0,'A1':2},
        # n=1
   {'x1':-0.5773502691896250,'x2':0.5773502691896250,'A1':1,'A2':1},
        # n=2
   {'x1':-0.7745966692414830,'x2':0,'x3':0.7745966692414830,'A1':0.5555555555555550,'A2':0.8888888888888880,'A3':0.5555555555555550},
        # n=3
   {'x1':-0.8611363115940520,'x2':-0.3399810435848560,'x3':0.3399810435848560 ,'x4':0.8611363115940520,
    'A1':0.3478548451374530,'A2':0.6521451548625460,'A3':0.6521451548625460,'A4':0.3478548451374530},
        # n=4
   {'x1':-0.9061798459386640,'x2':-0.5384693101056830,'x3':0,'x4':0.5384693101056830,'x5':0.9061798459386640,
    'A1':0.2369268850561890,'A2':0.4786286704993660,'A3':0.5688888888888880,'A4':0.4786286704993660,'A5':0.2369268850561890},
        # n=5
   {'x1':-0.9324695142031520,'x2':-0.6612093864662640,'x3':-0.2386191860831960 ,'x4':0.2386191860831960,'x5':0.6612093864662640,
    'x6':0.9324695142031520,
    'A1':0.1713244923791700,'A2':0.3607615730481380,'A3':0.4679139345726910,'A4':0.4679139345726910,'A5':0.3607615730481380,
    'A6':0.1713244923791700},
        # n=6
    {'x1':-0.9491079123427580,'x2':-0.7415311855993940,'x3':-0.4058451513773970,'x4':0.0000000000000000 ,'x5':0.4058451513773970,
     'x6':0.7415311855993940,'x7':0.9491079123427580,
    'A1':0.1294849661688690,'A2':0.2797053914892760,'A3':0.3818300505051180,'A4':0.4179591836734690,'A5':0.3818300505051180,
     'A6':0.2797053914892760,'A7':0.1294849661688690},
        # n=7
    {'x1':-0.9602898564975360,'x2':-0.7966664774136260,'x3':-0.5255324099163290,'x4':-0.1834346424956490,'x5':0.1834346424956490,
     'x6':0.5255324099163290,'x7':0.7966664774136260,'x8':0.9602898564975360,
    'A1':0.1012285362903760,'A2':0.2223810344533740,'A3':0.3137066458778870,'A4':0.3626837833783620,'A5':0.3626837833783620,
     'A6':0.3137066458778870,'A7':0.2223810344533740,'A8':0.1012285362903760},
        # n=8
    {'x1':-0.9681602395076260,'x2':-0.8360311073266350,'x3':-0.6133714327005900,'x4':-0.3242534234038080,'x5':0.0000000000000000,
     'x6':0.3242534234038080,'x7':0.6133714327005900,'x8':0.8360311073266350,'x9':0.9681602395076260,
    'A1':0.0812743883615744,'A2':0.1806481606948570 ,'A3':0.2606106964029350 ,'A4':0.3123470770400020,'A5':0.3302393550012590 ,
     'A6':0.3123470770400020,'A7':0.2606106964029350 ,'A8':0.1806481606948570,'A9':0.0812743883615744},
        # n=9
    {'x1':-0.9739065285171710,'x2':-0.8650633666889840,'x3':-0.6794095682990240,'x4':-0.4333953941292470,'x5':-0.1488743389816310,
     'x6':0.1488743389816310,'x7':0.4333953941292470,'x8':0.6794095682990240,'x9':0.8650633666889840,'x10':0.9739065285171710,
    'A1':0.0666713443086881 ,'A2':0.1494513491505800 ,'A3':0.2190863625159820 ,'A4':0.2692667193099960 ,'A5':0.2955242247147520 ,
     'A6':0.2955242247147520 ,'A7':0.2692667193099960 ,'A8':0.2190863625159820 ,'A9':0.1494513491505800 ,'A10':0.0666713443086881 },
        # n=10
    {'x1':-0.9782286581460570,'x2':-0.8870625997680950,'x3':-0.7301520055740490,'x4':-0.5190961292068110,'x5':-0.2695431559523440,
     'x6':0.0000000000000000,'x7':0.2695431559523440,'x8':0.5190961292068110,'x9':0.7301520055740490,'x10':0.8870625997680950,
     'x11':0.9782286581460570,
    'A1':0.0556685671161736 ,'A2':0.1255803694649040 ,'A3':0.1862902109277340 ,'A4':0.2331937645919900 ,'A5':0.2628045445102460 ,
     'A6':0.2729250867779000 ,'A7':0.2628045445102460 ,'A8':0.2331937645919900 ,'A9':0.1862902109277340 ,'A10':0.1255803694649040 ,
     'A11':0.0556685671161736 },
        # n=11
    {'x1':-0.9815606342467190 ,'x2':-0.9041172563704740,'x3':-0.7699026741943040,'x4':-0.5873179542866170 ,'x5':-0.3678314989981800,
     'x6':-0.1252334085114680,'x7':0.1252334085114680,'x8':0.3678314989981800,'x9':0.5873179542866170,'x10':0.7699026741943040,
     'x11':0.9041172563704740,'x12':0.9815606342467190,
    'A1':0.0471753363865118,'A2':0.1069393259953180,'A3':0.1600783285433460,'A4':0.2031674267230650,'A5':0.2334925365383540,
     'A6':0.2491470458134020,'A7':0.2491470458134020,'A8':0.2334925365383540,'A9':0.2031674267230650,'A10':0.1600783285433460,
     'A11':0.1069393259953180,'A12':0.0471753363865118},
        # n=12
    {'x1':-0.9841830547185880,'x2':-0.9175983992229770,'x3':-0.8015780907333090,'x4':-0.6423493394403400,'x5':-0.4484927510364460,
     'x6':-0.2304583159551340,'x7':0.0000000000000000,'x8':0.2304583159551340,'x9':0.4484927510364460,'x10':0.6423493394403400,
     'x11':0.8015780907333090,'x12':0.9175983992229770,'x13':0.9841830547185880,
    'A1':0.0404840047653158,'A2':0.0921214998377284,'A3':0.1388735102197870,'A4':0.1781459807619450,'A5':0.2078160475368880,
     'A6':0.2262831802628970,'A7':0.2325515532308730,'A8':0.2262831802628970,'A9':0.2078160475368880,'A10':0.1781459807619450,
     'A11':0.1388735102197870,'A12':0.0921214998377284,'A13':0.0404840047653158},
        # n=13
    {'x1':-0.9862838086968120,'x2':-0.9284348836635730,'x3':-0.8272013150697650,'x4':-0.6872929048116850,'x5':-0.5152486363581540 ,
     'x6':-0.3191123689278890 ,'x7':-0.1080549487073430,'x8':0.1080549487073430,'x9':0.3191123689278890,'x10':0.5152486363581540,
     'x11':0.6872929048116850,'x12':0.8272013150697650,'x13':0.9284348836635730,'x14':0.9862838086968120,
    'A1':0.0351194603317518,'A2':0.0801580871597602,'A3':0.1215185706879030,'A4':0.1572031671581930,'A5':0.1855383974779370,
     'A6':0.2051984637212950,'A7':0.2152638534631570,'A8':0.2152638534631570,'A9':0.2051984637212950,'A10':0.1855383974779370,
     'A11':0.1572031671581930,'A12':0.1215185706879030,'A13':0.0801580871597602,'A14':0.0351194603317518},
        # n=14
    {'x1':-0.9879925180204850,'x2':-0.9372733924007060,'x3':-0.8482065834104270,'x4':-0.7244177313601700,'x5':-0.5709721726085380,
     'x6':-0.3941513470775630 ,'x7':-0.2011940939974340,'x8':0.0000000000000000,'x9':0.2011940939974340,'x10':0.3941513470775630,
     'x11':0.5709721726085380,'x12':0.7244177313601700 ,'x13':0.8482065834104270,'x14':0.9372733924007060 ,'x15':0.9879925180204850,
    'A1':0.0307532419961172 ,'A2':0.0703660474881081 ,'A3':0.1071592204671710 ,'A4':0.1395706779261540,'A5':0.1662692058169930,
    'A6':0.1861610000155620 ,'A7':0.1984314853271110 ,'A8':0.2025782419255610,'A9':0.1984314853271110 ,'A10':0.1861610000155620 ,
    'A11':0.1662692058169930,'A12':0.1395706779261540,'A13':0.1071592204671710 ,'A14':0.0703660474881081 ,'A15':0.0307532419961172 },
        # n=15
    {'x1':-0.9894009349916490,'x2':-0.9445750230732320,'x3':-0.8656312023878310,'x4':-0.7554044083550030,'x5':-0.6178762444026430,
     'x6':-0.4580167776572270,'x7':-0.2816035507792580,'x8':-0.0950125098376374,'x9':0.0950125098376374,'x10':0.2816035507792580 ,
     'x11':0.4580167776572270 ,'x12':0.6178762444026430 ,'x13':0.7554044083550030 ,'x14':0.8656312023878310 ,'x15':0.9445750230732320 ,
     'x16':0.9894009349916490 ,
    'A1':0.0271524594117540 ,'A2':0.0622535239386478 ,'A3':0.0951585116824927 ,'A4':0.1246289712555330 ,'A5':0.1495959888165760 ,
     'A6':0.1691565193950020 ,'A7':0.1826034150449230 ,'A8':0.1894506104550680 ,'A9':0.1894506104550680 ,'A10':0.1826034150449230 ,
     'A11':0.1691565193950020 ,'A12':0.1495959888165760,'A13':0.1246289712555330 ,'A14':0.0951585116824927 ,'A15':0.0622535239386478 ,
     'A16':0.0271524594117540},
        # n=16
    {'x1':-0.9905754753144170 ,'x2':-0.9506755217687670,'x3':-0.8802391537269850,'x4':-0.7815140038968010,'x5':-0.6576711592166900,
     'x6':-0.5126905370864760,'x7':-0.3512317634538760,'x8':-0.1784841814958470,'x9':0.0000000000000000,'x10':0.1784841814958470,
     'x11':0.3512317634538760,'x12':0.5126905370864760,'x13':0.6576711592166900,'x14':0.7815140038968010,'x15':0.8802391537269850,
     'x16':0.9506755217687670,'x17':0.9905754753144170 ,
    'A1':0.0241483028685479 ,'A2':0.0554595293739872 ,'A3':0.0850361483171791 ,'A4':0.1118838471934030 ,'A5':0.1351363684685250 ,
     'A6':0.1540457610768100 ,'A7':0.1680041021564500 ,'A8':0.1765627053669920 ,'A9':0.1794464703562060 ,'A10':0.1765627053669920 ,
     'A11':0.1680041021564500 ,'A12':0.1540457610768100 ,'A13':0.1351363684685250 ,'A14':0.1118838471934030 ,'A15':0.0850361483171791 ,
     'A16':0.0554595293739872 ,'A17':0.0241483028685479 },
        # n=17
    {'x1':-0.9915651684209300,'x2':-0.9558239495713970,'x3':-0.8926024664975550,'x4':-0.8037049589725230,'x5':-0.6916870430603530,
     'x6':-0.5597708310739470,'x7':-0.4117511614628420,'x8':-0.2518862256915050,'x9':-0.0847750130417353,'x10':0.0847750130417353 ,
     'x11':0.2518862256915050 ,'x12':0.4117511614628420,'x13':0.5597708310739470 ,'x14':0.6916870430603530 ,'x15':0.8037049589725230 ,
     'x16':0.8926024664975550 ,'x17':0.9558239495713970,'x18':0.9915651684209300 ,
    'A1':0.0216160135264833 ,'A2':0.0497145488949698 ,'A3':0.0764257302548890 ,'A4':0.1009420441062870 ,'A5':0.1225552067114780 ,
     'A6':0.1406429146706500 ,'A7':0.1546846751262650 ,'A8':0.1642764837458320 ,'A9':0.1691423829631430 ,'A10':0.1691423829631430 ,
     'A11':0.1642764837458320 ,'A12':0.1546846751262650 ,'A13':0.1406429146706500 ,'A14':0.1225552067114780 ,'A15':0.1009420441062870 ,
     'A16':0.0764257302548890 ,'A17':0.0497145488949698 ,'A18':0.0216160135264833 },
        # n=18
    {'x1':-0.9924068438435840,'x2':-0.9602081521348300,'x3':-0.9031559036148170,'x4':-0.8227146565371420,'x5':-0.7209661773352290 ,
     'x6':-0.6005453046616810 ,'x7':-0.4645707413759600,'x8':-0.3165640999636290,'x9':-0.1603586456402250,'x10':0.0000000000000000 ,
     'x11':0.1603586456402250 ,'x12':0.3165640999636290 ,'x13':0.4645707413759600 ,'x14':0.6005453046616810 ,'x15':0.7209661773352290 ,
     'x16':0.8227146565371420 ,'x17':0.9031559036148170 ,'x18':0.9602081521348300 ,'x19':0.9924068438435840 ,
    'A1':0.0194617882297264 ,'A2':0.0448142267656996 ,'A3':0.0690445427376412 ,'A4':0.0914900216224500 ,'A5':0.1115666455473330 ,
     'A6':0.1287539625393360 ,'A7':0.1426067021736060 ,'A8':0.1527660420658590 ,'A9':0.1589688433939540 ,'A10':0.1610544498487830 ,
     'A11':0.1589688433939540 ,'A12':0.1527660420658590 ,'A13':0.1426067021736060 ,'A14':0.1287539625393360 ,'A15':0.1115666455473330 ,
     'A16':0.0914900216224500 ,'A17':0.0690445427376412 ,'A18':0.0448142267656996 ,'A19':0.0194617882297264},
        # n=19
    {'x1':-0.9931285991850940,'x2':-0.9639719272779130,'x3':-0.9122344282513260,'x4':-0.8391169718222180,'x5':-0.7463319064601500,
     'x6':-0.6360536807265150,'x7':-0.5108670019508270,'x8':-0.3737060887154190,'x9':-0.2277858511416450 ,'x10':-0.0765265211334973,
     'x11':0.0765265211334973 ,'x12':0.2277858511416450 ,'x13':0.3737060887154190 ,'x14':0.5108670019508270,'x15':0.6360536807265150 ,
     'x16':0.7463319064601500 ,'x17':0.8391169718222180,'x18':0.9122344282513260 ,'x19':0.9639719272779130,'x20':0.9931285991850940 ,
    'A1':0.0176140071391521 ,'A2':0.0406014298003869 ,'A3':0.0626720483341090 ,'A4':0.0832767415767047 ,'A5':0.1019301198172400 ,
     'A6':0.1181945319615180 ,'A7':0.1316886384491760 ,'A8':0.1420961093183820 ,'A9':0.1491729864726030 ,'A10':0.1527533871307250 ,
     'A11':0.1527533871307250 ,'A12':0.1491729864726030 ,'A13':0.1420961093183820 ,'A14':0.1316886384491760 ,'A15':0.1181945319615180 ,
     'A16':0.1019301198172400 ,'A17':0.0832767415767047 ,'A18':0.0626720483341090 ,'A19':0.0406014298003869 ,'A20':0.0176140071391521 }
   ]     #积分
num = eval(input('请输入n：'))    #积分精度
l_max = eval(input('请输入积分上限：'))    #积分上限
l_min= eval(input('请输入积分下限：'))    #积分下限
str_hs = input('请输入被积分函数（必须包含x）：')         #被积函数
temp = 0                                 #积分结果
start = time.perf_counter()              #获取积分开始时间
for i in range(num+1):                   #循环遍历
    t = n[num].get('x'+str(i+1))
    x = l_change(l_min,l_max,t)          #积分区域变换
    temp = n[num].get('A' + str(i + 1))*eval(str_hs)*(l_max-l_min)/2+temp
print("积分结果为：",temp)
end = time.perf_counter()
print("计算时间为：",end-start)            #输出运算时间
