import streamlit as st

st.set_page_config(page_title="Kalkulator Trading Crypto", layout="centered")

st.title("📊 Kalkulator")
st.write("Hitung jumlah token, Take Profit (TP), Stop Loss (SL), dan estimasi profit/loss.")

# Pilihan jenis modal
modal_type = st.radio("Pilih jenis modal:", ["Rupiah (IDR)", "USDT"])

# Input umum
harga_usdt = st.number_input("💵 Harga 1 USDT ke Rupiah", min_value=0.0, value=16343.0)
#harga_beli = st.number_input("📈 Harga beli token (USDT)", min_value=0.0)
harga_beli = st.number_input(
    "📈 Harga beli token (USDT)",
    min_value=0.0,
    format="%.10f",
    step=0.00000001
)
target_profit_pct = st.number_input("🎯 Target profit (%)", min_value=0.0, value=5.0)
stop_loss_pct = st.number_input("⚠️ Stop loss (%)", min_value=0.0, value=3.0)

# Input modal sesuai pilihan
if modal_type == "Rupiah (IDR)":
    modal_rp = st.number_input("💰 Modal dalam Rupiah (IDR)", min_value=0.0, step=10000.0)
    modal_usdt = modal_rp / harga_usdt if harga_usdt > 0 else 0.0
else:
    modal_usdt = st.number_input("💰 Modal dalam USDT", min_value=0.0)
    modal_rp = modal_usdt * harga_usdt

if st.button("🔍 Hitung"):
    if harga_beli == 0 or harga_usdt == 0:
        st.warning("Harga beli dan harga USDT tidak boleh nol.")
    else:
        jumlah_token = modal_usdt / harga_beli

        harga_tp = harga_beli * (1 + target_profit_pct / 100)
        harga_sl = harga_beli * (1 - stop_loss_pct / 100)

        nilai_tp_usdt = jumlah_token * harga_tp
        nilai_tp_rp = nilai_tp_usdt * harga_usdt
        profit_rp = nilai_tp_rp - modal_rp

        nilai_sl_usdt = jumlah_token * harga_sl
        nilai_sl_rp = nilai_sl_usdt * harga_usdt
        loss_rp = modal_rp - nilai_sl_rp

        st.success("✅ Hasil Perhitungan")
        st.write(f"**Modal awal:** Rp {modal_rp:,.0f} (≈ {modal_usdt:.4f} USDT)")
        st.write(f"**Jumlah token yang dibeli:** `{jumlah_token:.6f}`")
        st.write(f"**Harga Take Profit (TP):** `{harga_tp:.6f}` USDT")
        st.write(f"**Harga Stop Loss (SL):** `{harga_sl:.6f}` USDT")
        st.write(f"**Estimasi keuntungan (TP):** `Rp {profit_rp:,.0f}`")
        st.write(f"**Estimasi kerugian (SL):** `Rp {loss_rp:,.0f}`")
