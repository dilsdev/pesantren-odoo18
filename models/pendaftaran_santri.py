from odoo import models, fields

class PendaftaranSantri(models.Model):
    _name = 'pendaftaran.santri'
    _description = 'Data Pendaftaran Santri'

    # 1. Data Pribadi Santri
    name = fields.Char(string='Nama Lengkap', required=True)
    nickname = fields.Char(string='Nama Panggilan')
    gender = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan')
    ], string='Jenis Kelamin', required=True)
    birth_place = fields.Char(string='Tempat Lahir')
    birth_date = fields.Date(string='Tanggal Lahir')
    nik = fields.Char(string='NIK (Nomor Induk Kependudukan)')
    address = fields.Text(string='Alamat Lengkap')
    phone = fields.Char(string='Nomor HP Santri')
    email = fields.Char(string='Email')
    religion = fields.Selection([
        ('islam', 'Islam'),
        ('other', 'Lainnya')
    ], string='Agama', required=True)
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')
    ], string='Golongan Darah')
    nationality = fields.Char(string='Kewarganegaraan', default='Indonesia')

    # 2. Data Orang Tua/Wali
    father_name = fields.Char(string='Nama Ayah')
    father_job = fields.Char(string='Pekerjaan Ayah')
    father_education = fields.Char(string='Pendidikan Ayah')
    father_phone = fields.Char(string='Nomor HP Ayah')
    mother_name = fields.Char(string='Nama Ibu')
    mother_job = fields.Char(string='Pekerjaan Ibu')
    mother_education = fields.Char(string='Pendidikan Ibu')
    mother_phone = fields.Char(string='Nomor HP Ibu')
    guardian_name = fields.Char(string='Nama Wali (jika ada)')
    guardian_job = fields.Char(string='Pekerjaan Wali')
    guardian_phone = fields.Char(string='Nomor HP Wali')
    parent_address = fields.Text(string='Alamat Orang Tua')

    # 3. Data Pendidikan Sebelumnya
    previous_school = fields.Char(string='Nama Sekolah Asal')
    school_address = fields.Text(string='Alamat Sekolah Asal')
    education_level = fields.Selection([
        ('sd', 'SD/MI'),
        ('smp', 'SMP/MTs'),
        ('sma', 'SMA/MA')
    ], string='Jenjang Pendidikan Terakhir')
    nisn = fields.Char(string='Nomor Induk Siswa Nasional (NISN)')
    graduation_year = fields.Char(string='Tahun Lulus')

    # 4. Data Kesehatan
    medical_history = fields.Text(string='Riwayat Penyakit')
    allergies = fields.Text(string='Alergi')
    special_needs = fields.Text(string='Kebutuhan Khusus')
    emergency_contact = fields.Char(string='Kontak Darurat')

    # 5. Data Akademik dan Non-Akademik
    quran_memorization = fields.Text(string='Hafalan Al-Quran')
    academic_achievements = fields.Text(string='Prestasi Akademik')
    non_academic_achievements = fields.Text(string='Prestasi Non-Akademik')
    extracurricular_interests = fields.Text(string='Ekstrakurikuler yang Diminati')

    # 6. Informasi Lainnya
    reason_for_joining = fields.Text(string='Alasan Memilih Pesantren')
    referral_source = fields.Selection([
        ('family', 'Keluarga'),
        ('friends', 'Teman'),
        ('social_media', 'Media Sosial'),
        ('other', 'Lainnya')
    ], string='Referensi Pendaftaran')
    registration_date = fields.Date(string='Tanggal Pendaftaran')

    # 7. Dokumen Pendukung
    birth_certificate = fields.Binary(string='Akte Kelahiran')
    family_card = fields.Binary(string='Kartu Keluarga')
    last_certificate = fields.Binary(string='Ijazah Terakhir')
    health_certificate = fields.Binary(string='Surat Keterangan Sehat')
    parent_id_card = fields.Binary(string='KTP Orang Tua/Wali')
    photo = fields.Binary(string='Foto Berwarna')

    # 8. Data Biaya
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
        ('installment', 'Cicilan')
    ], string='Metode Pembayaran')
    amount_paid = fields.Float(string='Jumlah yang Dibayarkan')
    payment_proof = fields.Binary(string='Bukti Pembayaran')

    # Status Penerimaan
    status = fields.Selection([
        ('draft', 'Pendaftaran Diterima'),
        ('process', 'Dalam Proses Seleksi'),
        ('accepted', 'Diterima'),
        ('rejected', 'Ditolak')
    ], string='Status Penerimaan', default='draft')
