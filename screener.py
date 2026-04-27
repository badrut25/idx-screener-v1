# @title OOP Complete Suite: 4 Screeners (ML Lorentzian + Kernel Red-to-Green) + Telegram + WIB
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta, timezone
from tabulate import tabulate
import json
import os
import glob
import time
import requests

# ==============================================================================
# 1. CONFIGURATION
# ==============================================================================
class Config:
    TICKERS = [
        "AALI", "ABBA", "ABDA", "ABMM", "ACES", "ACST", "ADES", "ADHI", "ADMF", "ADMG", "ADRO", "AGII", "AGRO", "AGRS",
        "AHAP", "AIMS", "AISA", "AKKU", "AKPI", "AKRA", "AKSI", "ALDO", "ALKA", "ALMI", "ALTO", "AMAG", "AMFG", "AMIN",
        "AMRT", "ANJT", "ANTM", "APEX", "APIC", "APII", "APLI", "APLN", "ARGO", "ARII", "ARNA", "ARTA", "ARTI", "ARTO",
        "ASBI", "ASDM", "ASGR", "ASII", "ASJT", "ASMI", "ASRI", "ASRM", "ASSA", "ATIC", "AUTO", "BABP", "BACA", "BAJA",
        "BALI", "BAPA", "BATA", "BAYU", "BBCA", "BBHI", "BBKP", "BBLD", "BBMD", "BBNI", "BBRI", "BBRM", "BBTN", "BBYB",
        "BCAP", "BCIC", "BCIP", "BDMN", "BEKS", "BEST", "BFIN", "BGTG", "BHIT", "BIKA", "BIMA", "BINA", "BIPI", "BIPP",
        "BIRD", "BISI", "BJBR", "BJTM", "BKDP", "BKSL", "BKSW", "BLTA", "BLTZ", "BMAS", "BMRI", "BMSR", "BMTR", "BNBA",
        "BNBR", "BNGA", "BNII", "BNLI", "BOLT", "BPFI", "BPII", "BRAM", "BRMS", "BRNA", "BRPT", "BSDE", "BSIM", "BSSR",
        "BSWD", "BTEK", "BTEL", "BTON", "BTPN", "BUDI", "BUKK", "BULL", "BUMI", "BUVA", "BVIC", "BWPT", "BYAN", "CANI",
        "CASS", "CEKA", "CENT", "CFIN", "CINT", "CITA", "CLPI", "CMNP", "CMPP", "CNKO", "CNTX", "COWL", "CPIN", "CPRO",
        "CSAP", "CTBN", "CTRA", "CTTH", "DART", "DEFI", "DEWA", "DGIK", "DILD", "DKFT", "DLTA", "DMAS", "DNAR", "DNET",
        "DOID", "DPNS", "DSFI", "DSNG", "DSSA", "DUTI", "DVLA", "DYAN", "ECII", "EKAD", "ELSA", "ELTY", "EMDE", "EMTK",
        "ENRG", "EPMT", "ERAA", "ERTX", "ESSA", "ESTI", "ETWA", "EXCL", "FAST", "FASW", "FISH", "FMII", "FORU", "FPNI",
        "GAMA", "GDST", "GDYR", "GEMA", "GEMS", "GGRM", "GIAA", "GJTL", "GLOB", "GMTD", "GOLD", "GOLL", "GPRA", "GSMF",
        "GTBO", "GWSA", "GZCO", "HADE", "HDFA", "HDTX", "HERO", "HEXA", "HITS", "HMSP", "HOME", "HOTL", "HRUM", "IATA",
        "IBFN", "IBST", "ICBP", "ICON", "IGAR", "IIKP", "IKAI", "IKBI", "IMAS", "IMJS", "IMPC", "INAF", "INAI", "INCI",
        "INCO", "INDF", "INDR", "INDS", "INDX", "INDY", "INKP", "INPC", "INPP", "INRU", "INTA", "INTD", "INTP", "IPOL",
        "ISAT", "ISSP", "ITMA", "ITMG", "JAWA", "JECC", "JIHD", "JKON", "JKSW", "JPFA", "JRPT", "JSMR", "JSPT", "JTPE",
        "KAEF", "KARW", "KBLI", "KBLM", "KBLV", "KBRI", "KDSI", "KIAS", "KICI", "KIJA", "KKGI", "KLBF", "KOBX", "KOIN",
        "KONI", "KOPI", "KPIG", "KRAH", "KRAS", "KREN", "LAPD", "LCGP", "LEAD", "LINK", "LION", "LMAS", "LMPI", "LMSH",
        "LPCK", "LPGI", "LPIN", "LPKR", "LPLI", "LPPF", "LPPS", "LRNA", "LSIP", "LTLS", "MAGP", "MAIN", "MAMI", "MAPI",
        "MAYA", "MBAP", "MBSS", "MBTO", "MCOR", "MDIA", "MDKA", "MDLN", "MDRN", "MEDC", "MEGA", "MERK", "META",
        "MFMI", "MGNA", "MICE", "MIDI", "MIKA", "MIRA", "MITI", "MKPI", "MLBI", "MLIA", "MLPL", "MLPT", "MMLP",
        "MNCN", "MPMX", "MPPA", "MRAT", "MREI", "MSKY", "MTDL", "MTFN", "MTLA", "MTSM", "MYOH", "MYOR", "MYRX", "MYTX",
        "NELY", "NIKL", "NIPS", "NIRO", "NISP", "NOBU", "NRCA", "OCAP", "OKAS", "OMRE", "PADI", "PALM", "PANR", "PANS",
        "PBRX", "PDES", "PEGE", "PGAS", "PGLI", "PICO", "PJAA", "PKPK", "PLAS", "PLIN", "PNBN", "PNBS", "PNIN", "PNLF",
        "PNSE", "POLY", "POOL", "PPRO", "PRAS", "PSAB", "PSDN", "PSKT", "PTBA", "PTIS", "PTPP", "PTRO", "PTSN", "PTSP",
        "PUDP", "PWON", "PYFA", "RAJA", "RALS", "RANC", "RBMS", "RDTX", "RELI", "RICY", "RIGS", "RIMO", "RODA", "ROTI",
        "RUIS", "SAFE", "SAME", "SCCO", "SCMA", "SCPI", "SDMU", "SDPC", "SDRA", "SGRO", "SHID", "SIDO", "SILO", "SIMA",
        "SIMP", "SIPD", "SKBM", "SKLT", "SKYB", "SMAR", "SMBR", "SMCB", "SMDM", "SMDR", "SMGR", "SMMA", "SMMT", "SMRA",
        "SMRU", "SMSM", "SOCI", "SONA", "SPMA", "SQMI", "SRAJ", "SRIL", "SRSN", "SRTG", "SSIA", "SSMS", "SSTM", "STAR",
        "STTP", "SUGI", "SULI", "SUPR", "TALF", "TARA", "TAXI", "TBIG", "TBLA", "TBMS", "TCID", "TELE", "TFCO", "TGKA",
        "TIFA", "TINS", "TIRA", "TIRT", "TKIM", "TLKM", "TMAS", "TMPO", "TOBA", "TOTL", "TOTO", "TOWR", "TPIA", "TPMA",
        "TRAM", "TRIL", "TRIM", "TRIO", "TRIS", "TRST", "TRUS", "TSPC", "ULTJ", "UNIC", "UNIT", "UNSP", "UNTR", "UNVR",
        "VICO", "VINS", "VIVA", "VOKS", "VRNA", "WAPO", "WEHA", "WICO", "WIIM", "WIKA", "WINS", "WOMF", "WSKT", "WTON",
        "YPAS", "YULE", "ZBRA", "SHIP", "CASA", "DAYA", "DPUM", "IDPR", "JGLE", "KINO", "MARI", "MKNT", "MTRA", "OASA",
        "POWR", "INCF", "WSBP", "PBSA", "PRDA", "BOGA", "BRIS", "PORT", "CARS", "MINA", "FORZ", "CLEO", "TAMU", "CSIS",
        "TGRA", "FIRE", "TOPS", "KMTR", "ARMY", "MAPB", "WOOD", "HRTA", "MABA", "HOKI", "MPOW", "MARK", "NASA", "MDKI",
        "BELL", "KIOS", "GMFI", "MTWI", "ZINC", "MCAS", "PPRE", "WEGE", "PSSI", "MORA", "DWGL", "PBID", "JMAS", "CAMP",
        "IPCM", "PCAR", "LCKM", "BOSS", "HELI", "JSKY", "INPS", "GHON", "TDPM", "DFAM", "NICK", "BTPS", "SPTO", "PRIM",
        "HEAL", "TRUK", "PZZA", "TUGU", "MSIN", "SWAT", "KPAL", "TNCA", "MAPA", "TCPI", "IPCC", "RISE", "BPTR", "POLL",
        "NFCX", "MGRO", "NUSA", "FILM", "ANDI", "LAND", "MOLI", "PANI", "DIGI", "CITY", "SAPX", "KPAS", "SURE", "HKMU",
        "MPRO", "DUCK", "GOOD", "SKRN", "YELO", "CAKK", "SATU", "SOSS", "DEAL", "POLA", "DIVA", "LUCK", "URBN", "SOTS",
        "ZONE", "PEHA", "FOOD", "BEEF", "POLI", "CLAY", "NATO", "JAYA", "COCO", "MTPS", "CPRI", "HRME", "POSA", "JAST",
        "FITT", "BOLA", "CCSI", "SFAN", "POLU", "KJEN", "KAYU", "ITIC", "PAMG", "IPTV", "BLUE", "ENVY", "EAST", "LIFE",
        "FUJI", "KOTA", "INOV", "ARKA", "SMKL", "HDIT", "KEEN", "BAPI", "TFAS", "GGRP", "OPMS", "NZIA", "SLIS", "PURE",
        "IRRA", "DMMX", "SINI", "WOWS", "ESIP", "TEBE", "KEJU", "PSGO", "AGAR", "IFSH", "REAL", "IFII", "PMJS", "UCID",
        "GLVA", "PGJO", "AMAR", "CSRA", "INDO", "AMOR", "TRIN", "DMND", "PURA", "PTPW", "TAMA", "IKAN", "AYLS", "DADA",
        "ASPI", "ESTA", "BESS", "AMAN", "CARE", "SAMF", "SBAT", "KBAG", "CBMF", "RONY", "CSMI", "BBSS", "BHAT", "CASH",
        "TECH", "EPAC", "UANG", "PGUN", "SOFA", "PPGL", "TOYS", "SGER", "TRJA", "PNGO", "SCNP", "BBSI", "KMDS", "PURI",
        "SOHO", "HOMI", "ROCK", "ENZO", "PLAN", "PTDU", "ATAP", "VICI", "PMMP", "WIFI", "FAPA", "DCII", "KETR", "DGNS",
        "UFOE", "BANK", "WMUU", "EDGE", "UNIQ", "BEBS", "SNLK", "ZYRX", "LFLO", "FIMP", "TAPG", "NPGF", "LUCY", "ADCP",
        "HOPE", "MGLV", "TRUE", "LABA", "ARCI", "IPAC", "MASB", "BMHS", "FLMC", "NICL", "UVCR", "BUKA", "HAIS", "OILS",
        "GPSO", "MCOL", "RSGK", "RUNS", "SBMA", "CMNT", "GTSI", "IDEA", "KUAS", "BOBA", "MTEL", "DEPO", "BINO", "CMRY",
        "WGSH", "TAYS", "WMPP", "RMKE", "OBMD", "AVIA", "IPPE", "NASI", "BSML", "DRMA", "ADMR", "SEMA", "ASLC", "NETV",
        "BAUT", "ENAK", "NTBK", "SMKM", "STAA", "NANO", "BIKE", "WIRG", "SICO", "GOTO", "TLDN", "MTMH", "WINR", "IBOS",
        "OLIV", "ASHA", "SWID", "TRGU", "ARKO", "CHEM", "DEWI", "AXIO", "KRYA", "HATM", "RCCC", "GULA", "JARR", "AMMS",
        "RAFI", "KKES", "ELPI", "EURO", "KLIN", "TOOL", "BUAH", "CRAB", "MEDS", "COAL", "PRAY", "CBUT", "BELI", "MKTR",
        "OMED", "BSBK", "PDPP", "KDTN", "ZATA", "NINE", "MMIX", "PADA", "ISAP", "VTNY", "SOUL", "ELIT", "BEER", "CBPE",
        "SUNI", "CBRE", "WINE", "BMBL", "PEVE", "LAJU", "FWCT", "NAYZ", "IRSX", "PACK", "VAST", "CHIP", "HALO", "KING",
        "PGEO", "FUTR", "HILL", "BDKR", "PTMP", "SAGE", "TRON", "CUAN", "NSSS", "GTRA", "HAJJ", "PIPA", "NCKL", "MENN",
        "AWAN", "MBMA", "RAAM", "DOOH", "JATI", "TYRE", "MPXL", "SMIL", "KLAS", "MAXI", "VKTR", "RELF", "AMMN", "CRSN",
        "GRPM", "WIDI", "TGUK", "INET", "MAHA", "RMKO", "CNMA", "FOLK", "HBAT", "GRIA", "PPRI", "ERAL", "CYBR", "MUTU",
        "LMAX", "HUMI", "MSIE", "RSCH", "BABY", "AEGS", "IOTF", "KOCI", "PTPS", "BREN", "STRK", "KOKA", "LOPI", "UDNG",
        "RGAS", "MSTI", "IKPM", "AYAM", "SURI", "ASLI", "CGAS", "NICE", "MSJA", "SMLE", "ACRO", "MANG", "GRPH", "SMGA",
        "UNTD", "TOSK", "MPIX", "ALII", "MKAP", "MEJA", "LIVE", "HYGN", "BAIK", "VISI", "AREA", "MHKI", "ATLA", "DATA",
        "SOLA", "BATR", "SPRE", "PART", "GOLF", "ISEA", "BLES", "GUNA", "LABS", "DOSS", "NEST", "PTMR", "VERN", "DAAZ",
        "BOAT", "NAIK", "AADI", "MDIY", "KSIX", "RATU", "YOII", "HGII", "BRRC", "DGWG", "CBDK", "OBAT", "MINE", "KAQI",
        "YUPI", "FORE", "MDLA", "DKHH", "PSAT", "CDIA", "COIN", "BLOG", "CHEK", "MERI", "ASPR", "PMUI", "EMAS", "PJHB",
        "RLCO", "SUPA"
    ]
    MARKET_SUFFIX = ".JK"
    LOOKBACK_DAYS_HISTORY = 400
    RECENT_BARS = 60         # Gunakan angka besar (misal 60) untuk backfill 
    
    BACKTEST_WINDOW = 60     
    HORIZONS = [3, 5, 10, 20]
    AROON_LEN = 8
    KLINGER_FAST, KLINGER_SLOW, KLINGER_SIG, KLINGER_TRIG = 34, 55, 13, 13
    MACD_FAST, MACD_SLOW, MACD_SIG = 12, 26, 9
    UT_A, UT_C = 1.0, 10
    ST_PERIOD, ST_MULT = 10, 3.0
    REQUIRE_KO_POSITIVE = False
    REQUIRE_HIST_RISING = False
    USE_VOLUME_FILTER = True
    VOL_MA, VOL_MULT, MIN_VOL = 20, 1.5, 500_000
    PSAR_START, PSAR_INC, PSAR_MAX = 0.02, 0.02, 0.2

# ==============================================================================
# 2. DATA FETCHER
# ==============================================================================
class StockDataFetcher:
    def __init__(self, tickers, suffix=".JK", history_days=400):
        self.tickers = list(set([t + suffix if not t.endswith(suffix) else t for t in tickers]))
        self.start_date = (datetime.now() - timedelta(days=history_days)).strftime('%Y-%m-%d')

    def fetch(self, chunk_size=30):
        print(f"🚀 Memulai Download Data (Start: {self.start_date})...")
        all_dfs = {}
        for i in range(0, len(self.tickers), chunk_size):
            batch = self.tickers[i : i + chunk_size]
            try:
                data = yf.download(" ".join(batch), start=self.start_date, interval="1d", group_by="ticker", auto_adjust=False, threads=True, progress=False)
                if data.empty: continue
                if len(batch) == 1:
                    clean_name = batch[0].replace(".JK", "")
                    all_dfs[clean_name] = data
                else:
                    for t in batch:
                        if t in data.columns.levels[0]:
                            clean_name = t.replace(".JK", "")
                            df_t = data[t].copy()
                            df_t.dropna(how='all', inplace=True)
                            if not df_t.empty: all_dfs[clean_name] = df_t
            except Exception:
                continue
        print(f"✅ Selesai. Dapat {len(all_dfs)} ticker valid.\n")
        return all_dfs

# ==============================================================================
# 3. TECHNICAL INDICATORS & ML FEATURES
# ==============================================================================
class TechnicalIndicators:
    @staticmethod
    def wilder_rma(series, period): return series.ewm(alpha=1/period, adjust=False).mean()

    @staticmethod
    def compute_true_range(df):
        high, low, close, prev_close = df["High"], df["Low"], df["Close"], df["Close"].shift(1)
        return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)

    @staticmethod
    def add_klinger_pine_exact(df, trig_len=13, fast_x=34, slow_x=55):
        hlc3 = (df["High"] + df["Low"] + df["Close"]) / 3.0
        xTrend = pd.Series(np.where(hlc3 > hlc3.shift(1), df["Volume"] * 100.0, -df["Volume"] * 100.0), index=df.index)
        xKVO = xTrend.ewm(span=fast_x, adjust=False).mean() - xTrend.ewm(span=slow_x, adjust=False).mean()
        df["KO"], df["KO_Signal"] = xKVO, xKVO.ewm(span=trig_len, adjust=False).mean()
        return df

    @staticmethod
    def add_aroon_pine_exact(df, length=8):
        highs, lows, n = df["High"].values, df["Low"].values, len(df)
        highestbars_list, lowestbars_list = np.full(n, np.nan), np.full(n, np.nan)
        for i in range(length, n):
            highestbars_list[i] = np.argmax(highs[i - length : i + 1]) - length
            lowestbars_list[i] = np.argmin(lows[i - length : i + 1]) - length
        df["Aroon_Up"], df["Aroon_Down"] = 100.0 * (highestbars_list + length) / length, 100.0 * (lowestbars_list + length) / length
        return df

    @staticmethod
    def add_macd(df, fast=12, slow=26, signal=9):
        macd = df["Close"].ewm(span=fast, adjust=False).mean() - df["Close"].ewm(span=slow, adjust=False).mean()
        sig = macd.ewm(span=signal, adjust=False).mean()
        df["MACD"], df["MACD_Signal"], df["MACD_Hist"] = macd, sig, macd - sig
        return df

    @staticmethod
    def add_ut_bot(df, a=1.0, c=10):
        close = df["Close"]
        tr = TechnicalIndicators.compute_true_range(df)
        xATR = TechnicalIndicators.wilder_rma(tr, c)
        nLoss = a * xATR
        xATRTrailingStop = np.zeros(len(df))
        pos = np.zeros(len(df), dtype=int)
        src_val, nLoss_val = close.values, nLoss.values
        for i in range(1, len(df)):
            prev_stop, price, loss = xATRTrailingStop[i-1], src_val[i], nLoss_val[i]
            if (src_val[i-1] > prev_stop) and (price > prev_stop): xATRTrailingStop[i] = max(prev_stop, price - loss)
            elif (src_val[i-1] < prev_stop) and (price < prev_stop): xATRTrailingStop[i] = min(prev_stop, price + loss)
            elif price > prev_stop: xATRTrailingStop[i] = price - loss
            else: xATRTrailingStop[i] = price + loss
        for i in range(1, len(df)):
            price, prev_stop, prev_pos = src_val[i], xATRTrailingStop[i-1], pos[i-1]
            if (src_val[i-1] < prev_stop) and (price > prev_stop): pos[i] = 1
            elif (src_val[i-1] > prev_stop) and (price < prev_stop): pos[i] = -1
            else: pos[i] = prev_pos
        df["UT_Stop"], df["UT_Pos"] = xATRTrailingStop, pos
        df["UT_Buy"] = (df["UT_Pos"] == 1) & (df["UT_Pos"].shift(1) != 1)
        return df

    @staticmethod
    def add_supertrend(df, period=10, multiplier=3.0):
        src = (df["High"] + df["Low"]) / 2.0
        atr = TechnicalIndicators.wilder_rma(TechnicalIndicators.compute_true_range(df), period)
        up, dn = src - (multiplier * atr), src + (multiplier * atr)
        st, trend = np.zeros(len(df)), np.zeros(len(df), dtype=int)
        up_val, dn_val, close_val = up.values, dn.values, df["Close"].values
        st[0], trend[0] = up_val[0], 1
        for i in range(1, len(df)):
            prev_st = st[i-1]
            curr_up = max(up_val[i], st[i-1]) if close_val[i-1] > st[i-1] and trend[i-1] == 1 else up_val[i]
            curr_dn = min(dn_val[i], st[i-1]) if close_val[i-1] < st[i-1] and trend[i-1] == -1 else dn_val[i]
            prev_trend = trend[i-1]
            if prev_trend == -1 and close_val[i] > prev_st: trend[i], st[i] = 1, curr_up
            elif prev_trend == 1 and close_val[i] < prev_st: trend[i], st[i] = -1, curr_dn
            else: trend[i], st[i] = prev_trend, curr_up if trend[i] == 1 else curr_dn
        df["ST_Trend"] = trend
        df["ST_Buy"] = (df["ST_Trend"] == 1) & (pd.Series(trend).shift(1) == -1)
        return df

    @staticmethod
    def add_volume_filters(df, ma=20, mult=1.5, min_vol=500000):
        vol = df["Volume"]
        df["Volume_MA"] = vol.rolling(ma).mean()
        df["Volume_Spike"] = vol >= (mult * df["Volume_MA"])
        df["Volume_OK"] = vol >= min_vol
        df["Volume_Confirm"] = df["Volume_Spike"] | (vol >= df["Volume_MA"].fillna(0))
        return df

    @staticmethod
    def add_psar(df, start=0.02, increment=0.02, maximum=0.2):
        high, low, length = df['High'].values, df['Low'].values, len(df)
        psar, psar_trend = np.zeros(length), np.zeros(length, dtype=int)
        if length == 0: return df
        bull, af, hp, lp, psar[0] = True, start, high[0], low[0], low[0]
        for i in range(1, length):
            prev_psar = psar[i-1]
            if bull:
                psar[i] = min(prev_psar + af * (hp - prev_psar), low[i-1])
                if i > 1: psar[i] = min(psar[i], low[i-2])
                if low[i] < psar[i]:
                    bull, psar[i], hp, lp, af = False, hp, high[i], low[i], start
                else:
                    if high[i] > hp: hp, af = high[i], min(af + increment, maximum)
            else:
                psar[i] = max(prev_psar + af * (lp - prev_psar), high[i-1])
                if i > 1: psar[i] = max(psar[i], high[i-2])
                if high[i] > psar[i]:
                    bull, psar[i], hp, lp, af = True, lp, high[i], low[i], start
                else:
                    if low[i] < lp: lp, af = low[i], min(af + increment, maximum)
            psar_trend[i] = 1 if bull else -1
        df["PSAR"], df["PSAR_Trend"] = psar, psar_trend
        df["PSAR_Buy"] = (df["PSAR_Trend"] == 1) & (df["PSAR_Trend"].shift(1) == -1)
        return df

    # === FITUR KERNEL REGRESSION (PERSIS SEPERTI STANDALONE USER) ===
    @staticmethod
    def add_kernel_regression(df, h=8, r=8.0, x=25):
        weights = np.array([(1 + (i**2) / (2 * r * (h**2))) ** (-r) for i in range(x)])
        weights = weights / np.sum(weights)
        
        df['Kernel_yhat'] = df['Close'].rolling(window=x).apply(lambda vals: np.dot(vals[::-1], weights), raw=True)
        
        df['Is_Bullish_Rate'] = df['Kernel_yhat'] > df['Kernel_yhat'].shift(1)
        df['Is_Bearish_Rate'] = df['Kernel_yhat'] < df['Kernel_yhat'].shift(1)
        
        # Logika trigger mutlak: Hari ini Bullish, Kemarin Bearish
        df['Kernel_Red_to_Green'] = df['Is_Bullish_Rate'] & df['Is_Bearish_Rate'].shift(1)
        
        # Warna khusus tabel
        df['Kernel_Color'] = np.where(df['Is_Bullish_Rate'], '🟢 Hijau', '🔴 Merah')
        return df

    @staticmethod
    def add_lorentzian_features(df):
        delta = df['Close'].diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = -delta.clip(upper=0).rolling(14).mean()
        df['F_RSI'] = 100 - (100 / (1 + (gain / loss)))

        tp = (df['High'] + df['Low'] + df['Close']) / 3
        sma_tp = tp.rolling(20).mean()
        mad = tp.rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=False)
        df['F_CCI'] = (tp - sma_tp) / (0.015 * mad)

        tr = TechnicalIndicators.compute_true_range(df)
        atr = tr.rolling(14).mean()
        up_move = df['High'].diff()
        down_move = -df['Low'].diff()
        plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
        minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
        plus_di = 100 * pd.Series(plus_dm, index=df.index).rolling(14).mean() / atr
        minus_di = 100 * pd.Series(minus_dm, index=df.index).rolling(14).mean() / atr
        dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di)
        df['F_ADX'] = dx.rolling(14).mean()

        esa = tp.ewm(span=10, adjust=False).mean()
        d = np.abs(tp - esa).ewm(span=10, adjust=False).mean()
        ci = (tp - esa) / (0.015 * d)
        df['F_WT'] = ci.ewm(span=21, adjust=False).mean()

        df['F_RSI'] = df['F_RSI'].fillna(50)
        df['F_CCI'] = ((df['F_CCI'] + 200) / 4).clip(0, 100).fillna(50)
        df['F_ADX'] = df['F_ADX'].fillna(50)
        df['F_WT']  = ((df['F_WT'] + 100) / 2).clip(0, 100).fillna(50)

        df['ML_Label'] = np.where(df['Close'] > df['Close'].shift(4), 1, np.where(df['Close'] < df['Close'].shift(4), -1, 0))
        return df

# ==============================================================================
# 4. ENGINE LOGIC & EXECUTION
# ==============================================================================
class SignalLogic:
    def is_aroon_buys(self, df, j):
        if j <= 0: return False
        return (df["Aroon_Up"].iloc[j-1] <= df["Aroon_Down"].iloc[j-1]) and (df["Aroon_Up"].iloc[j] > df["Aroon_Down"].iloc[j])

    def is_ko_bullish(self, df, j, require_pos=True):
        if j <= 0: return False
        cross_up = (df["KO"].iloc[j-1] <= df["KO_Signal"].iloc[j-1]) and (df["KO"].iloc[j] > df["KO_Signal"].iloc[j])
        return False if not cross_up else (not require_pos or df["KO"].iloc[j] > 0)

    def is_macd_bullish(self, df, j, require_rising=False):
        if j <= 0: return False
        hist = df["MACD_Hist"].iloc[j]
        if hist <= 0: return False
        return False if require_rising and hist <= df["MACD_Hist"].iloc[j-1] else True

    def is_psar_bullish(self, df, j, require_fresh_crossover=False):
        if j <= 0: return False
        return bool(df["PSAR_Buy"].iloc[j]) if require_fresh_crossover else df["PSAR_Trend"].iloc[j] == 1

    def is_lorentzian_bullish(self, df, j, neighbors=8):
        if j < 50: return 0
        f_curr = df[['F_RSI', 'F_CCI', 'F_ADX', 'F_WT']].iloc[j].values
        start_idx = max(4, j - 400)
        hist_features = df[['F_RSI', 'F_CCI', 'F_ADX', 'F_WT']].iloc[start_idx:j-4].values
        hist_labels = df['ML_Label'].iloc[start_idx:j-4].values
        hist_features = hist_features[::-1][::4]
        hist_labels = hist_labels[::-1][::4]
        
        if len(hist_labels) < neighbors: return 0
        diff = np.abs(hist_features - f_curr)
        distances = np.sum(np.log(1 + diff), axis=1)
        top_indices = np.argsort(distances)[:neighbors]
        prediction = np.sum(hist_labels[top_indices])
        return prediction

class ScreenerEngine(SignalLogic):
    def __init__(self, data_dict): self.data_dict = data_dict

    def _prepare_df(self, df):
        if len(df) < 50: return None
        df = TechnicalIndicators.add_klinger_pine_exact(df.copy(), Config.KLINGER_TRIG, Config.KLINGER_FAST, Config.KLINGER_SLOW)
        df = TechnicalIndicators.add_aroon_pine_exact(df, Config.AROON_LEN)
        df = TechnicalIndicators.add_macd(df, Config.MACD_FAST, Config.MACD_SLOW, Config.MACD_SIG)
        df = TechnicalIndicators.add_volume_filters(df, Config.VOL_MA, Config.VOL_MULT, Config.MIN_VOL)
        df = TechnicalIndicators.add_ut_bot(df, Config.UT_A, Config.UT_C)
        df = TechnicalIndicators.add_supertrend(df, Config.ST_PERIOD, Config.ST_MULT)
        df = TechnicalIndicators.add_psar(df, Config.PSAR_START, Config.PSAR_INC, Config.PSAR_MAX)
        df = TechnicalIndicators.add_kernel_regression(df)
        df = TechnicalIndicators.add_lorentzian_features(df)
        df.dropna(inplace=True)
        return df

    def classify_pattern(self, row):
        st_trend, ut_pos, vol_spike, pct_price = row.get("ST_Trend", 0), row.get("UT_Pos", 0), row.get("Volume_Spike", False), row.get("Pct_Change_Price", 0)
        if st_trend == 1 and ut_pos == 1 and vol_spike and pct_price < 12: return "RUNNER"
        if ut_pos == 1 and vol_spike and pct_price >= 5: return "POP_CEPAT"
        return "NOISE_TRAP" if st_trend == -1 else "UNCLASSIFIED"

    def _package_result(self, t, df, j):
        row, prev = df.iloc[j], df.iloc[j-1]
        res = {
            "Ticker": t, "Signal_Date": row.name.date(), "Bars_Ago": len(df) - 1 - j,
            "Open": int(row["Open"]), "Close": int(row["Close"]), "Pct_Change_Price": round((row["Close"]-prev["Close"])/prev["Close"]*100, 2),
            "Volume": int(row["Volume"]), "Volume_Spike": bool(row["Volume_Spike"]),
            "KO": round(row["KO"], 2), "UT_Buy": bool(row["UT_Buy"]), "ST_Trend": int(row["ST_Trend"]),
            "Aroon_Up": round(row["Aroon_Up"], 1), "UT_Pos": int(row["UT_Pos"]),
            "PSAR_Trend": "Bull" if row["PSAR_Trend"] == 1 else "Bear",
            "Kernel_Color": row.get("Kernel_Color", "-"),
            "Kernel_Flip": "✅ Ya" if row.get("Kernel_Red_to_Green", False) else "❌ Tidak"
        }
        res["Pattern_Label"] = self.classify_pattern(res)
        return res

    def _finalize_and_sort(self, results):
        df = pd.DataFrame(results)
        return df.sort_values(by=["Signal_Date", "Volume_Spike", "Pct_Change_Price"], ascending=[False, False, False]).reset_index(drop=True) if not df.empty else df

    def run_super_screener(self):
        results = []
        for t, df in self.data_dict.items():
            if (df := self._prepare_df(df)) is None: continue
            for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
                if self.is_aroon_buys(df, j) and self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE) and self.is_macd_bullish(df, j, Config.REQUIRE_HIST_RISING) and (df["UT_Pos"].iloc[j] == 1) and (bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])):
                    results.append(self._package_result(t, df, j)); break
        return self._finalize_and_sort(results)

    def run_aroon_ut_screener(self):
        results = []
        for t, df in self.data_dict.items():
            if (df := self._prepare_df(df)) is None: continue
            for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
                if self.is_aroon_buys(df, j) and bool(df["UT_Buy"].iloc[j]):
                    results.append(self._package_result(t, df, j)); break
        return self._finalize_and_sort(results)

    def run_ko_ut_vol_screener(self):
        results = []
        for t, df in self.data_dict.items():
            if (df := self._prepare_df(df)) is None: continue
            for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
                if self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE) and bool(df["UT_Buy"].iloc[j]) and (bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])):
                    results.append(self._package_result(t, df, j)); break
        return self._finalize_and_sort(results)

    def run_aroon_psar_screener(self):
        results = []
        for t, df in self.data_dict.items():
            if (df := self._prepare_df(df)) is None: continue
            for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
                if self.is_aroon_buys(df, j) and self.is_psar_bullish(df, j, require_fresh_crossover=False) and (bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])):
                    results.append(self._package_result(t, df, j)); break
        return self._finalize_and_sort(results)

    # === UPDATE: LORENTZIAN SCREENER LOGIC (MATCH STANDALONE) ===
    def run_lorentzian_ml_screener(self):
        print("\n🔎 Running KERNEL LORENTZIAN SCREENER (Red-to-Green Only)...")
        results = []
        for t, df in self.data_dict.items():
            if (df := self._prepare_df(df)) is None: continue
            for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
                
                # TRIGGER UTAMA: Saham masuk jika garis mematah dari Merah ke Hijau
                c_kernel_flip = bool(df['Kernel_Red_to_Green'].iloc[j])
                
                # Syarat Volume (Opsional, tapi penting agar saham tidak ilikuid)
                c_vol = bool(df["Volume_OK"].iloc[j])

                if c_kernel_flip and c_vol:
                    # Ambil prediksi ML sebagai tambahan informasi di kolom
                    ml_score = self.is_lorentzian_bullish(df, j, neighbors=8)
                    
                    res = self._package_result(t, df, j)
                    
                    # Ubah label Pattern untuk menegaskan alasan masuk tabel ini
                    res["Pattern_Label"] = f"🟢 KERNEL FLIP (ML Score: {ml_score})"
                    
                    results.append(res)
                    break # Lanjut ke ticker berikutnya agar tidak dobel
        return self._finalize_and_sort(results)

def add_fundamentals(df):
    if df is None or df.empty: return df
    print(f"⏳ Mengambil fundamental untuk {len(df)} saham (menggunakan jeda waktu anti-blokir)...")
    pers, pbvs = [], []
    for t in df["Ticker"]:
        try:
            time.sleep(0.5) 
            info = yf.Ticker(t).info
            per = info.get('trailingPE') or info.get('forwardPE', 'N/A')
            pbv = info.get('priceToBook', 'N/A')
            pers.append(round(per, 2) if isinstance(per, (int, float)) else per)
            pbvs.append(round(pbv, 2) if isinstance(pbv, (int, float)) else pbv)
        except Exception:
            pers.append('N/A'); pbvs.append('N/A')
    df_copy = df.copy()
    df_copy["PER"], df_copy["PBV"] = pers, pbvs
    return df_copy

def send_telegram_message(data_dict, date_str):
    bot_token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    if not bot_token or not chat_id:
        print("⚠️ Token/Chat ID Telegram tidak ada. Melewati pengiriman pesan.")
        return

    def get_tickers(lst): return ", ".join([item["Ticker"] for item in lst]) if lst else "Tidak ada"

    msg = f"<b>🚀 Hasil Screener Saham IDX - {date_str}</b>\n\n"
    msg += f"<b>🤖 ML Lorentzian (Red-to-Green):</b>\n{get_tickers(data_dict['lorentzian_ml'])}\n\n"
    msg += f"<b>🏆 Super Screener:</b>\n{get_tickers(data_dict['super_screener'])}\n\n"
    msg += f"<b>🎯 Aroon + UT:</b>\n{get_tickers(data_dict['aroon_ut'])}\n\n"
    msg += f"<b>🔥 KO + UT + Vol:</b>\n{get_tickers(data_dict['ko_ut_vol'])}\n\n"
    msg += f"<b>⚡ Aroon + PSAR:</b>\n{get_tickers(data_dict['aroon_psar'])}\n\n"
    msg += f"<a href='https://badrut25.github.io/idx-screener-v1/'>Buka Dashboard Web</a>"

    try:
        res = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={"chat_id": chat_id, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": True})
        print("✅ Pesan Telegram berhasil dikirim!" if res.status_code == 200 else f"❌ Gagal Telegram: {res.text}")
    except Exception as e:
        print(f"❌ Error Telegram: {e}")

if __name__ == "__main__":
    fetcher = StockDataFetcher(Config.TICKERS, Config.MARKET_SUFFIX, Config.LOOKBACK_DAYS_HISTORY)
    data_storage = fetcher.fetch()
    screener = ScreenerEngine(data_storage)

    # JALANKAN SCREENER MACHINE LEARNING
    res_lorentzian = add_fundamentals(screener.run_lorentzian_ml_screener())

    res_super = add_fundamentals(screener.run_super_screener())
    res_aroon_ut = add_fundamentals(screener.run_aroon_ut_screener())
    res_ko_ut = add_fundamentals(screener.run_ko_ut_vol_screener())
    res_aroon_psar = add_fundamentals(screener.run_aroon_psar_screener())
    
    os.makedirs('docs', exist_ok=True)

    last_dates = [df.index[-1] for df in data_storage.values() if not df.empty]
    if last_dates:
        market_date = max(last_dates)
        today_str = market_date.strftime("%Y-%m-%d")
    else:
        wib_tz = timezone(timedelta(hours=7))
        today_str = datetime.now(wib_tz).strftime("%Y-%m-%d")

    wib_tz = timezone(timedelta(hours=7))
    timestamp_str = datetime.now(wib_tz).strftime("%Y-%m-%d %H:%M:%S WIB")

    export_data = {
        "last_update": timestamp_str,
        "lorentzian_ml": res_lorentzian.to_dict(orient="records") if not res_lorentzian.empty else [],
        "super_screener": res_super.to_dict(orient="records") if not res_super.empty else [],
        "aroon_ut": res_aroon_ut.to_dict(orient="records") if not res_aroon_ut.empty else [],
        "ko_ut_vol": res_ko_ut.to_dict(orient="records") if not res_ko_ut.empty else [],
        "aroon_psar": res_aroon_psar.to_dict(orient="records") if not res_aroon_psar.empty else []
    }

    with open(f'docs/data_{today_str}.json', 'w') as f: json.dump(export_data, f, default=str)
    with open('docs/data.json', 'w') as f: json.dump(export_data, f, default=str)

    history_files = glob.glob('docs/data_*.json')
    available_dates = [os.path.basename(f).replace('data_', '').replace('.json', '') for f in history_files]
    available_dates = list(set(available_dates))
    available_dates.sort(reverse=True)

    with open('docs/history_list.json', 'w') as f: json.dump(available_dates, f)
        
    print(f"✅ Data market tanggal {today_str} berhasil diekspor!")
    send_telegram_message(export_data, today_str)
    
# # @title OOP Complete Suite: 3 Screeners + 3 Backtesters + Telegram + WIB Timezone
# import numpy as np
# import pandas as pd
# import yfinance as yf
# from datetime import datetime, timedelta, timezone
# from tabulate import tabulate
# import json
# import os
# import glob
# import time
# import requests

# # ==============================================================================
# # 1. CONFIGURATION
# # ==============================================================================
# class Config:
#     TICKERS = [
#         "AALI", "ABBA", "ABDA", "ABMM", "ACES", "ACST", "ADES", "ADHI", "ADMF", "ADMG", "ADRO", "AGII", "AGRO", "AGRS",
#         "AHAP", "AIMS", "AISA", "AKKU", "AKPI", "AKRA", "AKSI", "ALDO", "ALKA", "ALMI", "ALTO", "AMAG", "AMFG", "AMIN",
#         "AMRT", "ANJT", "ANTM", "APEX", "APIC", "APII", "APLI", "APLN", "ARGO", "ARII", "ARNA", "ARTA", "ARTI", "ARTO",
#         "ASBI", "ASDM", "ASGR", "ASII", "ASJT", "ASMI", "ASRI", "ASRM", "ASSA", "ATIC", "AUTO", "BABP", "BACA", "BAJA",
#         "BALI", "BAPA", "BATA", "BAYU", "BBCA", "BBHI", "BBKP", "BBLD", "BBMD", "BBNI", "BBRI", "BBRM", "BBTN", "BBYB",
#         "BCAP", "BCIC", "BCIP", "BDMN", "BEKS", "BEST", "BFIN", "BGTG", "BHIT", "BIKA", "BIMA", "BINA", "BIPI", "BIPP",
#         "BIRD", "BISI", "BJBR", "BJTM", "BKDP", "BKSL", "BKSW", "BLTA", "BLTZ", "BMAS", "BMRI", "BMSR", "BMTR", "BNBA",
#         "BNBR", "BNGA", "BNII", "BNLI", "BOLT", "BPFI", "BPII", "BRAM", "BRMS", "BRNA", "BRPT", "BSDE", "BSIM", "BSSR",
#         "BSWD", "BTEK", "BTEL", "BTON", "BTPN", "BUDI", "BUKK", "BULL", "BUMI", "BUVA", "BVIC", "BWPT", "BYAN", "CANI",
#         "CASS", "CEKA", "CENT", "CFIN", "CINT", "CITA", "CLPI", "CMNP", "CMPP", "CNKO", "CNTX", "COWL", "CPIN", "CPRO",
#         "CSAP", "CTBN", "CTRA", "CTTH", "DART", "DEFI", "DEWA", "DGIK", "DILD", "DKFT", "DLTA", "DMAS", "DNAR", "DNET",
#         "DOID", "DPNS", "DSFI", "DSNG", "DSSA", "DUTI", "DVLA", "DYAN", "ECII", "EKAD", "ELSA", "ELTY", "EMDE", "EMTK",
#         "ENRG", "EPMT", "ERAA", "ERTX", "ESSA", "ESTI", "ETWA", "EXCL", "FAST", "FASW", "FISH", "FMII", "FORU", "FPNI",
#         "GAMA", "GDST", "GDYR", "GEMA", "GEMS", "GGRM", "GIAA", "GJTL", "GLOB", "GMTD", "GOLD", "GOLL", "GPRA", "GSMF",
#         "GTBO", "GWSA", "GZCO", "HADE", "HDFA", "HDTX", "HERO", "HEXA", "HITS", "HMSP", "HOME", "HOTL", "HRUM", "IATA",
#         "IBFN", "IBST", "ICBP", "ICON", "IGAR", "IIKP", "IKAI", "IKBI", "IMAS", "IMJS", "IMPC", "INAF", "INAI", "INCI",
#         "INCO", "INDF", "INDR", "INDS", "INDX", "INDY", "INKP", "INPC", "INPP", "INRU", "INTA", "INTD", "INTP", "IPOL",
#         "ISAT", "ISSP", "ITMA", "ITMG", "JAWA", "JECC", "JIHD", "JKON", "JKSW", "JPFA", "JRPT", "JSMR", "JSPT", "JTPE",
#         "KAEF", "KARW", "KBLI", "KBLM", "KBLV", "KBRI", "KDSI", "KIAS", "KICI", "KIJA", "KKGI", "KLBF", "KOBX", "KOIN",
#         "KONI", "KOPI", "KPIG", "KRAH", "KRAS", "KREN", "LAPD", "LCGP", "LEAD", "LINK", "LION", "LMAS", "LMPI", "LMSH",
#         "LPCK", "LPGI", "LPIN", "LPKR", "LPLI", "LPPF", "LPPS", "LRNA", "LSIP", "LTLS", "MAGP", "MAIN", "MAMI", "MAPI",
#         "MAYA", "MBAP", "MBSS", "MBTO", "MCOR", "MDIA", "MDKA", "MDLN", "MDRN", "MEDC", "MEGA", "MERK", "META",
#         "MFMI", "MGNA", "MICE", "MIDI", "MIKA", "MIRA", "MITI", "MKPI", "MLBI", "MLIA", "MLPL", "MLPT", "MMLP",
#         "MNCN", "MPMX", "MPPA", "MRAT", "MREI", "MSKY", "MTDL", "MTFN", "MTLA", "MTSM", "MYOH", "MYOR", "MYRX", "MYTX",
#         "NELY", "NIKL", "NIPS", "NIRO", "NISP", "NOBU", "NRCA", "OCAP", "OKAS", "OMRE", "PADI", "PALM", "PANR", "PANS",
#         "PBRX", "PDES", "PEGE", "PGAS", "PGLI", "PICO", "PJAA", "PKPK", "PLAS", "PLIN", "PNBN", "PNBS", "PNIN", "PNLF",
#         "PNSE", "POLY", "POOL", "PPRO", "PRAS", "PSAB", "PSDN", "PSKT", "PTBA", "PTIS", "PTPP", "PTRO", "PTSN", "PTSP",
#         "PUDP", "PWON", "PYFA", "RAJA", "RALS", "RANC", "RBMS", "RDTX", "RELI", "RICY", "RIGS", "RIMO", "RODA", "ROTI",
#         "RUIS", "SAFE", "SAME", "SCCO", "SCMA", "SCPI", "SDMU", "SDPC", "SDRA", "SGRO", "SHID", "SIDO", "SILO", "SIMA",
#         "SIMP", "SIPD", "SKBM", "SKLT", "SKYB", "SMAR", "SMBR", "SMCB", "SMDM", "SMDR", "SMGR", "SMMA", "SMMT", "SMRA",
#         "SMRU", "SMSM", "SOCI", "SONA", "SPMA", "SQMI", "SRAJ", "SRIL", "SRSN", "SRTG", "SSIA", "SSMS", "SSTM", "STAR",
#         "STTP", "SUGI", "SULI", "SUPR", "TALF", "TARA", "TAXI", "TBIG", "TBLA", "TBMS", "TCID", "TELE", "TFCO", "TGKA",
#         "TIFA", "TINS", "TIRA", "TIRT", "TKIM", "TLKM", "TMAS", "TMPO", "TOBA", "TOTL", "TOTO", "TOWR", "TPIA", "TPMA",
#         "TRAM", "TRIL", "TRIM", "TRIO", "TRIS", "TRST", "TRUS", "TSPC", "ULTJ", "UNIC", "UNIT", "UNSP", "UNTR", "UNVR",
#         "VICO", "VINS", "VIVA", "VOKS", "VRNA", "WAPO", "WEHA", "WICO", "WIIM", "WIKA", "WINS", "WOMF", "WSKT", "WTON",
#         "YPAS", "YULE", "ZBRA", "SHIP", "CASA", "DAYA", "DPUM", "IDPR", "JGLE", "KINO", "MARI", "MKNT", "MTRA", "OASA",
#         "POWR", "INCF", "WSBP", "PBSA", "PRDA", "BOGA", "BRIS", "PORT", "CARS", "MINA", "FORZ", "CLEO", "TAMU", "CSIS",
#         "TGRA", "FIRE", "TOPS", "KMTR", "ARMY", "MAPB", "WOOD", "HRTA", "MABA", "HOKI", "MPOW", "MARK", "NASA", "MDKI",
#         "BELL", "KIOS", "GMFI", "MTWI", "ZINC", "MCAS", "PPRE", "WEGE", "PSSI", "MORA", "DWGL", "PBID", "JMAS", "CAMP",
#         "IPCM", "PCAR", "LCKM", "BOSS", "HELI", "JSKY", "INPS", "GHON", "TDPM", "DFAM", "NICK", "BTPS", "SPTO", "PRIM",
#         "HEAL", "TRUK", "PZZA", "TUGU", "MSIN", "SWAT", "KPAL", "TNCA", "MAPA", "TCPI", "IPCC", "RISE", "BPTR", "POLL",
#         "NFCX", "MGRO", "NUSA", "FILM", "ANDI", "LAND", "MOLI", "PANI", "DIGI", "CITY", "SAPX", "KPAS", "SURE", "HKMU",
#         "MPRO", "DUCK", "GOOD", "SKRN", "YELO", "CAKK", "SATU", "SOSS", "DEAL", "POLA", "DIVA", "LUCK", "URBN", "SOTS",
#         "ZONE", "PEHA", "FOOD", "BEEF", "POLI", "CLAY", "NATO", "JAYA", "COCO", "MTPS", "CPRI", "HRME", "POSA", "JAST",
#         "FITT", "BOLA", "CCSI", "SFAN", "POLU", "KJEN", "KAYU", "ITIC", "PAMG", "IPTV", "BLUE", "ENVY", "EAST", "LIFE",
#         "FUJI", "KOTA", "INOV", "ARKA", "SMKL", "HDIT", "KEEN", "BAPI", "TFAS", "GGRP", "OPMS", "NZIA", "SLIS", "PURE",
#         "IRRA", "DMMX", "SINI", "WOWS", "ESIP", "TEBE", "KEJU", "PSGO", "AGAR", "IFSH", "REAL", "IFII", "PMJS", "UCID",
#         "GLVA", "PGJO", "AMAR", "CSRA", "INDO", "AMOR", "TRIN", "DMND", "PURA", "PTPW", "TAMA", "IKAN", "AYLS", "DADA",
#         "ASPI", "ESTA", "BESS", "AMAN", "CARE", "SAMF", "SBAT", "KBAG", "CBMF", "RONY", "CSMI", "BBSS", "BHAT", "CASH",
#         "TECH", "EPAC", "UANG", "PGUN", "SOFA", "PPGL", "TOYS", "SGER", "TRJA", "PNGO", "SCNP", "BBSI", "KMDS", "PURI",
#         "SOHO", "HOMI", "ROCK", "ENZO", "PLAN", "PTDU", "ATAP", "VICI", "PMMP", "WIFI", "FAPA", "DCII", "KETR", "DGNS",
#         "UFOE", "BANK", "WMUU", "EDGE", "UNIQ", "BEBS", "SNLK", "ZYRX", "LFLO", "FIMP", "TAPG", "NPGF", "LUCY", "ADCP",
#         "HOPE", "MGLV", "TRUE", "LABA", "ARCI", "IPAC", "MASB", "BMHS", "FLMC", "NICL", "UVCR", "BUKA", "HAIS", "OILS",
#         "GPSO", "MCOL", "RSGK", "RUNS", "SBMA", "CMNT", "GTSI", "IDEA", "KUAS", "BOBA", "MTEL", "DEPO", "BINO", "CMRY",
#         "WGSH", "TAYS", "WMPP", "RMKE", "OBMD", "AVIA", "IPPE", "NASI", "BSML", "DRMA", "ADMR", "SEMA", "ASLC", "NETV",
#         "BAUT", "ENAK", "NTBK", "SMKM", "STAA", "NANO", "BIKE", "WIRG", "SICO", "GOTO", "TLDN", "MTMH", "WINR", "IBOS",
#         "OLIV", "ASHA", "SWID", "TRGU", "ARKO", "CHEM", "DEWI", "AXIO", "KRYA", "HATM", "RCCC", "GULA", "JARR", "AMMS",
#         "RAFI", "KKES", "ELPI", "EURO", "KLIN", "TOOL", "BUAH", "CRAB", "MEDS", "COAL", "PRAY", "CBUT", "BELI", "MKTR",
#         "OMED", "BSBK", "PDPP", "KDTN", "ZATA", "NINE", "MMIX", "PADA", "ISAP", "VTNY", "SOUL", "ELIT", "BEER", "CBPE",
#         "SUNI", "CBRE", "WINE", "BMBL", "PEVE", "LAJU", "FWCT", "NAYZ", "IRSX", "PACK", "VAST", "CHIP", "HALO", "KING",
#         "PGEO", "FUTR", "HILL", "BDKR", "PTMP", "SAGE", "TRON", "CUAN", "NSSS", "GTRA", "HAJJ", "PIPA", "NCKL", "MENN",
#         "AWAN", "MBMA", "RAAM", "DOOH", "JATI", "TYRE", "MPXL", "SMIL", "KLAS", "MAXI", "VKTR", "RELF", "AMMN", "CRSN",
#         "GRPM", "WIDI", "TGUK", "INET", "MAHA", "RMKO", "CNMA", "FOLK", "HBAT", "GRIA", "PPRI", "ERAL", "CYBR", "MUTU",
#         "LMAX", "HUMI", "MSIE", "RSCH", "BABY", "AEGS", "IOTF", "KOCI", "PTPS", "BREN", "STRK", "KOKA", "LOPI", "UDNG",
#         "RGAS", "MSTI", "IKPM", "AYAM", "SURI", "ASLI", "CGAS", "NICE", "MSJA", "SMLE", "ACRO", "MANG", "GRPH", "SMGA",
#         "UNTD", "TOSK", "MPIX", "ALII", "MKAP", "MEJA", "LIVE", "HYGN", "BAIK", "VISI", "AREA", "MHKI", "ATLA", "DATA",
#         "SOLA", "BATR", "SPRE", "PART", "GOLF", "ISEA", "BLES", "GUNA", "LABS", "DOSS", "NEST", "PTMR", "VERN", "DAAZ",
#         "BOAT", "NAIK", "AADI", "MDIY", "KSIX", "RATU", "YOII", "HGII", "BRRC", "DGWG", "CBDK", "OBAT", "MINE", "KAQI",
#         "YUPI", "FORE", "MDLA", "DKHH", "PSAT", "CDIA", "COIN", "BLOG", "CHEK", "MERI", "ASPR", "PMUI", "EMAS", "PJHB",
#         "RLCO", "SUPA"
#     ]
#     MARKET_SUFFIX = ".JK"
#     LOOKBACK_DAYS_HISTORY = 400
    
#     # DIKEMBALIKAN KE 2 AGAR TIDAK TERLALU KETAT
#     RECENT_BARS = 1          
    
#     BACKTEST_WINDOW = 60     
#     HORIZONS = [3, 5, 10, 20]
#     AROON_LEN = 8
#     KLINGER_FAST, KLINGER_SLOW, KLINGER_SIG, KLINGER_TRIG = 34, 55, 13, 13
#     MACD_FAST, MACD_SLOW, MACD_SIG = 12, 26, 9
#     UT_A, UT_C = 1.0, 10
#     ST_PERIOD, ST_MULT = 10, 3.0
#     REQUIRE_KO_POSITIVE = False
#     REQUIRE_HIST_RISING = False
#     USE_VOLUME_FILTER = True
#     VOL_MA, VOL_MULT, MIN_VOL = 20, 1.5, 500_000
#     PSAR_START, PSAR_INC, PSAR_MAX = 0.02, 0.02, 0.2

# # ==============================================================================
# # 2. DATA FETCHER (Chunking)
# # ==============================================================================
# class StockDataFetcher:
#     def __init__(self, tickers, suffix=".JK", history_days=400):
#         self.tickers = list(set([t + suffix if not t.endswith(suffix) else t for t in tickers]))
#         self.start_date = (datetime.now() - timedelta(days=history_days)).strftime('%Y-%m-%d')

#     def fetch(self, chunk_size=30):
#         print(f"🚀 Memulai Download Data (Start: {self.start_date})...")
#         all_dfs = {}
#         for i in range(0, len(self.tickers), chunk_size):
#             batch = self.tickers[i : i + chunk_size]
#             try:
#                 data = yf.download(" ".join(batch), start=self.start_date, interval="1d", group_by="ticker", auto_adjust=False, threads=True, progress=False)
#                 if data.empty: continue
#                 if len(batch) == 1:
#                     clean_name = batch[0].replace(".JK", "")
#                     all_dfs[clean_name] = data
#                 else:
#                     for t in batch:
#                         if t in data.columns.levels[0]:
#                             clean_name = t.replace(".JK", "")
#                             df_t = data[t].copy()
#                             df_t.dropna(how='all', inplace=True)
#                             if not df_t.empty: all_dfs[clean_name] = df_t
#             except Exception as e:
#                 continue
#         print(f"✅ Selesai. Dapat {len(all_dfs)} ticker valid.\n")
#         return all_dfs

# # ==============================================================================
# # 3. TECHNICAL INDICATORS
# # ==============================================================================
# class TechnicalIndicators:
#     @staticmethod
#     def wilder_rma(series, period): return series.ewm(alpha=1/period, adjust=False).mean()

#     @staticmethod
#     def compute_true_range(df):
#         high, low, close, prev_close = df["High"], df["Low"], df["Close"], df["Close"].shift(1)
#         return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)

#     @staticmethod
#     def add_klinger_pine_exact(df, trig_len=13, fast_x=34, slow_x=55):
#         hlc3 = (df["High"] + df["Low"] + df["Close"]) / 3.0
#         xTrend = pd.Series(np.where(hlc3 > hlc3.shift(1), df["Volume"] * 100.0, -df["Volume"] * 100.0), index=df.index)
#         xKVO = xTrend.ewm(span=fast_x, adjust=False).mean() - xTrend.ewm(span=slow_x, adjust=False).mean()
#         df["KO"], df["KO_Signal"] = xKVO, xKVO.ewm(span=trig_len, adjust=False).mean()
#         return df

#     @staticmethod
#     def add_aroon_pine_exact(df, length=8):
#         highs, lows, n = df["High"].values, df["Low"].values, len(df)
#         highestbars_list, lowestbars_list = np.full(n, np.nan), np.full(n, np.nan)
#         for i in range(length, n):
#             highestbars_list[i] = np.argmax(highs[i - length : i + 1]) - length
#             lowestbars_list[i] = np.argmin(lows[i - length : i + 1]) - length
#         df["Aroon_Up"], df["Aroon_Down"] = 100.0 * (highestbars_list + length) / length, 100.0 * (lowestbars_list + length) / length
#         return df

#     @staticmethod
#     def add_macd(df, fast=12, slow=26, signal=9):
#         macd = df["Close"].ewm(span=fast, adjust=False).mean() - df["Close"].ewm(span=slow, adjust=False).mean()
#         sig = macd.ewm(span=signal, adjust=False).mean()
#         df["MACD"], df["MACD_Signal"], df["MACD_Hist"] = macd, sig, macd - sig
#         return df

#     @staticmethod
#     def add_ut_bot(df, a=1.0, c=10):
#         close = df["Close"]
#         tr = TechnicalIndicators.compute_true_range(df)
#         xATR = TechnicalIndicators.wilder_rma(tr, c)
#         nLoss = a * xATR

#         xATRTrailingStop = np.zeros(len(df))
#         pos = np.zeros(len(df), dtype=int)
#         src_val, nLoss_val = close.values, nLoss.values

#         for i in range(1, len(df)):
#             prev_stop, price, loss = xATRTrailingStop[i-1], src_val[i], nLoss_val[i]
#             if (src_val[i-1] > prev_stop) and (price > prev_stop): xATRTrailingStop[i] = max(prev_stop, price - loss)
#             elif (src_val[i-1] < prev_stop) and (price < prev_stop): xATRTrailingStop[i] = min(prev_stop, price + loss)
#             elif price > prev_stop: xATRTrailingStop[i] = price - loss
#             else: xATRTrailingStop[i] = price + loss

#         for i in range(1, len(df)):
#             price, prev_stop, prev_pos = src_val[i], xATRTrailingStop[i-1], pos[i-1]
#             if (src_val[i-1] < prev_stop) and (price > prev_stop): pos[i] = 1
#             elif (src_val[i-1] > prev_stop) and (price < prev_stop): pos[i] = -1
#             else: pos[i] = prev_pos

#         df["UT_Stop"], df["UT_Pos"] = xATRTrailingStop, pos
#         df["UT_Buy"] = (df["UT_Pos"] == 1) & (df["UT_Pos"].shift(1) != 1)
#         return df

#     @staticmethod
#     def add_supertrend(df, period=10, multiplier=3.0):
#         src = (df["High"] + df["Low"]) / 2.0
#         atr = TechnicalIndicators.wilder_rma(TechnicalIndicators.compute_true_range(df), period)
#         up, dn = src - (multiplier * atr), src + (multiplier * atr)
#         st, trend = np.zeros(len(df)), np.zeros(len(df), dtype=int)
#         up_val, dn_val, close_val = up.values, dn.values, df["Close"].values
#         st[0], trend[0] = up_val[0], 1

#         for i in range(1, len(df)):
#             prev_st = st[i-1]
#             curr_up = max(up_val[i], st[i-1]) if close_val[i-1] > st[i-1] and trend[i-1] == 1 else up_val[i]
#             curr_dn = min(dn_val[i], st[i-1]) if close_val[i-1] < st[i-1] and trend[i-1] == -1 else dn_val[i]
#             prev_trend = trend[i-1]
#             if prev_trend == -1 and close_val[i] > prev_st: trend[i], st[i] = 1, curr_up
#             elif prev_trend == 1 and close_val[i] < prev_st: trend[i], st[i] = -1, curr_dn
#             else: trend[i], st[i] = prev_trend, curr_up if trend[i] == 1 else curr_dn

#         df["ST_Trend"] = trend
#         df["ST_Buy"] = (df["ST_Trend"] == 1) & (pd.Series(trend).shift(1) == -1)
#         return df

#     @staticmethod
#     def add_volume_filters(df, ma=20, mult=1.5, min_vol=500000):
#         vol = df["Volume"]
#         df["Volume_MA"] = vol.rolling(ma).mean()
#         df["Volume_Spike"] = vol >= (mult * df["Volume_MA"])
#         df["Volume_OK"] = vol >= min_vol
#         df["Volume_Confirm"] = df["Volume_Spike"] | (vol >= df["Volume_MA"].fillna(0))
#         return df

#     @staticmethod
#     def add_psar(df, start=0.02, increment=0.02, maximum=0.2):
#         high, low, length = df['High'].values, df['Low'].values, len(df)
#         psar, psar_trend = np.zeros(length), np.zeros(length, dtype=int)
#         if length == 0: return df

#         bull, af, hp, lp, psar[0] = True, start, high[0], low[0], low[0]

#         for i in range(1, length):
#             prev_psar = psar[i-1]
#             if bull:
#                 psar[i] = min(prev_psar + af * (hp - prev_psar), low[i-1])
#                 if i > 1: psar[i] = min(psar[i], low[i-2])
#                 if low[i] < psar[i]:
#                     bull, psar[i], hp, lp, af = False, hp, high[i], low[i], start
#                 else:
#                     if high[i] > hp: hp, af = high[i], min(af + increment, maximum)
#             else:
#                 psar[i] = max(prev_psar + af * (lp - prev_psar), high[i-1])
#                 if i > 1: psar[i] = max(psar[i], high[i-2])
#                 if high[i] > psar[i]:
#                     bull, psar[i], hp, lp, af = True, lp, high[i], low[i], start
#                 else:
#                     if low[i] < lp: lp, af = low[i], min(af + increment, maximum)
#             psar_trend[i] = 1 if bull else -1

#         df["PSAR"], df["PSAR_Trend"] = psar, psar_trend
#         df["PSAR_Buy"] = (df["PSAR_Trend"] == 1) & (df["PSAR_Trend"].shift(1) == -1)
#         return df

# # ==============================================================================
# # 4. ENGINE LOGIC & EXECUTION
# # ==============================================================================
# class SignalLogic:
#     def is_aroon_buys(self, df, j):
#         if j <= 0: return False
#         return (df["Aroon_Up"].iloc[j-1] <= df["Aroon_Down"].iloc[j-1]) and (df["Aroon_Up"].iloc[j] > df["Aroon_Down"].iloc[j])

#     def is_ko_bullish(self, df, j, require_pos=True):
#         if j <= 0: return False
#         cross_up = (df["KO"].iloc[j-1] <= df["KO_Signal"].iloc[j-1]) and (df["KO"].iloc[j] > df["KO_Signal"].iloc[j])
#         return False if not cross_up else (not require_pos or df["KO"].iloc[j] > 0)

#     def is_macd_bullish(self, df, j, require_rising=False):
#         if j <= 0: return False
#         hist = df["MACD_Hist"].iloc[j]
#         if hist <= 0: return False
#         return False if require_rising and hist <= df["MACD_Hist"].iloc[j-1] else True

#     def is_psar_bullish(self, df, j, require_fresh_crossover=False):
#         if j <= 0: return False
#         return bool(df["PSAR_Buy"].iloc[j]) if require_fresh_crossover else df["PSAR_Trend"].iloc[j] == 1

# class ScreenerEngine(SignalLogic):
#     def __init__(self, data_dict): self.data_dict = data_dict

#     def _prepare_df(self, df):
#         if len(df) < 50: return None
#         df = TechnicalIndicators.add_klinger_pine_exact(df.copy(), Config.KLINGER_TRIG, Config.KLINGER_FAST, Config.KLINGER_SLOW)
#         df = TechnicalIndicators.add_aroon_pine_exact(df, Config.AROON_LEN)
#         df = TechnicalIndicators.add_macd(df, Config.MACD_FAST, Config.MACD_SLOW, Config.MACD_SIG)
#         df = TechnicalIndicators.add_volume_filters(df, Config.VOL_MA, Config.VOL_MULT, Config.MIN_VOL)
#         df = TechnicalIndicators.add_ut_bot(df, Config.UT_A, Config.UT_C)
#         df = TechnicalIndicators.add_supertrend(df, Config.ST_PERIOD, Config.ST_MULT)
#         df = TechnicalIndicators.add_psar(df, Config.PSAR_START, Config.PSAR_INC, Config.PSAR_MAX)
#         df.dropna(inplace=True)
#         return df

#     def classify_pattern(self, row):
#         st_trend, ut_pos, vol_spike, pct_price = row.get("ST_Trend", 0), row.get("UT_Pos", 0), row.get("Volume_Spike", False), row.get("Pct_Change_Price", 0)
#         if st_trend == 1 and ut_pos == 1 and vol_spike and pct_price < 12: return "RUNNER"
#         if ut_pos == 1 and vol_spike and pct_price >= 5: return "POP_CEPAT"
#         return "NOISE_TRAP" if st_trend == -1 else "UNCLASSIFIED"

#     def _package_result(self, t, df, j):
#         row, prev = df.iloc[j], df.iloc[j-1]
#         res = {
#             "Ticker": t, "Signal_Date": row.name.date(), "Bars_Ago": len(df) - 1 - j,
#             "Open": int(row["Open"]), "Close": int(row["Close"]), "Pct_Change_Price": round((row["Close"]-prev["Close"])/prev["Close"]*100, 2),
#             "Volume": int(row["Volume"]), "Volume_Spike": bool(row["Volume_Spike"]),
#             "KO": round(row["KO"], 2), "UT_Buy": bool(row["UT_Buy"]), "ST_Trend": int(row["ST_Trend"]),
#             "Aroon_Up": round(row["Aroon_Up"], 1), "UT_Pos": int(row["UT_Pos"]),
#             "PSAR_Trend": "Bull" if row["PSAR_Trend"] == 1 else "Bear"
#         }
#         res["Pattern_Label"] = self.classify_pattern(res)
#         return res

#     def _finalize_and_sort(self, results):
#         df = pd.DataFrame(results)
#         return df.sort_values(by=["Signal_Date", "Volume_Spike", "Pct_Change_Price"], ascending=[False, False, False]).reset_index(drop=True) if not df.empty else df

#     def run_super_screener(self):
#         results = []
#         for t, df in self.data_dict.items():
#             if (df := self._prepare_df(df)) is None: continue
#             for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
#                 if self.is_aroon_buys(df, j) and self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE) and self.is_macd_bullish(df, j, Config.REQUIRE_HIST_RISING) and (df["UT_Pos"].iloc[j] == 1) and (bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])):
#                     results.append(self._package_result(t, df, j)); break
#         return self._finalize_and_sort(results)

#     def run_aroon_ut_screener(self):
#         results = []
#         for t, df in self.data_dict.items():
#             if (df := self._prepare_df(df)) is None: continue
#             for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
#                 if self.is_aroon_buys(df, j) and bool(df["UT_Buy"].iloc[j]):
#                     results.append(self._package_result(t, df, j)); break
#         return self._finalize_and_sort(results)

#     def run_ko_ut_vol_screener(self):
#         results = []
#         for t, df in self.data_dict.items():
#             if (df := self._prepare_df(df)) is None: continue
#             for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
#                 if self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE) and bool(df["UT_Buy"].iloc[j]) and (bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])):
#                     results.append(self._package_result(t, df, j)); break
#         return self._finalize_and_sort(results)

#     def run_aroon_psar_screener(self):
#         results = []
#         for t, df in self.data_dict.items():
#             if (df := self._prepare_df(df)) is None: continue
#             for j in range(max(1, len(df) - Config.RECENT_BARS), len(df)):
#                 if self.is_aroon_buys(df, j) and self.is_psar_bullish(df, j, require_fresh_crossover=False) and (bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])):
#                     results.append(self._package_result(t, df, j)); break
#         return self._finalize_and_sort(results)


# def add_fundamentals(df):
#     if df is None or df.empty: return df
#     print(f"⏳ Mengambil fundamental untuk {len(df)} saham (menggunakan jeda waktu anti-blokir)...")
#     pers, pbvs = [], []
#     for t in df["Ticker"]:
#         try:
#             time.sleep(0.5) # JEDA WAKTU DITAMBAHKAN
#             info = yf.Ticker(t).info
#             per = info.get('trailingPE') or info.get('forwardPE', 'N/A')
#             pbv = info.get('priceToBook', 'N/A')
#             pers.append(round(per, 2) if isinstance(per, (int, float)) else per)
#             pbvs.append(round(pbv, 2) if isinstance(pbv, (int, float)) else pbv)
#         except Exception:
#             pers.append('N/A'); pbvs.append('N/A')
#     df_copy = df.copy()
#     df_copy["PER"], df_copy["PBV"] = pers, pbvs
#     return df_copy


# def send_telegram_message(data_dict, date_str):
#     bot_token = os.environ.get('lilili')
#     chat_id = os.environ.get('lalala')
#     if not bot_token or not chat_id:
#         print("⚠️ Token/Chat ID Telegram tidak ada. Melewati pengiriman pesan.")
#         return

#     def get_tickers(lst): return ", ".join([item["Ticker"] for item in lst]) if lst else "Tidak ada"

#     msg = f"<b>🚀 Hasil Screener Saham IDX - {date_str}</b>\n\n"
#     msg += f"<b>🏆 Super Screener:</b>\n{get_tickers(data_dict['super_screener'])}\n\n"
#     msg += f"<b>🎯 Aroon + UT:</b>\n{get_tickers(data_dict['aroon_ut'])}\n\n"
#     msg += f"<b>🔥 KO + UT + Vol:</b>\n{get_tickers(data_dict['ko_ut_vol'])}\n\n"
#     msg += f"<b>⚡ Aroon + PSAR:</b>\n{get_tickers(data_dict['aroon_psar'])}\n\n"
#     msg += f"<a href='https://badrut25.github.io/idx-screener-v1/'>Buka Dashboard Web</a>"

#     try:
#         res = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={"chat_id": chat_id, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": True})
#         print("✅ Pesan Telegram berhasil dikirim!" if res.status_code == 200 else f"❌ Gagal Telegram: {res.text}")
#     except Exception as e:
#         print(f"❌ Error Telegram: {e}")

# if __name__ == "__main__":
#     fetcher = StockDataFetcher(Config.TICKERS, Config.MARKET_SUFFIX, Config.LOOKBACK_DAYS_HISTORY)
#     data_storage = fetcher.fetch()
#     screener = ScreenerEngine(data_storage)

#     res_super = add_fundamentals(screener.run_super_screener())
#     res_aroon_ut = add_fundamentals(screener.run_aroon_ut_screener())
#     res_ko_ut = add_fundamentals(screener.run_ko_ut_vol_screener())
#     res_aroon_psar = add_fundamentals(screener.run_aroon_psar_screener())

#     os.makedirs('docs', exist_ok=True)

#     # =====================================================================
#     # PERBAIKAN LOGIKA TANGGAL: Ambil dari Data Market, BUKAN Jam Server
#     # =====================================================================
#     # 1. Cari tanggal terakhir dari data saham yang berhasil di-download
#     last_dates = [df.index[-1] for df in data_storage.values() if not df.empty]
#     if last_dates:
#         market_date = max(last_dates)
#         today_str = market_date.strftime("%Y-%m-%d")
#     else:
#         wib_tz = timezone(timedelta(hours=7))
#         today_str = datetime.now(wib_tz).strftime("%Y-%m-%d")

#     # 2. Waktu update terakhir (tulisan di web) tetap pakai jam saat robot jalan
#     wib_tz = timezone(timedelta(hours=7))
#     timestamp_str = datetime.now(wib_tz).strftime("%Y-%m-%d %H:%M:%S WIB")
#     # =====================================================================

#     export_data = {
#         "last_update": timestamp_str,
#         "super_screener": res_super.to_dict(orient="records") if not res_super.empty else [],
#         "aroon_ut": res_aroon_ut.to_dict(orient="records") if not res_aroon_ut.empty else [],
#         "ko_ut_vol": res_ko_ut.to_dict(orient="records") if not res_ko_ut.empty else [],
#         "aroon_psar": res_aroon_psar.to_dict(orient="records") if not res_aroon_psar.empty else []
#     }

#     # Simpan file menggunakan tanggal market yang AKURAT
#     with open(f'docs/data_{today_str}.json', 'w') as f: json.dump(export_data, f, default=str)
#     with open('docs/data.json', 'w') as f: json.dump(export_data, f, default=str)

#     history_files = glob.glob('docs/data_*.json')
#     available_dates = [os.path.basename(f).replace('data_', '').replace('.json', '') for f in history_files]
    
#     # Hapus duplikat dan urutkan
#     available_dates = list(set(available_dates))
#     available_dates.sort(reverse=True)

#     with open('docs/history_list.json', 'w') as f: json.dump(available_dates, f)
        
#     print(f"✅ Data market tanggal {today_str} berhasil diekspor!")
#     send_telegram_message(export_data, today_str)

# # if __name__ == "__main__":
# #     fetcher = StockDataFetcher(Config.TICKERS, Config.MARKET_SUFFIX, Config.LOOKBACK_DAYS_HISTORY)
# #     data_storage = fetcher.fetch()
# #     screener = ScreenerEngine(data_storage)

# #     res_super = add_fundamentals(screener.run_super_screener())
# #     res_aroon_ut = add_fundamentals(screener.run_aroon_ut_screener())
# #     res_ko_ut = add_fundamentals(screener.run_ko_ut_vol_screener())
# #     res_aroon_psar = add_fundamentals(screener.run_aroon_psar_screener())

# #     os.makedirs('docs', exist_ok=True)

# #     # KUNCI ZONA WAKTU WIB (Menghindari bias server GitHub UTC)
# #     wib_tz = timezone(timedelta(hours=7))
# #     now_wib = datetime.now(wib_tz)
# #     today_str = now_wib.strftime("%Y-%m-%d")
# #     timestamp_str = now_wib.strftime("%Y-%m-%d %H:%M:%S WIB")

# #     export_data = {
# #         "last_update": timestamp_str,
# #         "super_screener": res_super.to_dict(orient="records") if not res_super.empty else [],
# #         "aroon_ut": res_aroon_ut.to_dict(orient="records") if not res_aroon_ut.empty else [],
# #         "ko_ut_vol": res_ko_ut.to_dict(orient="records") if not res_ko_ut.empty else [],
# #         "aroon_psar": res_aroon_psar.to_dict(orient="records") if not res_aroon_psar.empty else []
# #     }

# #     with open(f'docs/data_{today_str}.json', 'w') as f: json.dump(export_data, f, default=str)
# #     with open('docs/data.json', 'w') as f: json.dump(export_data, f, default=str)

# #     history_files = glob.glob('docs/data_*.json')
# #     available_dates = [os.path.basename(f).replace('data_', '').replace('.json', '') for f in history_files]
# #     available_dates.sort(reverse=True)

# #     with open('docs/history_list.json', 'w') as f: json.dump(available_dates, f)
        
# #     print(f"✅ Data tanggal {today_str} berhasil diekspor!")
# #     send_telegram_message(export_data, today_str)
