import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Fungsi Midpoint Rule
def midpoint_rule(x, y):
    """
    Menghitung integral menggunakan metode Midpoint Rule.

    Parameters:
        x (array): Array titik-titik pembagi.
        y (array): Array nilai fungsi pada titik-titik pembagi.

    Returns:
        float: Nilai integral yang dihitung.
    """
    n = len(x)
    integral = 0
    for i in range(n - 1):
        midpoint = (x[i] + x[i + 1]) / 2
        integral += (x[i + 1] - x[i]) * np.interp(midpoint, x, y)
    return integral

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Midpoint Rule Calculator",
    page_icon="📈",
    layout="centered",
)

# Header dengan Gambar
st.markdown(
    """
    <style>
    .header {
        background-image: linear-gradient(to right, #4CAF50, #81C784);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
    }
    .header img {
        max-width: 80px;
        margin-bottom: 10px;
    }
    .header h1 {
        font-size: 36px;
        margin: 0;
    }
    .header p {
        font-size: 18px;
        margin: 0;
    }
    </style>
    <div class="header">
        <h1>Midpoint Rule Calculator</h1>
        <p>Hitung integral fungsi dengan metode Midpoint Rule secara instan!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar Input
st.sidebar.title("⚙️ Pengaturan Input")
st.sidebar.write("Masukkan data Anda dengan format yang benar:")
x_input = st.sidebar.text_area(
    "Masukkan nilai x (pisahkan dengan koma):",
    "1, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8",
    help="Nilai titik pembagi pada sumbu x.",
)
y_input = st.sidebar.text_area(
    "Masukkan nilai y (pisahkan dengan koma):",
    "1.449, 2.06, 2.645, 3.216, 3.779, 4.338, 4.898",
    help="Nilai fungsi pada masing-masing titik pembagi x.",
)
st.sidebar.write("---")
calculate = st.sidebar.button("💻 Hitung Integral")

# Kolom untuk Hasil dan Grafik
col1, col2 = st.columns([1, 2])

if calculate:
    try:
        # Proses input data
        x = np.array([float(i) for i in x_input.split(",")])
        y = np.array([float(i) for i in y_input.split(",")])

        if len(x) != len(y):
            col1.error("❌ Panjang array x dan y harus sama.")
        else:
            # Menghitung integral
            result = midpoint_rule(x, y)
            col1.success(f"✅ Nilai integral adalah: {result:.4f}")

            # Visualisasi grafik
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x, y, marker="o", color="#007BFF", label="Data Fungsi")
            ax.fill_between(
                x[:-1],
                y[:-1],
                np.interp((x[:-1] + x[1:]) / 2, x, y),
                color="skyblue",
                alpha=0.5,
                label="Area Integral",
            )
            ax.set_title("Grafik Data dan Area Integral", fontsize=16, color="#333333")
            ax.set_xlabel("x", fontsize=14)
            ax.set_ylabel("y", fontsize=14)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(fontsize=12)
            col2.pyplot(fig)

    except ValueError:
        col1.error("❌ Masukkan nilai yang valid untuk x dan y.")
else:
    st.info("💡 Masukkan data di sidebar dan klik 'Hitung Integral' untuk memulai.")

# Footer dengan Nama Kelompok
st.markdown(
    """
    <style>
    .footer {
        margin-top: 30px;
        padding: 10px 0;
        text-align: center;
        font-size: 14px;
        color: grey;
    }
    .footer h4 {
        margin: 0;
        font-size: 16px;
    }
    .footer ul {
        list-style: none;
        padding: 0;
    }
    .footer ul li {
        margin: 5px 0;
    }
    </style>
    <div class="footer">
        <h4>Dibuat oleh Kelompok:</h4>
        <ul>
            <li>Akbar Prasetyo &nbsp;&nbsp; (22.11.4758)</li>
            <li>F.X Ewang Cita Giya Nusa &nbsp;&nbsp; (22.11.4749)</li>
            <li>Wahyu Septa Pramudya &nbsp;&nbsp; (22.11.4789)</li>
            <li>Fernanda Pandu Jatmika &nbsp;&nbsp; (22.11.4751)</li>
        </ul>
        <p>© 2025 Midpoint Rule Calculator</p>
    </div>
    """,
    unsafe_allow_html=True,
)
