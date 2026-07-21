# Claude ile YKS Tercih Robotu

2026-YKS sonuç belgenizi yükleyin, sorulara cevap verin; 24 tercihlik dengeli bir liste, burs oranları, tahmini yıllık maliyetler ve puanlama metodolojili bir Excel raporu üretilsin. Hem **Claude** hem **ChatGPT** üzerinde çalışır. Tamamen ücretsizdir.

## Neden güvenilir

- **Tahmin yok, veri var.** ÖSYM'nin 2025 Tablo 3 ve Tablo 4 verilerindeki 21.602 programın taban ve tavan puanları paketin içinde gömülü gelir. Model ezberden puan uydurmaz; her karşılaştırma bu tablolardan yapılır.
- **Son iki yılın sonuç istatistikleri.** 2025 ve 2026 YKS sayısal bilgilerindeki yığınsal puan dağılımları pakete dahildir. 2026 puanınız 2025 taban puanıyla asla doğrudan karşılaştırılmaz; başarı sıranız üzerinden **sıralama-eşdeğerlik dönüşümü** yapılır. Yıllar arası tek geçerli karşılaştırma yöntemi budur.
- **Resmi kurallar gömülü.** 2026 YKS Kılavuzu'ndaki başarı sırası şartları (Tıp 50.000, Hukuk 100.000, Mühendislik 300.000 vb.), OBP katsayıları ve tercih koşulları pakete işlenmiştir; sıranızın yetmediği program türleri gerekçesiyle elenir.
- **Hesaplar deterministiktir.** Eşdeğerlik ve filtreleme, modele değil paketteki Python betiğine yaptırılır; aynı girdiye her zaman aynı sonuç.
- **Kişisel veri kullanılmaz.** T.C. kimlik numarası, ad-soyad ve fotoğraf hiçbir çıktıya yazılmaz.

## Ne üretir

1. Puanlarınızın 2025 eşdeğer karşılıkları ve uygunluk kontrolü
2. Bölüm, şehir, devlet/vakıf, bütçe ve burs tercihlerinize göre filtrelenmiş aday havuzu
3. **24 tercihlik liste: 6 hayal / 10 gerçekçi / 8 garanti** dengesiyle
4. Vakıf programlarında burs oranı ve tahmini yıllık maliyet (mümkünse resmi kaynaktan, değilse "tahmini" etiketiyle)
5. Trafik ışıklı, koşullu biçimlendirmeli, düzenlenebilir ağırlıklı tek sayfa **Excel raporu**

Robot analize başlamadan önce 5 soruyu mutlaka sorar: bölüm hedefi, şehir, devlet/vakıf tercihi, bütçe ve burs şartı. Bunlar cevaplanmadan liste üretilmez.

## Kurulum — Claude

1. Bu repodan [`yks-tercih-analizi.skill`](./yks-tercih-analizi.skill) dosyasını indirin (Download raw file).
2. Claude.ai → **Ayarlar → Yetenekler (Capabilities) → Skill yükle** ile dosyayı seçin.
3. Yeni bir sohbette sonuç belgenizin fotoğrafını/PDF'ini yükleyin ve "tercih listemi hazırla" yazın.

Alternatif: `yks-tercih-analizi/` klasörünü bir Claude Projesi'ne yükleyip `SKILL.md` içeriğini proje talimatı yapabilirsiniz.

## Kurulum — ChatGPT

1. Repoyu indirin (Code → Download ZIP) ve `yks-tercih-analizi/` klasörünü açın.
2. Yeni bir **Project** (veya Custom GPT) oluşturun; `SKILL.md` içeriğini Instructions alanına yapıştırın.
3. `data/` içindeki 3 CSV'yi, `scripts/tercih_analiz.py` dosyasını ve `references/` klasöründeki dosyaları Files/Knowledge olarak yükleyin.
4. Code Interpreter'ın açık olduğundan emin olun ve sonuç belgenizi yükleyerek başlayın.

## Repo yapısı

```
├── yks-tercih-analizi.skill      # Claude için tek dosya kurulum
└── yks-tercih-analizi/           # Kaynak paket (ChatGPT ve inceleme için)
    ├── SKILL.md                  # Talimatlar ve iş akışı
    ├── data/                     # 2025 taban puanları + 2025/2026 dağılımlar
    ├── references/               # Metodoloji, kılavuz kuralları, ücret bantları, Excel şablonu
    └── scripts/tercih_analiz.py  # Eşdeğerlik ve filtreleme hesapları
```

## Sorumluluk notu

2025 taban puanları referanstır; kesin tercihler ÖSYM'nin 2026 Yükseköğretim Programları ve Kontenjanları Kılavuzu ile doğrulanmalıdır. Program kodları, kontenjanlar ve ücretler değişebilir. Bu araç resmi tercih danışmanlığı değildir; nihai karar adaya ve ailesine aittir.

## Lisans

MIT — dilediğiniz gibi kullanın, geliştirin, paylaşın.

## İletişim

- **Blog:** [bahadir.digital](https://bahadir.digital)
- **LinkedIn:** [linkedin.com/in/bahadireren](https://linkedin.com/in/bahadireren)
- **X:** [x.com/bahadir_digital](https://x.com/bahadir_digital)
- **Instagram:** [@bahadir.digital](https://instagram.com/bahadir.digital) · [@ofiste.ai](https://instagram.com/ofiste.ai)
- **Claude.ai Türkiye WhatsApp topluluğu:** [katılım linki](https://chat.whatsapp.com/I2763pKIpmS9xADAHLaGPE)
- **E-posta:** bahadireren@gmail.com
