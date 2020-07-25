# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:49:36 2020

@author: parkerj12
"""
import re
import requests
import yfinance
import talib
from talib.abstract import *
import dash
import dash_core_components as dcc
import dash_html_components as html
class TAdata():
    def __init__(self):
        self.symbols = []
        self.token = 'sk_2ddaab04d2914887bf39d40b7b6d0556'
        self.getSymbols()
        self.indicatordata = {}
        self.funcs = talib.get_functions()
        self.symboldata = {}
        print(talib.get_functions())
        self.function_map = {
                'HT_DCPERIOD':HT_DCPERIOD,
        'HT_DCPHASE':HT_DCPHASE,
        'HT_PHASOR':HT_PHASOR,
        'HT_SINE':HT_SINE,
        'HT_TRENDMODE':HT_TRENDMODE,
        'ADD':ADD,
        'DIV':DIV,
        'MAX':MAX,
        'MAXINDEX':MAXINDEX,
        'MIN':MIN,
        'MININDEX':MININDEX,
        'MINMAX':MINMAX,
        'MINMAXINDEX':MINMAXINDEX,
        'MULT':MULT,
        'SUB':SUB,
        'SUM':SUM,
        'ACOS':ACOS,
        'ASIN':ASIN,
        'ATAN':ATAN,
        'CEIL':CEIL,
        'COS':COS,
        'COSH':COSH,
        'EXP':EXP,
        'FLOOR':FLOOR,
        'LN':LN,
        'LOG10':LOG10,
        'SIN':SIN,
        'SINH':SINH,
        'SQRT':SQRT,
        'TAN':TAN,
        'TANH':TANH,
        'ADX':ADX,
        'ADXR':ADXR,
        'APO':APO,
        'AROON':AROON,
        'AROONOSC':AROONOSC,
        'BOP':BOP,
        'CCI':CCI,
        'CMO':CMO,
        'DX':DX,
        'MACD':MACD,
        'MACDEXT':MACDEXT,
        'MACDFIX':MACDFIX,
        'MFI':MFI,
        'MINUS_DI':MINUS_DI,
        'MINUS_DM':MINUS_DM,
        'MOM':MOM,
        'PLUS_DI':PLUS_DI,
        'PLUS_DM':PLUS_DM,
        'PPO':PPO,
        'ROC':ROC,
        'ROCP':ROCP,
        'ROCR':ROCR,
        'ROCR100':ROCR100,
        'RSI':RSI,
        'STOCH':STOCH,
        'STOCHF':STOCHF,
        'STOCHRSI':STOCHRSI,
        'TRIX':TRIX,
        'ULTOSC':ULTOSC,
        'WILLR':WILLR,
        'BBANDS':BBANDS,
        'DEMA':DEMA,
        'EMA':EMA,
        'HT_TRENDLINE':HT_TRENDLINE,
        'KAMA':KAMA,
        'MA':MA,
        'MAMA':MAMA,
        'MAVP':MAVP,
        'MIDPOINT':MIDPOINT,
        'MIDPRICE':MIDPRICE,
        'SAR':SAR,
        'SAREXT':SAREXT,
        'SMA':SMA,
        'T3':T3,
        'TEMA':TEMA,
        'TRIMA':TRIMA,
        'WMA':WMA,
        'CDL2CROWS':CDL2CROWS,
        'CDL3BLACKCROWS':CDL3BLACKCROWS,
        'CDL3INSIDE':CDL3INSIDE,
        'CDL3LINESTRIKE':CDL3LINESTRIKE,
        'CDL3OUTSIDE':CDL3OUTSIDE,
        'CDL3STARSINSOUTH':CDL3STARSINSOUTH,
        'CDL3WHITESOLDIERS':CDL3WHITESOLDIERS,
        'CDLABANDONEDBABY':CDLABANDONEDBABY,
        'CDLADVANCEBLOCK':CDLADVANCEBLOCK,
        'CDLBELTHOLD':CDLBELTHOLD,
        'CDLBREAKAWAY':CDLBREAKAWAY,
        'CDLCLOSINGMARUBOZU':CDLCLOSINGMARUBOZU,
        'CDLCONCEALBABYSWALL':CDLCONCEALBABYSWALL,
        'CDLCOUNTERATTACK':CDLCOUNTERATTACK,
        'CDLDARKCLOUDCOVER':CDLDARKCLOUDCOVER,
        'CDLDOJI':CDLDOJI,
        'CDLDOJISTAR':CDLDOJISTAR,
        'CDLDRAGONFLYDOJI':CDLDRAGONFLYDOJI,
        'CDLENGULFING':CDLENGULFING,
        'CDLEVENINGDOJISTAR':CDLEVENINGDOJISTAR,
        'CDLEVENINGSTAR':CDLEVENINGSTAR,
        'CDLGAPSIDESIDEWHITE':CDLGAPSIDESIDEWHITE,
        'CDLGRAVESTONEDOJI':CDLGRAVESTONEDOJI,
        'CDLHAMMER':CDLHAMMER,
        'CDLHANGINGMAN':CDLHANGINGMAN,
        'CDLHARAMI':CDLHARAMI,
        'CDLHARAMICROSS':CDLHARAMICROSS,
        'CDLHIGHWAVE':CDLHIGHWAVE,
        'CDLHIKKAKE':CDLHIKKAKE,
        'CDLHIKKAKEMOD':CDLHIKKAKEMOD,
        'CDLHOMINGPIGEON':CDLHOMINGPIGEON,
        'CDLIDENTICAL3CROWS':CDLIDENTICAL3CROWS,
        'CDLINNECK':CDLINNECK,
        'CDLINVERTEDHAMMER':CDLINVERTEDHAMMER,
        'CDLKICKING':CDLKICKING,
        'CDLKICKINGBYLENGTH':CDLKICKINGBYLENGTH,
        'CDLLADDERBOTTOM':CDLLADDERBOTTOM,
        'CDLLONGLEGGEDDOJI':CDLLONGLEGGEDDOJI,
        'CDLLONGLINE':CDLLONGLINE,
        'CDLMARUBOZU':CDLMARUBOZU,
        'CDLMATCHINGLOW':CDLMATCHINGLOW,
        'CDLMATHOLD':CDLMATHOLD,
        'CDLMORNINGDOJISTAR':CDLMORNINGDOJISTAR,
        'CDLMORNINGSTAR':CDLMORNINGSTAR,
        'CDLONNECK':CDLONNECK,
        'CDLPIERCING':CDLPIERCING,
        'CDLRICKSHAWMAN':CDLRICKSHAWMAN,
        'CDLRISEFALL3METHODS':CDLRISEFALL3METHODS,
        'CDLSEPARATINGLINES':CDLSEPARATINGLINES,
        'CDLSHOOTINGSTAR':CDLSHOOTINGSTAR,
        'CDLSHORTLINE':CDLSHORTLINE,
        'CDLSPINNINGTOP':CDLSPINNINGTOP,
        'CDLSTALLEDPATTERN':CDLSTALLEDPATTERN,
        'CDLSTICKSANDWICH':CDLSTICKSANDWICH,
        'CDLTAKURI':CDLTAKURI,
        'CDLTASUKIGAP':CDLTASUKIGAP,
        'CDLTHRUSTING':CDLTHRUSTING,
        'CDLTRISTAR':CDLTRISTAR,
        'CDLUNIQUE3RIVER':CDLUNIQUE3RIVER,
        'CDLUPSIDEGAP2CROWS':CDLUPSIDEGAP2CROWS,
        'CDLXSIDEGAP3METHODS':CDLXSIDEGAP3METHODS,
        'AVGPRICE':AVGPRICE,
        'MEDPRICE':MEDPRICE,
        'TYPPRICE':TYPPRICE,
        'WCLPRICE':WCLPRICE,
        'BETA':BETA,
        'CORREL':CORREL,
        'LINEARREG':LINEARREG,
        'LINEARREG_ANGLE':LINEARREG_ANGLE,
        'LINEARREG_INTERCEPT':LINEARREG_INTERCEPT,
        'LINEARREG_SLOPE':LINEARREG_SLOPE,
        'STDDEV':STDDEV,
        'TSF':TSF,
        'VAR':VAR,
        'ATR':ATR,
        'NATR':NATR,
        'TRANGE':TRANGE,
        'AD':AD,
        'ADOSC':ADOSC,
        'OBV':OBV,
        
                }
        self.retrieveTAData()
        self.checkTriggers()
    def retrieveTAData(self):
        x=0
        for s in self.symbols:
            x=x+1
            print(x)
            tickerData = yfinance.Ticker(s)
            tickerDf = tickerData.history(period = "max")
            tickerDf = tickerDf.rename(columns={"Open": "open", "High": "high", "Close": "close","Low" : "low","Volume" : "volume"})
            
            for f in self.funcs:
                if(f.count('CDL')==0):
                    continue
                try:
                    self.indicatordata[f] = self.function_map[f](tickerDf)
                except:
                    continue
            self.symboldata[s] = self.indicatordata
            if(x==20):
                break
    def getSymbols(self):
        url = "https://cloud.iexapis.com/stable/ref-data/iex/symbols?token="+self.token
        r = requests.get(url)
        data = r.text
        tempSymbols = re.findall('"symbol":".\w+',data)
        for s in tempSymbols:
            symbol = s.replace('"symbol":"',"")
            if(len(symbol)<5 and self.symbols.count(symbol)==0):    
                self.symbols.append(symbol)

        print(len(self.symbols))
    def displaydata(self):
        data = pd.DataFrame.from_dict(self.symboldata['AA']['CDL2CROWS'])
        data.plot()
    def checkTriggers(self):
        for s in self.symboldata:
            for pattern in self.symboldata[s]:
                for date in pattern:
                    if not (date == 0):
                        print(s+' Triggered on '+date+' For Pattern '+pattern)
TaData = TAdata()