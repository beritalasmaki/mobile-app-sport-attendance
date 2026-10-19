# Design-periaatteet

Nämä periaatteet ohjaavat kaikkea käyttöliittymä- ja vuorovaikutussuunnittelua, jota teen tässä keskustelussa ja sen jatkossa. Kun suunnittelen, arvioin tai muokkaan käyttöliittymää (esim. React-komponentteja, näkymiä, lomakkeita, navigaatiota), noudatan alla olevia periaatteita ja perustelen valintani tarvittaessa niiden kautta.

## Periaatteet

1. The Ten Principles of Interaction Design
2. Don't make me think
3. Design consistency
4. Gestalt psychology

---

## 1. The Ten Principles of Interaction Design

Kymmenen vuorovaikutussuunnittelun perusperiaatetta (pohjana Jakob Nielsenin 10 käytettävyysheuristiikkaa):

1. **Järjestelmän tilan näkyvyys.** Käyttäjän pitää aina tietää, mitä tapahtuu: näytä lataus, tallennus, edistyminen ja nykyinen sijainti.
2. **Järjestelmän ja todellisen maailman vastaavuus.** Käytä käyttäjän omaa kieltä ja tuttuja käsitteitä, älä sisäistä teknistä sanastoa.
3. **Käyttäjän kontrolli ja vapaus.** Tarjoa selkeä tapa peruuttaa, palata ja kumota (undo/redo, "Peruuta", "Takaisin").
4. **Johdonmukaisuus ja standardit.** Sama asia näyttää ja toimii samalla tavalla kaikkialla; noudata alustan konventioita.
5. **Virheiden ehkäisy.** Suunnittele niin, ettei virheitä synny: järkevät oletukset, rajoitukset, vahvistus vaarallisille toiminnoille.
6. **Tunnistaminen muistamisen sijaan.** Pidä vaihtoehdot, ohjeet ja toiminnot näkyvillä, älä kuormita käyttäjän muistia.
7. **Joustavuus ja tehokkuus.** Palvele sekä aloittelijaa että kokenutta käyttäjää (oikotiet, oletukset, mukautettavuus).
8. **Esteettinen ja minimalistinen suunnittelu.** Jokainen elementti ansaitsee paikkansa; poista kaikki, mikä ei tue käyttäjän tavoitetta.
9. **Auta käyttäjää tunnistamaan, ymmärtämään ja korjaamaan virheet.** Virheilmoitukset selkeällä kielellä, ilman koodeja, ja ehdota ratkaisu.
10. **Ohjeet ja dokumentaatio.** Paras ratkaisu on, ettei ohjetta tarvita, mutta tarvittaessa ohjeen on oltava helposti löydettävä, lyhyt ja tehtäväkeskeinen.

---

## 2. Don't make me think (Steve Krug)

Käyttöliittymän pitää olla itsestään selvä. Käyttäjän ei pidä joutua pysähtymään miettimään, mitä jokin tarkoittaa tai mitä seuraavaksi pitäisi tehdä.

- Tee jokaisesta näkymästä **itsestään selvä** tai ainakin **itsestään selitettävä**.
- Käyttäjät **skannaavat**, eivät lue: käytä selkeää visuaalista hierarkiaa, lyhyitä otsikoita ja tiivistä tekstiä.
- Poista turha sanamäärä; leikkaa tekstistä puolet, sitten puolet siitä uudelleen.
- Tee klikattavat asiat selvästi klikattaviksi.
- Älä käytä mielikuvituksellisia nimiä tai kikkailua, kun selkeä nimi toimii.
- Vähennä päätöksiä: jokainen turha valinta lisää kognitiivista kuormaa.
- Navigaation pitää kertoa aina: missä olen, mistä pääsen minne, miten pääsen takaisin.

**Testi:** Jos joudun selittämään, miten jokin toimii, suunnittelu ei ole vielä valmis.

---

## 3. Design consistency

Johdonmukaisuus tekee käyttöliittymästä ennustettavan ja nopean oppia.

- **Visuaalinen johdonmukaisuus:** samat värit, typografia, välitykset, kulmien pyöristykset ja ikonityyli kaikkialla. Käytä design tokeneita (värit, fontit, spacing) yhtenä lähteenä.
- **Toiminnallinen johdonmukaisuus:** samanlaiset toiminnot toimivat samalla tavalla (painikkeet, lomakkeet, vahvistukset, virheet).
- **Sisällöllinen johdonmukaisuus:** sama termi tarkoittaa aina samaa asiaa; sama äänensävy.
- **Ulkoinen johdonmukaisuus:** noudata alustan ja alan tuttuja konventioita.
- Käytä uudelleenkäytettäviä komponentteja yksittäisten tyylien sijaan.
- Poikkeus tehdään vain, jos sille on selkeä syy, ja poikkeuksen pitää näyttää tarkoitukselliselta.

---

## 4. Gestalt psychology

Ihmisen hahmottaminen ryhmittelee elementtejä automaattisesti. Hyödynnän näitä lakeja asettelussa ja hierarkiassa:

- **Läheisyys (proximity):** toisiinsa liittyvät elementit sijoitetaan lähelle toisiaan, asiaan kuulumattomat erilleen.
- **Samankaltaisuus (similarity):** samalla tavalla näyttävät elementit koetaan saman ryhmän jäseniksi (väri, muoto, koko).
- **Jatkuvuus (continuity):** silmä seuraa linjoja ja kaaria; käytä linjauksia ohjaamaan katsetta.
- **Sulkeisuus (closure):** mieli täydentää puuttuvat osat; kokonaisuuden ei tarvitse olla täysin piirretty.
- **Hahmo ja tausta (figure/ground):** tärkeä sisältö erottuu selvästi taustasta; käytä kontrastia ja syvyyttä.
- **Yhteinen alue (common region):** reunus tai tausta kokoaa elementit yhteen ryhmäksi (esim. kortit).
- **Yhteinen kohtalo (common fate):** yhdessä liikkuvat elementit koetaan yhteen kuuluviksi (animaatiot).
- **Symmetria ja järjestys (prägnanz):** ihminen tulkitsee kuvion yksinkertaisimmalla mahdollisella tavalla; suosi selkeitä ja yksinkertaisia rakenteita.

---

## Käytännön toimintatapa

Kun suunnittelen tai muokkaan käyttöliittymää:

1. Tarkista, ettei näkymä vaadi käyttäjältä turhaa ajattelua (periaate 2).
2. Käytä samoja tokeneita, komponentteja ja sanastoa kuin muualla projektissa (periaate 3).
3. Ryhmittele ja korosta sisältö Gestalt-lakien mukaan (periaate 4).
4. Käy lopuksi läpi kymmenen vuorovaikutusperiaatetta tarkistuslistana (periaate 1).
5. Jos jokin pyyntö on ristiriidassa näiden kanssa, kerro se lyhyesti ja ehdota vaihtoehto.
