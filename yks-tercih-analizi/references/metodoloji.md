# Tercih Metodolojisi

## 1. Sıralama-eşdeğerlik yöntemi (neden puan değil)

Her yıl soru zorluğu, aday sayısı ve puan dağılımı değişir. 2026'da TYT'ye giren geçerli aday sayısı 2.254.830 iken 2025'te 2.351.397 idi; ortalamalar da farklı (ör. TYT Türkçe 2026: 20,1 — 2025: 21,2). Bu yüzden 2026 puanı 2025 taban puanıyla doğrudan karşılaştırılamaz. Karşılaştırılabilir tek büyüklük **başarı sırasıdır**: yerleştirme sıralama mantığı puana değil sıraya dayanır.

Yöntem: öğrencinin 2026 yerleştirme başarı sırası, 2025 yerleştirme puanlarının yığınsal dağılımında (`data/siralama_donusum.csv`) doğrusal interpolasyonla 2025 eşdeğer puanına çevrilir. Program taraflarında da 2025 taban puanı aynı tablodan 2025 taban sıralamasına çevrilir. Karşılaştırma sıralama uzayında yapılır.

Sınır durumları: 550+ puan ve 115 altı bölgelerde tablo uç değeri kullanılır; ilk 100'e giren adaylarda interpolasyon hassasiyeti düşer, bunu belirt.

## 2. Risk bandları

`oran = program_taban_sıralaması / öğrenci_sıralaması`

| Band | Oran | Anlamı |
|---|---|---|
| KALE (garanti) | ≥ 1,25 | Program geçen yıl öğrencinin sırasından belirgin düşük sırayla kapandı; yerleşme olasılığı çok yüksek |
| GERÇEKÇİ | 0,90 – 1,25 | Sınır bölgesi; kontenjan/talep dalgalanmasına göre iki yönde de sonuçlanabilir |
| HAYAL | 0,60 – 0,90 | Geçen yıl kapatamazdı ama taban düşüşü/kontenjan artışıyla şansı var |
| KAPSAM DIŞI | < 0,60 | Önerme; listeye alma |

Ek güvenlik: tercih 22-24 için oran ≥ 1,50 şartı (açıkta kalma sigortası). Kontenjanı dolmamış (yerleşen < kontenjan) programlar KALE sayılabilir ama nedeni araştırılmalı (yeni program, ücret, şehir).

## 3. 24 tercihin dağılımı: 6 / 10 / 8

- **1-6 HAYAL:** Kaybettirmez; yerleşirse büyük kazanç. Taban puana göre azalan.
- **7-16 GERÇEKÇİ:** Listenin ağırlık merkezi; yerleşme büyük olasılıkla bu blokta gerçekleşir. Meslek ve il uyumu en yüksek programlar burada yoğunlaşmalı.
- **17-24 KALE:** Güvenlik ağı. Öğrencinin "buraya yerleşsem pişman olmam" diyeceği programlardan seçilmeli; sırf garanti diye istenmeyen program yazdırma — yerleşip kayıt yaptırmamak sonraki yıl OBP katsayı kaybına yol açar (kılavuz notlarına bak).

## 4. Kompozit skor (0-100)

| Bileşen | Ağırlık | Hesap |
|---|---|---|
| Yerleşme uyumu | 25 | KALE=25, GERÇEKÇİ=18, HAYAL=8 |
| Meslek/bölüm uyumu | 25 | Hedef meslekle birebir=25, yakın alan=15, ilgili=8 |
| Şehir uyumu | 15 | Tercih edilen il=15, kabul edilebilir=8, diğer=3 |
| Program niteliği | 15 | Doluluk oranı, taban puanın alan medyanına göre konumu, dil (İngilizce +), üniversitenin alandaki bilinirliği — 0-15 arası gerekçeli takdir |
| Maliyet/burs | 20 | Devlet veya %100 burslu=20; yıllık maliyet bütçenin ≤%50'si=14, ≤%100'ü=8, aşıyor=0 |

Ağırlıklar Excel'in Metodoloji sayfasında giriş hücresidir; kullanıcı değiştirirse skorlar formülle yeniden hesaplanır. Skor tercih SIRASINI belirlemez (sırayı band yapısı belirler); aynı band içinde önceliklendirme ve eleme için kullanılır.

## 5. Dikkat edilecek yapısal noktalar

- Vakıf programlarının Burslu/%50/%25/Ücretli varyantları ayrı program kodlarıdır; Burslu varyantın taban puanı devlet üniversitelerinin çoğundan yüksektir.
- "--" taban puan = o yıl yerleşen olmamış; taban oluşmamış. Fırsat olabilir ama nedeni sorgulanmalı.
- İngilizce programlarda hazırlık yılı maliyeti ve muafiyet sınavı notu düşülmeli.
- İkinci öğretim (İÖ) devlet programları ücretlidir; maliyet satırına ekle.
- KKTC ve yurt dışı programlarda ayrı ücret/koşul yapısı vardır; kullanıcı istemedikçe havuza katma.
