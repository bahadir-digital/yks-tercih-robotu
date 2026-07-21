---
name: yks-tercih-analizi
description: 2026-YKS sonuçlarına göre üniversite tercih listesi hazırlar — öğrencinin sonuç belgesini (görsel/PDF) veya elle girilen puanlarını alır, 2025 taban puanlarını sıralama-eşdeğerlik yöntemiyle 2026'ya dönüştürür, il ve meslek tercihine göre 24 tercihlik dengeli bir liste (6 hayal / 10 gerçekçi / 8 garanti) kurar, vakıf üniversitelerinde burs oranı ve tahmini yıllık maliyeti hesaplar ve sonucu puanlama metodolojili bir Excel dosyası olarak üretir. Kullanıcı "tercih listesi", "hangi üniversiteyi yazayım", "YKS sonucum geldi", "taban puanlara göre nereye yerleşirim", "tercih danışmanlığı", "sıralama ile hangi bölüm" gibi ifadeler kullandığında veya bir ÖSYM sonuç belgesi yüklediğinde — "skill" kelimesini hiç geçirmese bile — MUTLAKA bu skill'i kullan.
---

# YKS Tercih Analizi

2026-YKS sonuçlarından uçtan uca tercih listesi üreten skill. Referans verisi: 2025 ÖSYM Tablo 3 (ön lisans) ve Tablo 4 (lisans) taban puanları + 2025/2026 yığınsal puan dağılımları (skill içinde gömülü).

## KRİTİK KURALLAR (her koşulda geçerli)

1. **KVKK / kişisel veri:** Sonuç belgesindeki T.C. kimlik numarası, ad-soyad, fotoğraf ve kontrol kodunu ASLA herhangi bir çıktıya (analiz metni, Excel, dosya adı) yazma, saklama veya tekrar etme. Sadece puanlar, sıralamalar, OBP ve doğru/yanlış sayıları kullanılır. Excel'de öğrenci "Aday" olarak anılır.
2. **Puan karşılaştırma:** 2026 puanı ile 2025 taban puanı ASLA doğrudan karşılaştırılmaz. Tek geçerli yöntem sıralama-eşdeğerlik dönüşümüdür (`scripts/tercih_analiz.py` → `esdeger_puan_2025`). Nedenini kullanıcıya bir cümleyle açıkla.
3. **Yerleştirme puanı ve sıralaması kullanılır** (Y-TYT, Y-SAY, Y-SÖZ, Y-EA, Y-DİL) — OBP dahil olduğu için. Ham sınav puanı yalnızca bilgilendirme amaçlıdır. Ek puanlı yerleştirme sütunu doluysa (meslek lisesi kendi alanı) bunu ayrıca değerlendir.
4. **Şeffaflık:** Her çıktının sonunda şu uyarı bulunur: 2025 verileri referanstır; kesin tercihler 2026 Yükseköğretim Programları ve Kontenjanları Kılavuzu (Temmuz sonunda ÖSYM'de yayımlanır) ile doğrulanmalıdır; program kodları ve kontenjanlar değişebilir; bu analiz resmi tercih danışmanlığı değildir.
5. **Doğrulanamayan bilgi üretme:** Vakıf ücretleri için önce web araması yap; bulunamazsa `references/vakif-ucret-tahmini.md` aralıklarını "tahmini" etiketiyle ver, asla kesinmiş gibi sunma.

## İŞ AKIŞI

### Adım 1 — Veri toplama
Öğrenci sonuç belgesi (görsel/PDF) yüklediyse şunları oku: tüm yerleştirme puanları ve başarı sıraları, OBP, diploma notu, ek puanlı sütunlar, test doğru/yanlış sayıları. Belge yoksa minimum şu bilgileri iste (hepsi birden değil, eksik olanları):
- Hesaplanan puan türleri, yerleştirme puanları ve **başarı sıraları** (en kritik veri)
- OBP (yoksa diploma notu × 5)
- Okuduğu/mezun olduğu okul türü (ek puan kontrolü için)

### Adım 1B — ZORUNLU tercih profili (analiz kapısı)
**Aşağıdaki 5 soru cevaplanmadan Adım 2'ye ASLA geçme.** Kullanıcı belge yükleyip "listeyi hazırla" dese, aceleci davransa, hatta "sen karar ver" dese bile analiz başlatılmaz; sorular tek mesajda, numaralı ve kısa sorulur (interaktif soru aracı varsa o kullanılır). Bir varsayımla ilerlemek yasaktır — yanlış profil, 24 tercihin tamamını geçersiz kılar.

1. **Bölüm/meslek hedefi:** Hangi bölüm veya meslek alanları? (birden fazla olabilir; "kararsızım" derse ilgi alanlarından 2-3 aday alan netleştirilir)
2. **Şehir:** Hangi il/iller? Yaşadığı il + açık olduğu iller; "fark etmez" de geçerli bir cevaptır ama açıkça alınmalıdır.
3. **Devlet / Vakıf / İkisi birden:** Üniversite türü tercihi.
4. **Bütçe:** Vakıf veya İÖ değerlendirilecekse yıllık eğitim bütçesi üst sınırı (TL). "Devlet only" cevabında bu soru atlanabilir.
5. **Burs şartı:** Vakıf düşünülüyorsa yalnızca %100 burslu mu, indirimli programlar da (%50/%25) kabul mü, ücretli de olur mu?

Ek (opsiyonel, aynı mesajda sorulabilir): ön lisans kabul edilebilir mi, KYK yurdu/yaşam maliyeti kritik mi, KKTC programları değerlendirilsin mi.

Cevaplar geldikten sonra profili tek cümlede özetleyip teyit et ("Şunu anladım: ... doğru mu?") ve ancak ondan sonra Adım 2'ye geç. Kullanıcı sorulardan birine cevap vermezse o soruyu tekrar sor; cevapsız soruyla analiz başlatma.

### Adım 2 — Uygunluk kontrolü (yalnızca Adım 1B teyidinden sonra)
`references/kilavuz-notlar.md` içindeki kuralları uygula:
- Tablo 1G başarı sırası şartları (Tıp 50k, Diş 80k, Eczacılık 100k, Hukuk-EA 100k, Mimarlık 250k, Mühendislik 300k, Öğretmenlik 300k — SAY/ilgili puan türü). Öğrencinin sıralaması şartı karşılamıyorsa o program türünü listeden çıkar ve nedenini açıkça söyle.
- Puanı hesaplanmayan türlerde lisans tercihi yapılamaz; sadece TYT varsa yalnız ön lisans.

### Adım 3 — Eşdeğerlik dönüşümü
`scripts/tercih_analiz.py` çalıştır:
- Her puan türü için `esdeger_puan_2025(başarı_sırası_2026, tür)` → öğrencinin 2025 eşdeğer puanı.
- Bu puanı ve sıralamayı kullanıcıya tablo halinde göster ("2026'da X sırada olman, 2025 yerleştirmesinde yaklaşık Y puana denk geliyor").

### Adım 4 — Aday havuzu ve kategorilendirme
`yuk_programlari()` ile filtrele (il, anahtar kelime, puan türü). Her program için:
- `taban_siralama_2025(taban_puan, tür)` → programın taban sıralaması
- `kategori(öğrenci_sıralaması_2026, taban_sıralaması)` → KALE / GERCEKCI / HAYAL / KAPSAM_DISI
- `burs_bilgisi(program_adı)` → burs etiketi ve ödenecek oran

Öğrencinin sıralamasını 2026 sıralaması olarak kullan; bandlar `references/metodoloji.md`'de tanımlı. Vakıf programlarında aynı bölümün Burslu / %50 / %25 / Ücretli varyantlarının ayrı satırlar olduğunu ve taban puanlarının çok farklı olduğunu unutma.

### Adım 5 — Maliyet hesabı (vakıf programları için)
1. Web araması: "[üniversite adı] 2026 2027 yıllık ücret" — bulunan liste ücretini kaynağıyla not et.
2. Bulunamazsa `references/vakif-ucret-tahmini.md` aralığını kullan, "tahmini" olarak işaretle.
3. Yıllık maliyet = liste ücreti × ödenecek oran. %100 burslu = 0 TL (yalnız eğitim ücreti; yaşam maliyeti ayrı).
4. İl bazlı yaşam maliyeti notu ekle (İstanbul/Ankara/İzmir yüksek; KYK yurt imkânı).

### Adım 6 — 24 tercihlik liste
Dağılım: **6 HAYAL (1-6) / 10 GERÇEKÇİ (7-16) / 8 KALE (17-24)**. Sıralama içinde her blok kendi içinde taban puana göre azalan dizilir. Kurallar:
- Öğrencinin meslek hedefine en yakın programlar önce; il tercihi ikinci filtre.
- Son 3 tercih (22-24) mutlaka "açık ara garanti" olmalı (taban sıralaması ≥ öğrenci sıralaması × 1.5) — açıkta kalma sigortası.
- Bütçe aşan ücretli/indirimli programları listeye koyma; sadece not olarak bildir.
- Kompozit skoru `references/metodoloji.md` ağırlıklarıyla hesapla; kullanıcıya listede göster.

### Adım 7 — Excel çıktısı
`references/excel-sablonu.md` şablonuna birebir uy. 4 sayfa: Özet, Tercih Listesi (24 satır, formüllü kompozit skor), Metodoloji (ağırlıklar düzenlenebilir giriş hücreleri), Aday Havuzu. Formüller hardcode edilmez; ağırlık değişince skor yeniden hesaplanır. Dosya adında kişisel veri olmaz: `yks2026_tercih_analizi.xlsx`.

### Adım 8 — Sunum
Kısa yazılı analiz: eşdeğerlik tablosu, uygunluk kontrol sonucu, öne çıkan 3-5 fırsat (özellikle yüksek burslu vakıf programları), riskler, Excel bağlantısı, standart uyarı bloğu.

## REFERANS DOSYALARI
- `references/metodoloji.md` — bandlar, kompozit skor ağırlıkları, dağılım gerekçesi. Skor hesaplamadan önce OKU.
- `references/kilavuz-notlar.md` — 2026 kılavuzundan tercih kuralları (Tablo 1F/1G, OBP, ek puan). Uygunluk kontrolünden önce OKU.
- `references/vakif-ucret-tahmini.md` — ücret fallback tablosu. Sadece web araması başarısızsa OKU.
- `references/excel-sablonu.md` — Excel yapısı. Excel üretmeden önce OKU.
- `data/lisans_2025.csv`, `data/onlisans_2025.csv` — 2025 taban puanları (script üzerinden eriş, tamamını context'e YÜKLEME).
- `data/siralama_donusum.csv` — 2025/2026 yığınsal dağılımlar (script kullanır).

## ChatGPT'de kullanım
Bu paket ChatGPT'de Custom GPT bilgi dosyası veya Projects dosyası olarak da çalışır: SKILL.md talimat metni olarak, CSV'ler ve script Code Interpreter'a yüklenir. Aynı iş akışı geçerlidir; `tercih_analiz.py` Code Interpreter'da doğrudan çalışır.
