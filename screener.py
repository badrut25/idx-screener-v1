# @title OOP Complete Suite: 3 Screeners + 3 Backtesters (Chunking & Auto-Update)- pake ini ya
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta, date
from tabulate import tabulate  # <--- INI BARIS YANG HILANG SEBELUMNYA

# ==============================================================================
# 1. CONFIGURATION
# ==============================================================================
class Config:
    # --- Ticker List ---
    TICKERS1 = [
        "AALI", "ABBA", "ACES", "ADRO", "AGII", "AKRA", "AMRT", "ANTM", "APLN",
        "ARTO", "ASII", "ASRI", "BBCA", "BBNI", "BBRI", "BBTN", "BDMN", "BEST",
        "BFIN", "BMRI", "BRIS", "BRPT", "BSDE", "BTPS", "BUMI", "BYAN", "CPIN",
        "CTRA", "DILD", "DMAS", "ELSA", "EMTK", "ENRG", "ERAA", "EXCL", "GGRM",
        "GOTO", "HRUM", "ICBP", "INCO", "INDF", "INKP", "INTP", "ISAT", "ITMG",
        "JPFA", "JSMR", "KLBF", "MAPI", "MDKA", "MEDC", "MIKA", "MNCN", "MTEL",
        "MYOR", "PGAS", "PTBA", "PTPP", "PWON", "SCMA", "SIDO", "SMGR", "SMRA",
        "SRTG", "TBIG", "TINS", "TKIM", "TLKM", "TOWR", "TPIA", "UNTR", "UNVR",
        "WIKA", "WSKT", "BELI", "BUKA", "PADA", "GPRA", "BSML", "CITY", "FREN",
        "DEWA", "BREN", "CUAN", "STRK", "BRAND", "GOLA", "CARE"
    ]
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

    # --- Time Settings ---
    # 400 hari agar backtest punya data history yang cukup
    LOOKBACK_DAYS_HISTORY = 400

    # --- Logic Settings ---
    RECENT_BARS = 2          # Window pengecekan sinyal (Screener)
    BACKTEST_WINDOW = 60     # Cek sinyal dalam 60 hari terakhir (Backtest)
    HORIZONS = [3, 5, 10, 20] # Target hold hari untuk Backtest

    # --- Indicator Params ---
    AROON_LEN = 8

    KLINGER_FAST = 34
    KLINGER_SLOW = 55
    KLINGER_SIG = 13
    KLINGER_TRIG = 13

    MACD_FAST = 12
    MACD_SLOW = 26
    MACD_SIG = 9

    UT_A = 1.0
    UT_C = 10

    ST_PERIOD = 10
    ST_MULT = 3.0

    # --- Filters ---
    REQUIRE_KO_POSITIVE = False
    REQUIRE_HIST_RISING = False

    USE_VOLUME_FILTER = True
    VOL_MA = 20
    VOL_MULT = 1.5
    MIN_VOL = 500_000

    # --- PSAR Params ---
    PSAR_START = 0.02
    PSAR_INC = 0.02
    PSAR_MAX = 0.2

# ==============================================================================
# 2. DATA FETCHER (Chunking)
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
            # print(f"   > Batch {i+1} - {min(i+chunk_size, len(self.tickers))}...")

            try:
                data = yf.download(
                    tickers=" ".join(batch),
                    start=self.start_date,
                    end=None,
                    interval="1d",
                    group_by="ticker",
                    auto_adjust=False,
                    threads=True,
                    progress=False
                )

                if data.empty: continue

                # Parsing MultiIndex
                if len(batch) == 1:
                    clean_name = batch[0].replace(".JK", "")
                    all_dfs[clean_name] = data
                else:
                    for t in batch:
                        if t in data.columns.levels[0]:
                            clean_name = t.replace(".JK", "")
                            df_t = data[t].copy()
                            df_t.dropna(how='all', inplace=True)
                            if not df_t.empty:
                                all_dfs[clean_name] = df_t

            except Exception as e:
                print(f"   ⚠️ Error batch: {e}")
                continue

        print(f"✅ Selesai. Dapat {len(all_dfs)} ticker valid.\n")
        return all_dfs

# ==============================================================================
# REVISI: TECHNICAL INDICATORS (Fix UT Bot Index Bug)
# ==============================================================================
class TechnicalIndicators:
    # ... (Metode wilder_rma, compute_true_range, klinger, aroon, macd SAMA SEPERTI SEBELUMNYA)
    # Tulis ulang saja agar lengkap, atau pastikan add_ut_bot diganti:

    @staticmethod
    def wilder_rma(series, period):
        return series.ewm(alpha=1/period, adjust=False).mean()

    @staticmethod
    def compute_true_range(df):
        high, low, close = df["High"], df["Low"], df["Close"]
        prev_close = close.shift(1)
        tr1 = high - low
        tr2 = (high - prev_close).abs()
        tr3 = (low - prev_close).abs()
        return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    @staticmethod
    def add_klinger_pine_exact(df, trig_len=13, fast_x=34, slow_x=55):
        high, low, close, vol = df["High"], df["Low"], df["Close"], df["Volume"]
        hlc3 = (high + low + close) / 3.0
        hlc3_prev = hlc3.shift(1)
        xTrend = np.where(hlc3 > hlc3_prev, vol * 100.0, -vol * 100.0)
        xTrend = pd.Series(xTrend, index=df.index)
        xFast = xTrend.ewm(span=fast_x, adjust=False).mean()
        xSlow = xTrend.ewm(span=slow_x, adjust=False).mean()
        xKVO = xFast - xSlow
        xTrigger = xKVO.ewm(span=trig_len, adjust=False).mean()
        df["KO"] = xKVO
        df["KO_Signal"] = xTrigger
        return df

    @staticmethod
    def add_aroon_pine_exact(df, length=8):
        highs = df["High"].values
        lows = df["Low"].values
        n = len(df)
        highestbars_list = np.full(n, np.nan)
        lowestbars_list = np.full(n, np.nan)
        for i in range(length, n):
            window_high = highs[i - length : i + 1]
            window_low = lows[i - length : i + 1]
            highestbars_list[i] = np.argmax(window_high) - length
            lowestbars_list[i] = np.argmin(window_low) - length
        df["Aroon_Up"] = 100.0 * (highestbars_list + length) / length
        df["Aroon_Down"] = 100.0 * (lowestbars_list + length) / length
        return df

    @staticmethod
    def add_macd(df, fast=12, slow=26, signal=9):
        src = df["Close"]
        fast_ma = src.ewm(span=fast, adjust=False).mean()
        slow_ma = src.ewm(span=slow, adjust=False).mean()
        macd = fast_ma - slow_ma
        sig = macd.ewm(span=signal, adjust=False).mean()
        df["MACD"] = macd
        df["MACD_Signal"] = sig
        df["MACD_Hist"] = macd - sig
        return df

    # === BAGIAN YANG DIPERBAIKI (BUG FIX) ===
    @staticmethod
    def add_ut_bot(df, a=1.0, c=10):
        close = df["Close"]
        tr = TechnicalIndicators.compute_true_range(df)
        xATR = TechnicalIndicators.wilder_rma(tr, c)
        nLoss = a * xATR
        src_ut = close

        xATRTrailingStop = np.zeros(len(df))
        pos = np.zeros(len(df), dtype=int)
        src_val = src_ut.values
        nLoss_val = nLoss.values

        for i in range(1, len(df)):
            prev_stop = xATRTrailingStop[i-1]
            price = src_val[i]
            loss = nLoss_val[i]
            if (src_val[i-1] > prev_stop) and (price > prev_stop):
                xATRTrailingStop[i] = max(prev_stop, price - loss)
            elif (src_val[i-1] < prev_stop) and (price < prev_stop):
                xATRTrailingStop[i] = min(prev_stop, price + loss)
            elif price > prev_stop:
                xATRTrailingStop[i] = price - loss
            else:
                xATRTrailingStop[i] = price + loss

        for i in range(1, len(df)):
            price = src_val[i]
            prev_stop = xATRTrailingStop[i-1]
            prev_pos = pos[i-1]
            if (src_val[i-1] < prev_stop) and (price > prev_stop):
                pos[i] = 1
            elif (src_val[i-1] > prev_stop) and (price < prev_stop):
                pos[i] = -1
            else:
                pos[i] = prev_pos

        df["UT_Stop"] = xATRTrailingStop
        df["UT_Pos"] = pos

        # PERBAIKAN: Gunakan shift pada kolom DataFrame, bukan pada list/numpy array
        # Agar index tanggal tetap sinkron.
        df["UT_Buy"] = (df["UT_Pos"] == 1) & (df["UT_Pos"].shift(1) != 1)
        return df

    @staticmethod
    def add_supertrend(df, period=10, multiplier=3.0):
        high, low, close = df["High"], df["Low"], df["Close"]
        src = (high + low) / 2.0
        tr = TechnicalIndicators.compute_true_range(df)
        atr = TechnicalIndicators.wilder_rma(tr, period)
        up = src - (multiplier * atr)
        dn = src + (multiplier * atr)
        st = np.zeros(len(df))
        trend = np.zeros(len(df), dtype=int)
        up_val, dn_val, close_val = up.values, dn.values, close.values
        st[0] = up_val[0]; trend[0] = 1

        for i in range(1, len(df)):
            prev_st = st[i-1]
            if close_val[i-1] > st[i-1] and trend[i-1] == 1: curr_up = max(up_val[i], st[i-1])
            else: curr_up = up_val[i]
            if close_val[i-1] < st[i-1] and trend[i-1] == -1: curr_dn = min(dn_val[i], st[i-1])
            else: curr_dn = dn_val[i]

            prev_trend = trend[i-1]
            if prev_trend == -1 and close_val[i] > prev_st: trend[i] = 1; st[i] = curr_up
            elif prev_trend == 1 and close_val[i] < prev_st: trend[i] = -1; st[i] = curr_dn
            else: trend[i] = prev_trend; st[i] = curr_up if trend[i] == 1 else curr_dn

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
        high = df['High'].values
        low = df['Low'].values
        length = len(df)

        psar = np.zeros(length)
        psar_trend = np.zeros(length, dtype=int) # 1 untuk Bullish, -1 untuk Bearish

        if length == 0:
            return df

        bull = True
        af = start
        hp = high[0]
        lp = low[0]
        psar[0] = low[0]

        for i in range(1, length):
            prev_psar = psar[i-1]

            if bull:
                psar[i] = prev_psar + af * (hp - prev_psar)
                psar[i] = min(psar[i], low[i-1])
                if i > 1:
                    psar[i] = min(psar[i], low[i-2])

                # Cek Reversal
                if low[i] < psar[i]:
                    bull = False
                    psar[i] = hp
                    hp = high[i]
                    lp = low[i]
                    af = start
                else:
                    if high[i] > hp:
                        hp = high[i]
                        af = min(af + increment, maximum)
            else:
                psar[i] = prev_psar + af * (lp - prev_psar)
                psar[i] = max(psar[i], high[i-1])
                if i > 1:
                    psar[i] = max(psar[i], high[i-2])

                # Cek Reversal
                if high[i] > psar[i]:
                    bull = True
                    psar[i] = lp
                    hp = high[i]
                    lp = low[i]
                    af = start
                else:
                    if low[i] < lp:
                        lp = low[i]
                        af = min(af + increment, maximum)

            psar_trend[i] = 1 if bull else -1

        df["PSAR"] = psar
        df["PSAR_Trend"] = psar_trend
        df["PSAR_Buy"] = (df["PSAR_Trend"] == 1) & (df["PSAR_Trend"].shift(1) == -1)

        return df

# ==============================================================================
# 4. SIGNAL CHECKERS (Mixin)
#    Dipakai bersama oleh Screener dan Backtester
# ==============================================================================
class SignalLogic:
    def is_aroon_buys(self, df, j):
        if j <= 0: return False
        return (df["Aroon_Up"].iloc[j-1] <= df["Aroon_Down"].iloc[j-1]) and \
               (df["Aroon_Up"].iloc[j] > df["Aroon_Down"].iloc[j])

    def is_ko_bullish(self, df, j, require_pos=True):
        if j <= 0: return False
        cross_up = (df["KO"].iloc[j-1] <= df["KO_Signal"].iloc[j-1]) and \
                   (df["KO"].iloc[j] > df["KO_Signal"].iloc[j])
        if not cross_up: return False
        if require_pos and df["KO"].iloc[j] <= 0: return False
        return True

    def is_macd_bullish(self, df, j, require_rising=False):
        if j <= 0: return False
        hist = df["MACD_Hist"].iloc[j]
        if hist <= 0: return False
        if require_rising and hist <= df["MACD_Hist"].iloc[j-1]: return False
        return True

    def is_psar_bullish(self, df, j, require_fresh_crossover=False):
        if j <= 0: return False
        # Jika True, hanya ambil saat HARI INI persis titik PSAR pindah ke bawah candle (Buy Signal)
        if require_fresh_crossover:
            return bool(df["PSAR_Buy"].iloc[j])
        # Jika False, asalkan titik PSAR ada di bawah candle (sedang trend naik), return True
        return df["PSAR_Trend"].iloc[j] == 1

# ==============================================================================
# REVISI FINAL: SCREENER ENGINE (Sorted Newest -> Oldest)
# ==============================================================================
class ScreenerEngine(SignalLogic):
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def _prepare_df(self, df):
        if len(df) < 50: return None
        df = df.copy()
        # Hitung indikator
        df = TechnicalIndicators.add_klinger_pine_exact(df, Config.KLINGER_TRIG, Config.KLINGER_FAST, Config.KLINGER_SLOW)
        df = TechnicalIndicators.add_aroon_pine_exact(df, Config.AROON_LEN)
        df = TechnicalIndicators.add_macd(df, Config.MACD_FAST, Config.MACD_SLOW, Config.MACD_SIG)
        df = TechnicalIndicators.add_volume_filters(df, Config.VOL_MA, Config.VOL_MULT, Config.MIN_VOL)
        df = TechnicalIndicators.add_ut_bot(df, Config.UT_A, Config.UT_C)
        df = TechnicalIndicators.add_supertrend(df, Config.ST_PERIOD, Config.ST_MULT)
        df = TechnicalIndicators.add_psar(df, Config.PSAR_START, Config.PSAR_INC, Config.PSAR_MAX)
        df.dropna(inplace=True)
        return df

    def classify_pattern(self, row):
        st_trend = row.get("ST_Trend", 0)
        st_buy   = row.get("ST_Buy", False)
        ut_pos   = row.get("UT_Pos", 0)
        vol_spike = row.get("Volume_Spike", False)
        pct_price = row.get("Pct_Change_Price", 0)

        if st_trend == 1 and ut_pos == 1 and vol_spike and pct_price < 12: return "RUNNER"
        if ut_pos == 1 and vol_spike and pct_price >= 5: return "POP_CEPAT"
        if st_trend == -1: return "NOISE_TRAP"
        return "UNCLASSIFIED"

    def _package_result(self, t, df, j):
        row = df.iloc[j]
        prev = df.iloc[j-1]
        res = {
            "Ticker": t,
            "Signal_Date": row.name.date(),
            "Bars_Ago": len(df) - 1 - j,
            "Open": int(row["Open"]),
            "Close": int(row["Close"]),
            "Pct_Change_Price": round((row["Close"]-prev["Close"])/prev["Close"]*100, 2),
            "Volume": int(row["Volume"]),
            "Volume_Spike": bool(row["Volume_Spike"]),
            "KO": round(row["KO"], 2),
            "UT_Buy": bool(row["UT_Buy"]),
            "ST_Trend": int(row["ST_Trend"]),
            "Aroon_Up": round(row["Aroon_Up"], 1),
            "UT_Pos": int(row["UT_Pos"]),
            "PSAR_Trend": "Bull" if row["PSAR_Trend"] == 1 else "Bear" # <--- Tambahan
        }
        res["Pattern_Label"] = self.classify_pattern(res)
        return res

    # --- HELPER BARU: SORTING OUTPUT ---
    def _finalize_and_sort(self, results):
        df = pd.DataFrame(results)
        if df.empty: return df

        # LOGIKA SORTING:
        # 1. Signal_Date Descending (Terbaru di atas)
        # 2. Volume_Spike Descending (True di atas)
        # 3. Pct_Change_Price Descending (Kenaikan tertinggi di atas)
        df = df.sort_values(
            by=["Signal_Date", "Volume_Spike", "Pct_Change_Price"],
            ascending=[False, False, False]
        ).reset_index(drop=True)
        return df

    # --- 1. SUPER SCREENER ---
    def run_super_screener(self):
        print("\n🔎 Running SUPER SCREENER...")
        results = []
        for t, df in self.data_dict.items():
            df = self._prepare_df(df)
            if df is None: continue

            last_idx = len(df) - 1
            j_start = max(1, last_idx - Config.RECENT_BARS + 1)

            for j in range(j_start, last_idx + 1):
                c_aroon = self.is_aroon_buys(df, j)
                c_ko = self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE)
                c_macd = self.is_macd_bullish(df, j, Config.REQUIRE_HIST_RISING)
                c_ut_trend = (df["UT_Pos"].iloc[j] == 1)
                c_vol = True
                if Config.USE_VOLUME_FILTER:
                    c_vol = bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])

                if c_aroon and c_ko and c_macd and c_ut_trend and c_vol:
                    results.append(self._package_result(t, df, j))
                    break

        return self._finalize_and_sort(results)

    # --- 2. AROON + UT SCREENER ---
    def run_aroon_ut_screener(self):
        print("\n🔎 Running AROON + UT SCREENER...")
        results = []
        for t, df in self.data_dict.items():
            df = self._prepare_df(df)
            if df is None: continue

            last_idx = len(df) - 1
            j_start = max(1, last_idx - Config.RECENT_BARS + 1)

            for j in range(j_start, last_idx + 1):
                c_aroon = self.is_aroon_buys(df, j)
                c_ut = bool(df["UT_Buy"].iloc[j])

                if c_aroon and c_ut:
                    results.append(self._package_result(t, df, j))
                    break

        return self._finalize_and_sort(results)

    # --- 3. KO + UT + VOLUME SCREENER ---
    def run_ko_ut_vol_screener(self):
        print("\n🔎 Running KO + UT + VOLUME SCREENER...")
        results = []
        for t, df in self.data_dict.items():
            df = self._prepare_df(df)
            if df is None: continue

            last_idx = len(df) - 1
            j_start = max(1, last_idx - Config.RECENT_BARS + 1)

            for j in range(j_start, last_idx + 1):
                c_ko = self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE)
                c_ut = bool(df["UT_Buy"].iloc[j])
                c_vol = True
                if Config.USE_VOLUME_FILTER:
                    c_vol = bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])

                if c_ko and c_ut and c_vol:
                    results.append(self._package_result(t, df, j))
                    break

        return self._finalize_and_sort(results)

    # --- 4. AROON + PSAR SCREENER ---
    def run_aroon_psar_screener(self):
        print("\n🔎 Running AROON + PSAR SCREENER...")
        results = []
        for t, df in self.data_dict.items():
            df = self._prepare_df(df)
            if df is None: continue

            last_idx = len(df) - 1
            j_start = max(1, last_idx - Config.RECENT_BARS + 1)

            for j in range(j_start, last_idx + 1):
                # Kriteria 1: Aroon Cross Up (Aroon Up memotong ke atas Aroon Down)
                c_aroon = self.is_aroon_buys(df, j)

                # Kriteria 2: PSAR sedang Bullish (titik berada di bawah harga)
                # Gunakan require_fresh_crossover=True jika Anda ingin mencari SAAT INI titik berbalik
                c_psar = self.is_psar_bullish(df, j, require_fresh_crossover=False)

                c_vol = True
                if Config.USE_VOLUME_FILTER:
                    c_vol = bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])

                if c_aroon and c_psar and c_vol:
                    results.append(self._package_result(t, df, j))
                    break

        return self._finalize_and_sort(results)

# ==============================================================================
# REVISI FINAL: BACKTEST ENGINE (Sorted Output)
# ==============================================================================
class BacktestEngine(ScreenerEngine):
    def _calculate_forward_returns(self, df, entry_idx, entry_price):
        res = {}
        for h in Config.HORIZONS:
            exit_idx = entry_idx + h
            if exit_idx < len(df):
                exit_price = df["Close"].iloc[exit_idx]
                pct = (exit_price - entry_price) / entry_price * 100
                res[f"Ret_{h}d"] = round(pct, 2)
            else:
                res[f"Ret_{h}d"] = np.nan
        return res

    def _generic_backtest_loop(self, signal_check_func, title):
        print(f"\n🧪 Backtesting: {title}")
        trades = []

        for t, df in self.data_dict.items():
            df = self._prepare_df(df)
            if df is None: continue

            last_idx = len(df) - 1
            start_scan = max(1, last_idx - Config.BACKTEST_WINDOW)

            for j in range(start_scan, last_idx):
                if signal_check_func(df, j):
                    entry_price = df["Close"].iloc[j]
                    row_data = {
                        "Ticker": t,
                        "Signal_Date": df.index[j].date(),
                        "Entry_Price": entry_price
                    }
                    returns = self._calculate_forward_returns(df, j, entry_price)
                    row_data.update(returns)
                    trades.append(row_data)

        df_trades = pd.DataFrame(trades)

        # SORTING BACKTEST TRADES LIST (NEWEST FIRST)
        if not df_trades.empty:
            df_trades = df_trades.sort_values(by="Signal_Date", ascending=False).reset_index(drop=True)

        return df_trades

    def summarize_backtest(self, df_trades):
        if df_trades.empty:
            print("   (No trades found)")
            return

        print("\n📊 BACKTEST SUMMARY")
        summary = []
        for h in Config.HORIZONS:
            col = f"Ret_{h}d"
            if col in df_trades.columns:
                valid_trades = df_trades.dropna(subset=[col])
                if valid_trades.empty: continue

                win_rate = (valid_trades[col] > 0).mean() * 100
                avg_ret = valid_trades[col].mean()

                summary.append({
                    "Horizon": f"{h} Days",
                    "Win Rate": f"{win_rate:.1f}%",
                    "Avg Return": f"{avg_ret:.2f}%",
                    "Trades": len(valid_trades)
                })

        df_sum = pd.DataFrame(summary)
        print(df_sum.to_string(index=False))

    # (Method backtest_super, backtest_aroon_ut, dll SAMA SEPERTI SEBELUMNYA)
    def backtest_super(self):
        def check(df, j):
            c_aroon = self.is_aroon_buys(df, j)
            c_ko = self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE)
            c_macd = self.is_macd_bullish(df, j, Config.REQUIRE_HIST_RISING)
            c_ut_trend = (df["UT_Pos"].iloc[j] == 1) # Consistency check
            c_vol = True
            if Config.USE_VOLUME_FILTER:
                c_vol = bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])
            return c_aroon and c_ko and c_macd and c_ut_trend and c_vol

        df_trades = self._generic_backtest_loop(check, "Super Screener")
        self.summarize_backtest(df_trades)
        return df_trades

    def backtest_aroon_ut(self):
        def check(df, j):
            return self.is_aroon_buys(df, j) and bool(df["UT_Buy"].iloc[j])
        df_trades = self._generic_backtest_loop(check, "Aroon + UT")
        self.summarize_backtest(df_trades)
        return df_trades

    def backtest_ko_ut_vol(self):
        def check(df, j):
            c_ko = self.is_ko_bullish(df, j, Config.REQUIRE_KO_POSITIVE)
            c_ut = bool(df["UT_Buy"].iloc[j])
            c_vol = True
            if Config.USE_VOLUME_FILTER:
                c_vol = bool(df["Volume_OK"].iloc[j]) and bool(df["Volume_Confirm"].iloc[j])
            return c_ko and c_ut and c_vol

        df_trades = self._generic_backtest_loop(check, "KO + UT + Volume")
        self.summarize_backtest(df_trades)
        return df_trades

# ==============================================================================
# MAIN EXECUTION (DENGAN OUTPUT TABEL RAPI)
# ==============================================================================
def print_pretty(df, title=""):
    """
    Fungsi helper untuk mencetak DataFrame menjadi tabel cantik
    menggunakan library 'tabulate'.
    """
    if title:
        print(f"\n{'='*len(title)}")
        print(f"{title}")
        print(f"{'='*len(title)}")

    if df.empty:
        print(">> Tidak ada hasil (No Results).")
        return

    # Kita convert ke string dulu agar tampilan tanggal rapi
    df_print = df.copy()

    # Format angka float agar tidak terlalu panjang (misal KO)
    # Kolom harga (Open, Close) biarkan integer
    for col in df_print.columns:
        if df_print[col].dtype == 'float64':
            df_print[col] = df_print[col].apply(lambda x: f"{x:.2f}")

    # Cetak tabel dengan format 'psql' (seperti database SQL) atau 'fancy_grid'
    print(tabulate(df_print, headers='keys', tablefmt='psql', showindex=False))

import json
import os

if __name__ == "__main__":
    # 1. Download Data
    fetcher = StockDataFetcher(Config.TICKERS, Config.MARKET_SUFFIX, Config.LOOKBACK_DAYS_HISTORY)
    data_storage = fetcher.fetch()

    # 2. Setup Engines
    screener = ScreenerEngine(data_storage)

    # 3. Jalankan Screener
    res_super = screener.run_super_screener()
    res_aroon_ut = screener.run_aroon_ut_screener()
    res_ko_ut = screener.run_ko_ut_vol_screener()
    res_aroon_psar = screener.run_aroon_psar_screener()

    # 4. Siapkan folder docs (wajib untuk GitHub Pages)
    os.makedirs('docs', exist_ok=True)

    # 5. Gabungkan data ke dalam satu dictionary
    export_data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S WIB"),
        "super_screener": res_super.to_dict(orient="records") if not res_super.empty else [],
        "aroon_ut": res_aroon_ut.to_dict(orient="records") if not res_aroon_ut.empty else [],
        "ko_ut_vol": res_ko_ut.to_dict(orient="records") if not res_ko_ut.empty else [],
        "aroon_psar": res_aroon_psar.to_dict(orient="records") if not res_aroon_psar.empty else []
    }

    # 6. Simpan ke file JSON
    with open('docs/data.json', 'w') as f:
        json.dump(export_data, f, default=str)
        
    print("✅ Data berhasil diekspor ke docs/data.json")

# if __name__ == "__main__":
#     # 1. Download Data
#     fetcher = StockDataFetcher(Config.TICKERS, Config.MARKET_SUFFIX, Config.LOOKBACK_DAYS_HISTORY)
#     data_storage = fetcher.fetch()

#     # 2. Setup Engines
#     screener = ScreenerEngine(data_storage)
#     backtester = BacktestEngine(data_storage)

#     # --- RUN SCREENERS ---

#     # 1. Super Screener
#     res1 = screener.run_super_screener()
#     print_pretty(res1, "HASIL: SUPER SCREENER")

#     # 2. Aroon + UT Screener
#     res2 = screener.run_aroon_ut_screener()
#     print_pretty(res2, "HASIL: AROON + UT SCREENER")

#     # 3. KO + UT + Volume Screener
#     res3 = screener.run_ko_ut_vol_screener()
#     print_pretty(res3, "HASIL: KO + UT + VOLUME SCREENER")

#     # 4. Aroon + PSAR Screener
#     res4 = screener.run_aroon_psar_screener()
#     print_pretty(res4, "HASIL: AROON + PSAR SCREENER")

#     # --- RUN BACKTESTS (Opsional: Tampilkan Tabel Ringkasan) ---
#     # Jika ingin melihat detail trade backtest yang rapi:

#     bt1 = backtester.backtest_super()
#     print_pretty(bt1.head(10), "BACKTEST SAMPLE: SUPER SCREENER (Top 10 Latest)")
