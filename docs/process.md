# Prosessimittari: Club Coach

Yksi paikka, josta näkee missä prosessissa ollaan. Figmassa sama sisältö on sivulla CLUB COACH, osiossa `07 · Prosessimittari`.
Päivitetty: 28.10.2026. Päivitetään jokaisen työsession lopussa. Tämä tiedosto on lähde; Figma-näkymä päivitetään siitä.

## Työskentelysäännöt
1. Työskennellään vain kohdassa **Nyt**. Siinä on aina tasan yksi asia.
2. Uusia kokonaisuuksia ei aloiteta ilman, että omistaja hyväksyy ne. Ideat menevät kohtaan **Parkissa**.
3. Jokainen vastaus loppuu tilannekatsaukseen: valmista, nyt, seuraavaksi, odottaa omistajaa (enintään 5 riviä).
4. Vaihe ei ole valmis, ennen kuin sen portti on täytetty.
5. Päätökset ja kompromissit kirjataan `docs/project-log.md`:hen.

## Nyt
**Vanhempien sovelluksen mid-fi-ruudut: Tapahtuma-ruudut** (tiedot, osallistujat, keskustelu). Vanhempien ruudut: 2 / 7 valmiina (Tänään, Kalenteri).

## Seuraavaksi (enintään 3)
1. Loput vanhempien mid-fi-ruudut: Keskustelut, Laskut ja Lasku, Minä.
2. Figma-proto vanhempien mid-fi-ruuduista (avainpolut klikattavissa).
3. Testisuunnitelma ja haastattelurunko (Claude valmistelee, omistaja tekee haastattelut ja testit).

## Odottaa omistajaa
- Keitä haastatellaan ja testataan (vanhempia ja valmentajia, montako)?
- Seurojen vaakunoiden ja kuvien käyttöoikeudet (nyt paikkamerkkejä).

## Parkissa (ei tehdä nyt)
- Neljä värilöydöstä (`colour-usage.md` kohta 8): `text/on-fill`, `status/warning`, `border/strong`, `accent`-grafiikka.
- Valmentajasovelluksen violetti sävy ja sovellusikonit.
- Hi-fi-etusivujen päivitys uuteen rakenteeseen.
- Harmaan tilan vihreät jäänteet (nav-merkki, selitepisteet).
- README:n täydennykset.

## Rata A: tuotesuunnittelu
| # | Vaihe | Tila | Portti (valmis kun) |
|---|---|---|---|
| 1 | Käyttäjätutkimus | **Ohitettu, tehdään** | 5–8 haastattelua (vanhemmat ja valmentajat), löydökset kirjattu. Nyt on vain hypoteeseja |
| 2 | Konsepti ja rakenne | Valmis | Tietoarkkitehtuuri ja avainpolut hyväksytty. Kaksi sovellusta päätetty |
| 3 | Mid-fi ja proto | **Käynnissä** (vanhemmat 2/7, valmentajat 0/?) | Kaikki avainpolut klikattavissa Figma-protona kummassakin sovelluksessa |
| 4 | Testaus ja iterointi | Tulossa | 5 testaajaa per sovellus, löydökset ja muutokset kirjattu, toistetaan kunnes testitehtävät onnistuvat |
| 5 | Hi-fi | Tulossa | Testattu rakenne piirretty kolmelle seuralle, vaalea ja tumma. Vanhat etusivut arkistoitu |
| 6 | Toteutus | Tulossa | PWA mock-datalla julkaistu, rajapintakuvaus (`docs/technology.md`) |

## Rata B: design system
| # | Vaihe | Tila | Portti (valmis kun) |
|---|---|---|---|
| 1 | Audit | **Ohitettu, tehdään jälkikäteen** | Mid-fi-ruuduista listattu toistuvat elementit, komponenttijärjestys ja lukittavat värit päätetty |
| 2 | Arkkitehtuuri ja tokenit | Valmis | Kerrokset, nimeäminen ja arvot dokumentoitu (`docs/design-system/README.md`). Neljä löydöstä parkissa |
| 3 | Komponentit | **Käynnissä** (noin 28) | Auditoitu lista vahvistettu, tilat (pressed, disabled, focus) tehty |
| 4 | Patternit | Tulossa | Toistuvat yhdistelmät (lista + suodatin, lomake, tyhjä ja virhetila) dokumentoitu |
| 5 | Dokumentaatio | **Käynnissä** | README ja värisäännöt hyväksytty |
| 6 | Koodiin | Tulossa | Tokenit CSS-muuttujina ja Tailwind-teemana, komponentit Reactilla |

## Miksi järjestys on tämä
Tuotesuunnittelu etenee tutkimus, konsepti, mid-fi, testaus ja iterointi, hi-fi, toteutus. Design systemissä audit tulee ennen tokeneita ja komponentteja.
Tässä projektissa design system eteni tuotetta pidemmälle ja tokenit tehtiin ennen auditia. Se korjataan: auditti tehdään vanhempien mid-fi-ruutujen jälkeen, ja hi-fi aloitetaan vasta testauksen jälkeen.
