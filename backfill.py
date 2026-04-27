import os
import json
import glob
from datetime import datetime
import pandas as pd

# Kita 'meminjam' mesin yang sudah ada di screener.py
from screener import StockDataFetcher, ScreenerEngine, Config, add_fundamentals

if __name__ == "__main__":
    print("🚀 Memulai Mesin Waktu: Mengunduh data 400 hari ke belakang...")
    fetcher = StockDataFetcher(Config.TICKERS, Config.MARKET_SUFFIX, Config.LOOKBACK_DAYS_HISTORY)
    full_data = fetcher.fetch()

    os.makedirs('docs', exist_ok=True)

    # 40 hari bursa = kurang lebih 2 bulan kalender. Silakan ubah angka ini sesuai kebutuhan.
    DAYS_TO_BACKFILL = 6
    all_generated_dates = set()

    for offset in range(DAYS_TO_BACKFILL, -1, -1):
        sliced_data = {}
        target_date_str = None

        for t, df in full_data.items():
            # Memotong data seolah-olah kita sedang berada di masa lalu
            if offset == 0:
                df_slice = df.copy()
            else:
                df_slice = df.iloc[:-offset].copy()

            if not df_slice.empty:
                sliced_data[t] = df_slice
                # Ambil tanggal terakhir dari potongan data ini
                if target_date_str is None:
                    target_date_str = df_slice.index[-1].strftime("%Y-%m-%d")

        if not target_date_str:
            continue

        print(f"⏳ Menjalankan screener untuk tanggal: {target_date_str} (Mundur {offset} hari)")

        # Masukkan data masa lalu ke dalam mesin Screener
        screener = ScreenerEngine(sliced_data)
        
        # === TAMBAHAN BARU: EKSEKUSI LORENTZIAN ===
        res_lorentzian = add_fundamentals(screener.run_lorentzian_ml_screener())
        
        res_super = add_fundamentals(screener.run_super_screener())
        res_aroon_ut = add_fundamentals(screener.run_aroon_ut_screener())
        res_ko_ut = add_fundamentals(screener.run_ko_ut_vol_screener())
        res_aroon_psar = add_fundamentals(screener.run_aroon_psar_screener())

        # Bungkus hasilnya (Termasuk data Lorentzian)
        export_data = {
            "last_update": f"{target_date_str} 17:00:00 WIB (Backfilled)",
            "lorentzian_ml": res_lorentzian.to_dict(orient="records") if not res_lorentzian.empty else [],
            "super_screener": res_super.to_dict(orient="records") if not res_super.empty else [],
            "aroon_ut": res_aroon_ut.to_dict(orient="records") if not res_aroon_ut.empty else [],
            "ko_ut_vol": res_ko_ut.to_dict(orient="records") if not res_ko_ut.empty else [],
            "aroon_psar": res_aroon_psar.to_dict(orient="records") if not res_aroon_psar.empty else []
        }

        # Simpan ke JSON khusus tanggal tersebut
        with open(f'docs/data_{target_date_str}.json', 'w') as f:
            json.dump(export_data, f, default=str)

        all_generated_dates.add(target_date_str)

        # Jika ini adalah perulangan terakhir (offset 0 / hari ini), jadikan data utama
        if offset == 0:
            with open('docs/data.json', 'w') as f:
                json.dump(export_data, f, default=str)

    # Memperbarui history_list.json agar web mendeteksinya
    history_files = glob.glob('docs/data_*.json')
    available_dates = []
    for file in history_files:
        base_name = os.path.basename(file)
        date_part = base_name.replace('data_', '').replace('.json', '')
        available_dates.append(date_part)

    available_dates.sort(reverse=True)

    with open('docs/history_list.json', 'w') as f:
        json.dump(available_dates, f)

    print(f"\n✅ SELESAI! Berhasil menyuntikkan data masa lalu sebanyak {len(all_generated_dates)} hari.")

# import os
# import json
# import glob
# from datetime import datetime
# import pandas as pd

# # Kita 'meminjam' mesin yang sudah ada di screener.py
# from screener import StockDataFetcher, ScreenerEngine, Config, add_fundamentals

# if __name__ == "__main__":
#     print("🚀 Memulai Mesin Waktu: Mengunduh data 400 hari ke belakang...")
#     fetcher = StockDataFetcher(Config.TICKERS, Config.MARKET_SUFFIX, Config.LOOKBACK_DAYS_HISTORY)
#     full_data = fetcher.fetch()

#     os.makedirs('docs', exist_ok=True)

#     # 40 hari bursa = kurang lebih 2 bulan kalender
#     DAYS_TO_BACKFILL = 6
#     all_generated_dates = set()

#     for offset in range(DAYS_TO_BACKFILL, -1, -1):
#         sliced_data = {}
#         target_date_str = None

#         for t, df in full_data.items():
#             # Memotong data seolah-olah kita sedang berada di masa lalu
#             if offset == 0:
#                 df_slice = df.copy()
#             else:
#                 df_slice = df.iloc[:-offset].copy()

#             if not df_slice.empty:
#                 sliced_data[t] = df_slice
#                 # Ambil tanggal terakhir dari potongan data ini
#                 if target_date_str is None:
#                     target_date_str = df_slice.index[-1].strftime("%Y-%m-%d")

#         if not target_date_str:
#             continue

#         print(f"⏳ Menjalankan screener untuk tanggal: {target_date_str} (Mundur {offset} hari)")

#         # # Masukkan data masa lalu ke dalam mesin Screener
#         # screener = ScreenerEngine(sliced_data)
#         # res_super = screener.run_super_screener()
#         # res_aroon_ut = screener.run_aroon_ut_screener()
#         # res_ko_ut = screener.run_ko_ut_vol_screener()
#         # res_aroon_psar = screener.run_aroon_psar_screener()

#         # Masukkan data masa lalu ke dalam mesin Screener
#         screener = ScreenerEngine(sliced_data)
#         res_super = add_fundamentals(screener.run_super_screener())
#         res_aroon_ut = add_fundamentals(screener.run_aroon_ut_screener())
#         res_ko_ut = add_fundamentals(screener.run_ko_ut_vol_screener())
#         res_aroon_psar = add_fundamentals(screener.run_aroon_psar_screener())

#         # Bungkus hasilnya
#         export_data = {
#             "last_update": f"{target_date_str} 17:00:00 WIB (Backfilled)",
#             "super_screener": res_super.to_dict(orient="records") if not res_super.empty else [],
#             "aroon_ut": res_aroon_ut.to_dict(orient="records") if not res_aroon_ut.empty else [],
#             "ko_ut_vol": res_ko_ut.to_dict(orient="records") if not res_ko_ut.empty else [],
#             "aroon_psar": res_aroon_psar.to_dict(orient="records") if not res_aroon_psar.empty else []
#         }

#         # Simpan ke JSON khusus tanggal tersebut
#         with open(f'docs/data_{target_date_str}.json', 'w') as f:
#             json.dump(export_data, f, default=str)

#         all_generated_dates.add(target_date_str)

#         # Jika ini adalah perulangan terakhir (offset 0 / hari ini), jadikan data utama
#         if offset == 0:
#             with open('docs/data.json', 'w') as f:
#                 json.dump(export_data, f, default=str)

#     # Memperbarui history_list.json agar web mendeteksinya
#     history_files = glob.glob('docs/data_*.json')
#     available_dates = []
#     for file in history_files:
#         base_name = os.path.basename(file)
#         date_part = base_name.replace('data_', '').replace('.json', '')
#         available_dates.append(date_part)

#     available_dates.sort(reverse=True)

#     with open('docs/history_list.json', 'w') as f:
#         json.dump(available_dates, f)

#     print(f"\n✅ SELESAI! Berhasil menyuntikkan data masa lalu sebanyak {len(all_generated_dates)} hari.")
