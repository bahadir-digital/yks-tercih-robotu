#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YKS Tercih Analizi — yardımcı hesaplama modülü
Kullanım: skill klasörü içinden import edilir veya doğrudan çalıştırılır.

Temel işlevler:
  esdeger_puan_2025(siralama_2026, puan_turu)  -> öğrencinin 2026 başarı sırasının
                                                  2025 yerleştirme puanı karşılığı
  taban_siralama_2025(puan_2025, puan_turu)    -> bir programın 2025 taban puanının
                                                  2025 sıralama karşılığı
  kategori(ogrenci_siralama_2026_esdeger_2025, program_taban_siralamasi) -> H/G/K
  yuk_programlari(...)                         -> filtrelenmiş aday havuzu
"""
import csv, os, re, unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")

PUAN_TURLERI = ["TYT", "SAY", "SOZ", "EA", "DIL"]
_TR_MAP = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")


def _norm(s):
    return (s or "").translate(_TR_MAP).lower()


def _load_donusum():
    tablolar = {2025: {}, 2026: {}}
    with open(os.path.join(DATA, "siralama_donusum.csv"), encoding="utf-8") as f:
        for row in csv.DictReader(f):
            yil = int(row["yil"])
            puan = float(row["puan"])
            for pt in PUAN_TURLERI:
                tablolar[yil].setdefault(pt, []).append((puan, int(row[pt])))
    # puan azalan sırada (550 -> 115), sıralama artan
    for yil in tablolar:
        for pt in tablolar[yil]:
            tablolar[yil][pt].sort(key=lambda x: -x[0])
    return tablolar


_DONUSUM = _load_donusum()


def _puan_to_siralama(puan, puan_turu, yil):
    """Kümülatif tablodan doğrusal interpolasyonla puan -> sıralama."""
    tbl = _DONUSUM[yil][puan_turu]
    if puan >= tbl[0][0]:
        return tbl[0][1]
    if puan <= tbl[-1][0]:
        return tbl[-1][1]
    for i in range(len(tbl) - 1):
        p_hi, s_hi = tbl[i]
        p_lo, s_lo = tbl[i + 1]
        if p_lo <= puan <= p_hi:
            oran = (p_hi - puan) / (p_hi - p_lo)
            return int(round(s_hi + oran * (s_lo - s_hi)))
    return tbl[-1][1]


def _siralama_to_puan(siralama, puan_turu, yil):
    """Kümülatif tablodan doğrusal interpolasyonla sıralama -> puan."""
    tbl = _DONUSUM[yil][puan_turu]
    if siralama <= tbl[0][1]:
        return tbl[0][0]
    if siralama >= tbl[-1][1]:
        return tbl[-1][0]
    for i in range(len(tbl) - 1):
        p_hi, s_hi = tbl[i]
        p_lo, s_lo = tbl[i + 1]
        if s_hi <= siralama <= s_lo:
            oran = (siralama - s_hi) / (s_lo - s_hi)
            return round(p_hi - oran * (p_hi - p_lo), 2)
    return tbl[-1][0]


def esdeger_puan_2025(siralama_2026, puan_turu):
    """Öğrencinin 2026 yerleştirme başarı sırası -> 2025 eşdeğer yerleştirme puanı.
    Taban puan karşılaştırmasının TEK geçerli yolu budur; 2026 ham puanı
    2025 taban puanıyla ASLA doğrudan karşılaştırma."""
    return _siralama_to_puan(siralama_2026, puan_turu, 2025)


def taban_siralama_2025(taban_puan, puan_turu):
    """Programın 2025 taban puanı -> 2025 taban sıralaması (yaklaşık)."""
    return _puan_to_siralama(taban_puan, puan_turu, 2025)


def kategori(ogrenci_siralamasi, program_taban_siralamasi):
    """Risk bandı. Sıralama uzayında oran: taban_sıra / öğrenci_sıra.
    >= 1.25  -> KALE (garanti)
    0.90-1.25 -> GERCEKCI
    0.60-0.90 -> HAYAL (ulaşılabilir hayal)
    < 0.60   -> KAPSAM DISI (önermeye değmez)"""
    if not program_taban_siralamasi or not ogrenci_siralamasi:
        return "BELIRSIZ"
    oran = program_taban_siralamasi / ogrenci_siralamasi
    if oran >= 1.25:
        return "KALE"
    if oran >= 0.90:
        return "GERCEKCI"
    if oran >= 0.60:
        return "HAYAL"
    return "KAPSAM_DISI"


def burs_bilgisi(program_adi):
    """Program adından burs oranını çıkarır. Döner: (etiket, odenecek_oran)."""
    p = _norm(program_adi)
    if "burslu" in p:
        return ("%100 Burslu", 0.0)
    m = re.search(r"%\s*(\d+)\s*indirimli", p)
    if m:
        ind = int(m.group(1))
        return ("%%%d İndirimli" % ind, (100 - ind) / 100.0)
    if "ucretli" in p:
        return ("Ücretli", 1.0)
    return ("Devlet/Ücretsiz", None)  # devlet programı veya belirtilmemiş


def yuk_programlari(dosya, puan_turu=None, sehirler=None, anahtar_kelimeler=None,
                    min_taban=None, max_taban=None):
    """CSV'den filtrelenmiş program listesi.
    dosya: 'lisans_2025.csv' | 'onlisans_2025.csv'
    anahtar_kelimeler: program adında aranacak kelimeler (TR-normalize, OR mantığı)
    sehirler: şehir listesi (TR-normalize)"""
    sonuc = []
    kw = [_norm(k) for k in (anahtar_kelimeler or [])]
    sh = [_norm(s) for s in (sehirler or [])]
    with open(os.path.join(DATA, dosya), encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if puan_turu and row["puan_turu"] != puan_turu:
                continue
            if sh and _norm(row["sehir"]) not in sh:
                continue
            if kw and not any(k in _norm(row["program"]) for k in kw):
                continue
            try:
                tp = float(row["taban_puan"])
            except (ValueError, TypeError):
                continue  # '--' = yerleşen yok, taban oluşmamış
            if min_taban and tp < min_taban:
                continue
            if max_taban and tp > max_taban:
                continue
            row["taban_puan"] = tp
            sonuc.append(row)
    sonuc.sort(key=lambda r: -r["taban_puan"])
    return sonuc


if __name__ == "__main__":
    # Hızlı doğrulama
    s = esdeger_puan_2025(230527, "SAY")
    print("2026 SAY sıralama 230.527 -> 2025 eşdeğer puan:", s)
    print("Taban 330.5 SAY -> 2025 sıralama:", taban_siralama_2025(330.5, "SAY"))
