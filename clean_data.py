import argparse
from pathlib import Path
import sys
import pandas as pd


def clean_dataset(input_path, output_path):
    # Konversi string path menjadi objek Path
    input_file = Path(input_path).resolve()

    print(f"=== MEMUAT DATASET ===")
    print(f"Mencoba membaca file dari: {input_file}")

    # Validasi keberadaan file secara dinamis
    if not input_file.exists():
        print(f"[ERROR] File tidak ditemukan di path: {input_file}")
        sys.exit(1)

    if not input_file.is_file():
        print(
            f"[ERROR] Path yang dimasukkan adalah folder, bukan file: {input_file}"
        )
        sys.exit(1)

    try:
        df = pd.read_csv(input_file)
        print(f"[SUKSES] Berhasil memuat {len(df)} baris data.\n")
    except Exception as e:
        print(f"[ERROR] Gagal membaca CSV: {e}")
        sys.exit(1)

    # --- PROSES CLEANING / OLAH DATA DI SINI ---

    # Menentukan lokasi output secara dinamis
    if output_path:
        out_file = Path(output_path).resolve()
    else:
        # Jika output tidak diisi, otomatis buat nama baru di folder yang sama
        out_file = input_file.parent / f"{input_file.stem}_clean.csv"

    # Simpan file hasil
    df.to_csv(out_file, index=False)
    print(f"[SUKSES] File bersih disimpan ke: {out_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Script pembersihan data dengan jalur path dinamis."
    )

    # Argumen dinamis 1: Input Path (Wajib)
    parser.add_argument(
        "input_path",
        type=str,
        help="Path ke file CSV input (bisa relatif seperti ./data.csv atau absolut /home/user/data.csv)",
    )

    # Argumen dinamis 2: Output Path (Opsional)
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Path tujuan penyimpanan file hasil (opsional)",
    )

    args = parser.parse_args()

    clean_dataset(input_path=args.input_path, output_path=args.output)


if __name__ == "__main__":
    main()
