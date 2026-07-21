# YKS Tercih Analizi Skill

2026-YKS sonuçlarından uçtan uca tercih listesi üretir: sonuç belgesi analizi, sıralama-eşdeğerlik dönüşümü, 24 tercihlik dengeli liste (6 hayal / 10 gerçekçi / 8 garanti), burs ve yıllık maliyet hesabı, puanlama metodolojili Excel çıktısı.

## İçerik
```
yks-tercih-analizi/
├── SKILL.md                      # Ana talimatlar
├── data/
│   ├── lisans_2025.csv           # ÖSYM Tablo 4 (12.265 program)
│   ├── onlisans_2025.csv         # ÖSYM Tablo 3 (9.337 program)
│   └── siralama_donusum.csv      # 2025/2026 yığınsal puan dağılımları
├── references/
│   ├── metodoloji.md             # Bandlar, kompozit skor, dağılım
│   ├── kilavuz-notlar.md         # 2026 kılavuz tercih kuralları
│   ├── vakif-ucret-tahmini.md    # Ücret fallback tablosu
│   └── excel-sablonu.md          # Excel çıktı yapısı
└── scripts/
    └── tercih_analiz.py          # Eşdeğerlik + filtreleme hesapları
```

## Claude'da kurulum
Ayarlar → Yetenekler → Skill yükle → `yks-tercih-analizi.skill` dosyasını seç. Ya da klasörü bir Claude Projesi'ne yükleyip SKILL.md içeriğini proje talimatı yap.

## ChatGPT'de kurulum
1. Custom GPT oluştur (veya bir Project aç).
2. SKILL.md içeriğini Instructions alanına yapıştır ("skill" ifadelerini "bu talimatlar" olarak oku).
3. `data/` içindeki 3 CSV'yi ve `scripts/tercih_analiz.py` ile `references/` dosyalarını Knowledge/Files olarak yükle.
4. Code Interpreter'ı aç. Script doğrudan çalışır.

## Kullanım
Sonuç belgesini (fotoğraf/PDF) yükleyin veya puan-sıralama bilgilerinizi yazın. Skill, analize başlamadan önce 5 zorunlu soruyu sorar: bölüm/meslek hedefi, şehir, devlet/vakıf tercihi, bütçe ve burs şartı — bunlar cevaplanmadan liste üretilmez. Örnek: "Sonuç belgem ekte, İzmir veya İstanbul'da yazılım alanında okumak istiyorum, vakıf için yıllık bütçem 600 bin TL."

## Sorumluluk notu
2025 taban puanları referanstır; kesin tercih 2026 Yükseköğretim Programları ve Kontenjanları Kılavuzu ile yapılmalıdır. Bu araç resmi tercih danışmanlığı değildir. Kişisel veriler (T.C. no, ad-soyad) hiçbir çıktıda kullanılmaz.

---
Hazırlayan: Bahadır Eren — bahadir.digital · Türkçe Profesyoneller İçin Claude Skills serisi
