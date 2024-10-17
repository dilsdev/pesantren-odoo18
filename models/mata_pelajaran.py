from odoo import models, fields

class MataPelajaranPesantren(models.Model):
    _name = 'mata.pelajaran.pesantren'
    _description = 'Mata Pelajaran Pesantren'

    nama_mata_pelajaran = fields.Char(string='Nama Mata Pelajaran', required=True)
    kode_mata_pelajaran = fields.Char(string='Kode Mata Pelajaran')
    kategori_mata_pelajaran = fields.Selection([
        ('umum', 'Umum'),
        ('diniyah', 'Diniyah'),
        ('kitab', 'Kajian Kitab'),
        ('keterampilan', 'Keterampilan')], string='Kategori', required=True)
    guru_id = fields.Many2one('res.partner', string='Guru Pengajar')
    jumlah_jam = fields.Integer(string='Jumlah Jam')
    # tingkat_id = fields.Many2one('school.level', string='Tingkat/Kelas')
    semester = fields.Selection([
        ('ganjil', 'Ganjil'),
        ('genap', 'Genap')], string='Semester')
    jadwal_hari = fields.Selection([
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('sabtu', 'Sabtu'),
        ('minggu', 'Minggu')], string='Hari')
    jadwal_waktu = fields.Float(string='Waktu (Jam)')
    ruangan_id = fields.Many2one('pesantren.room', string='Ruangan')
    silabus = fields.Text(string='Silabus')
    metode_pengajaran = fields.Selection([
        ('ceramah', 'Ceramah'),
        ('diskusi', 'Diskusi'),
        ('praktikum', 'Praktikum'),
        ('hafalan', 'Hafalan'),
        ('mudzakarah', 'Mudzakarah')], string='Metode Pengajaran')
    buku_kitab = fields.Text(string='Buku/Kitab Acuan')
    bobot_penilaian = fields.Float(string='Bobot Penilaian')
    kurikulum = fields.Selection([
        ('kurikulum_nasional', 'Kurikulum Nasional'),
        ('kurikulum_pesantren', 'Kurikulum Pesantren'),
        ('kurikulum_khusus', 'Kurikulum Khusus')], string='Kurikulum')
    kkm = fields.Float(string='Nilai KKM')
    jumlah_siswa = fields.Integer(string='Jumlah Siswa')
    catatan_khusus = fields.Text(string='Catatan Khusus')
    status_mata_pelajaran = fields.Boolean(string='Aktif/Nonaktif', default=True)
