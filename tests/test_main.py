# tests/test_main.py
import pytest
from src.models import Mahasiswa, DaftarMahasiswa


class TestMahasiswa:
    def test_buat_mahasiswa_valid(self):
        mhs = Mahasiswa("2024SI001", "Andi Pratama",
                        "Sistem Informasi", 2024, 3.50)
        assert mhs.nim == "2024SI001"
        assert mhs.ipk == 3.50

    def test_nim_tidak_valid(self):
        with pytest.raises(ValueError):
            Mahasiswa("abc", "Test", "SI", 2024, 3.0)

    def test_ipk_diluar_range(self):
        with pytest.raises(ValueError):
            Mahasiswa("2024SI002", "Test", "SI", 2024, 5.0)

    # --- Tambahan (edge case) ---
    def test_nim_kosong(self):
        with pytest.raises(ValueError):
            Mahasiswa("", "Test", "SI", 2024, 3.0)

    def test_nama_kosong(self):
        with pytest.raises(ValueError):
            Mahasiswa("2024SI003", "", "SI", 2024, 3.0)

    def test_nama_sangat_panjang(self):
        nama = "A" * 200
        mhs = Mahasiswa("2024SI004", nama, "SI", 2024, 3.0)
        assert mhs.nama == nama
        assert nama in str(mhs)

    def test_ipk_boundary_nol(self):
        assert Mahasiswa("2024SI005", "Test", "SI", 2024, 0.0).ipk == 0.0

    def test_ipk_boundary_empat(self):
        assert Mahasiswa("2024SI006", "Test", "SI", 2024, 4.0).ipk == 4.0

    def test_ipk_negatif(self):
        with pytest.raises(ValueError):
            Mahasiswa("2024SI007", "Test", "SI", 2024, -0.1)


class TestDaftarMahasiswa:
    def test_tambah_dan_cari(self):
        db = DaftarMahasiswa()
        mhs = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        db.tambah(mhs)
        assert db.cari("2024SI001") == mhs
        assert db.jumlah == 1

    def test_nim_duplikat(self):
        db = DaftarMahasiswa()
        m1 = Mahasiswa("2024SI001", "Andi", "SI", 2024)
        m2 = Mahasiswa("2024SI001", "Budi", "SI", 2024)
        db.tambah(m1)
        with pytest.raises(ValueError):
            db.tambah(m2)

    # --- Tambahan (edge case) ---
    def test_cari_nim_tidak_ada(self):
        assert DaftarMahasiswa().cari("999999") is None

    def test_hapus_nim_tidak_ada(self):
        assert DaftarMahasiswa().hapus("999999") is False

    def test_hapus_berhasil(self):
        db = DaftarMahasiswa()
        db.tambah(Mahasiswa("2024SI001", "Andi", "SI", 2024))
        assert db.hapus("2024SI001") is True
        assert db.jumlah == 0

    def test_edit_ipk_berhasil(self):
        db = DaftarMahasiswa()
        db.tambah(Mahasiswa("2024SI001", "Andi", "SI", 2024, 3.0))
        assert db.edit_ipk("2024SI001", 3.75) is True
        assert db.cari("2024SI001").ipk == 3.75

    def test_edit_ipk_diluar_range(self):
        db = DaftarMahasiswa()
        db.tambah(Mahasiswa("2024SI001", "Andi", "SI", 2024, 3.0))
        with pytest.raises(ValueError):
            db.edit_ipk("2024SI001", 4.5)

    def test_edit_ipk_nim_tidak_ada(self):
        assert DaftarMahasiswa().edit_ipk("999999", 3.0) is False
