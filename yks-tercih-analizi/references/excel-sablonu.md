# Excel Çıktı Şablonu (tek sayfa)

Dosya adı: `yks2026_tercih_analizi.xlsx` (kişisel veri içermez). **Font: Aptos, 9 punto** (başlık 13pt). Tek sayfa: "Tercih Analizi". Kategori metin olarak yazılmaz; band bilgisi tamamen görselle (trafik ışığı ikon seti + satır tonu + ok ikonları) verilir. Formüller hardcode edilmez; recalc sonrası sıfır formül hatasıyla teslim edilir.

## Sayfa düzeni (tek sayfa)

**Üst blok (satır 1-11):**
- Başlık + üretim tarihi/kaynak notu (kişisel kimlik bilgisi içermediği ibaresi).
- ADAY PROFİLİ mini tablosu (A5:D8): puan türü, 2026 puan, 2026 sıra, 2025 eşdeğer puan.
- GİRDİLER (F4:G8): SAY sırası, TYT sırası, bütçe, OBP — **mavi yazı + sarı dolgu** düzenlenebilir hücreler; tablo formülleri buraya referans verir.
- SKOR AĞIRLIKLARI (I4:J10): 5 bileşen giriş hücresi + =SUM toplamı; toplam ≠ 100 ise CellIs kuralıyla kırmızı yanar.
- UYGUNLUK (Tablo 1G) (L4:M11): program türleri; AÇIK yeşil dolgu/yazı, KAPALI kırmızı dolgu/yazı.
- DAĞILIM (O4:P7): oran sütunundan COUNTIF/COUNTIFS ile Kale/Gerçekçi/Hayal sayaçları.
- LEJANT satırı: görsel dilin bir cümlelik açıklaması.

**Tercih tablosu (başlık satır 13, veri 14-37, 24 satır):**
| Sütun | İçerik |
|---|---|
| A | Tercih sırası 1-24 |
| B | **Durum** — değeri `=K{satır}` (oran), sayı gizli (`showValue=False`), 3TrafficLights1 ikon seti: kırmızı <0,90 · sarı 0,90-1,25 · yeşil ≥1,25 |
| C-H | Program kodu, üniversite, tür, şehir, program (burs ibaresi dahil), puan türü |
| I | 2025 taban puan — 3 renkli ColorScale (beyaz→sarı→turuncu) |
| J | 2025 taban sıralama |
| K | Sıralama oranı `=J/IF(H="TYT",TYT_hücresi,SAY_hücresi)` — 3Arrows ikon seti (değer görünür) |
| L | Burs — "%100 Burslu" CellIs kuralıyla yeşil |
| M | Yıllık maliyet — ColorScale yeşil(0)→sarı(bütçenin yarısı)→kırmızı(bütçe) + bütçe aşımında CellIs kırmızı dolgu |
| N | Maliyet kaynağı ("Resmi site (tarih)" / "Tahmin bandı" / "Devlet") |
| O-S | Skor bileşenleri ham 0-1 |
| T | SKOR `=SUMPRODUCT mantığıyla O:S × ağırlık hücreleri` — DataBar (0-100) |

**Satır tonu (FormulaRule, A:T aralığına):** $K'ya göre KALE açık yeşil `EBF6EB`, GERÇEKÇİ açık sarı `FFF8E1`, HAYAL açık kırmızı `FDEBE6`.
**Diğer:** E sütununda "DEVLET" kalın koyu yeşil (CellIs). Başlık satırı koyu dolgu `1F4E5F` + beyaz kalın; freeze_panes veri başında.

**Alt blok:** birleştirilmiş hücrede standart uyarı metni (gri italik).

## Teknik notlar
- İkon setleri: openpyxl `IconSetRule('3TrafficLights1'|'3Arrows','num',[0,0.9,1.25])`. XLOOKUP/FILTER/SORT kullanma; IF/COUNTIF(S)/SUM yeterli.
- Sayı biçimleri: puan `0.00`, sıralama `#,##0`, TL `#,##0`, skor `0.0`.
- Kullanıcı özellikle çok sayfalı isterse eski düzen (Özet/Liste/Metodoloji/Havuz) uygulanabilir; varsayılan tek sayfadır.
