# coding: latin1

#Copyright (c) <2013>, <Kari Aliranta, Jaakko Leppäkangas, Janne Pesonen and Atte Rautio>
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met: 
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer. 
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution. 
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those
#of the authors and should not be interpreted as representing official policies, 
#either expressed or implied, of the FreeBSD Project.

"""
Created on Apr 24, 2013

@author: Jaakko Leppakangas
"""
"""
Helper module for all the different channel groups.
"""

class BrainRegions(object):
    """
    This class contains channel groups which are created according to
    mne_browse_raw channel groups. The channel name can be reconstructed by
    using the prefix 'MEG ' with each channel number. The last number indicates
    the type of the meter. Magnetometers end with number one, whereas
    gradiometers end with number two and three.
    """
    vertex = ['0633','0632','0423','0422','0712','0713','0433','0432',
              '0742','0743','1822','1823','1043','1042','1112','1113',
              '0722','0723','1142','1143','0732','0733','2212','2213',
              '0631','0421','0711','0431','0741','1821','1041','1111',
              '0721','1141','0731','2211']
    
    left_temporal = ['0223','0222','0212','0213','0133','0132','0112','0113',
                     '0233','0232','0243','0242','1512','1513','0143','0142',
                     '1623','1622','1613','1612','1523','1522','1543','1542',
                     '1533','1532','0221','0211','0131','0111','0231','0241',
                     '1511','0141','1621','1611','1521','1541','1531']
    
    right_temporal= ['1312','1313','1323','1322','1442','1443','1423','1422',
                     '1342','1343','1333','1332','2612','2613','1433','1432',
                     '2413','2412','2422','2423','2642','2643','2623','2622',
                     '2633','2632','1311','1321','1441','1421','1341','1331',
                     '2611','1431','2411','2421','2641','2621','2631']
    
    left_parietal = ['0633','0632','0423','0422','0412','0413','0712','0713',
                     '0433','0432','0442','0443','0742','0743','1822','1823',
                     '1813','1812','1832','1833','1843','1842','1632','1633',
                     '2013','2012','0631','0421','0411','0711','0431','0441',
                     '0741','1821','1811','1831','1841','1631','2011']
    
    right_parietal= ['1043','1042','1112','1113','1123','1122','0722','0723',
                     '1142','1143','1133','1132','0732','0733','2212','2213',
                     '2223','2222','2242','2243','2232','2233','2442','2443',
                     '2023','2022','1041','1111','1121','0721','1141','1131',
                     '0731','2211','2221','2241','2231','2441','2021']
    
    left_occipital= ['2042','2043','1913','1912','2113','2112','1922','1923',
                     '1942','1943','1642','1643','1933','1932','1733','1732',
                     '1723','1722','2143','2142','1742','1743','1712','1713',
                     '2041','1911','2111','1921','1941','1641','1931','1731',
                     '1721','2141','1741','1711']
    
    right_occipital=['2032','2033','2312','2313','2342','2343','2322','2323',
                     '2432','2433','2122','2123','2332','2333','2512','2513',
                     '2522','2523','2132','2133','2542','2543','2532','2533',
                     '2031','2311','2341','2321','2431','2121','2331','2511',
                     '2521','2131','2541','2531']
    
    left_frontal = ['0522','0523','0512','0513','0312','0313','0342','0343',
                    '0122','0123','0822','0823','0532','0533','0542','0543',
                    '0322','0323','0612','0613','0332','0333','0622','0623',
                    '0642','0643','0521','0511','0311','0341','0121','0821',
                    '0531','0541','0321','0611','0331','0621','0641']
    
    right_frontal = ['0812','0813','0912','0913','0922','0923','1212','1213',
                     '1222','1223','1412','1413','0942','0943','0932','0933',
                     '1232','1233','1012','1013','1022','1023','1242','1243',
                     '1032','1033','0811','0911','0921','1211','1221','1411',
                     '0941','0931','1231','1011','1021','1241','1031']
