# WikipediaGPTApp
Repozitorijum za predmet napredno softversko inženjerstvo

## 📌 Opis projekta

Problem koji ovaj projekat rešava je kako automatski prikupiti i obraditi tekstualni sadržaj koji bi mogao da se koristi u istraživanjima, testiranju algoritama za obradu jezika, ili za pravljenje datasetova. U oblastima poput lingvistike, NLP-a i detekcije AI sadržaja u tekstovima, potrebni su jasno označeni tekstualni uzorci, ali ih je teško prikupiti ručno, pa ova aplikacija omogućava efikasno generisanje i preuzimanje tekstova za zadatu ključnu reč. Ručno traženje i kopiranje teksta sa interneta je veoma neefikasno, pa su tehnologije poput Wikipedia API i OpenAI API, zbog mogućnosti pristupa tekstovima i generisanja sadržaja, bile pogodne za implementaciju ovog rešenja.
## 🛠️ Tehnologije

- **Python 3**
- **Wikipedia API** – omogućava direktno preuzimanje sadržaja sa Wikipedije
- **OpenAI API** – za generisanje teksta od strane veštačke inteligencije
- **Tkinter** – za GUI
---
## 🌐 Wikipedia API (MediaWiki API)

Wikipedia API, poznat i kao **MediaWiki API**, predstavlja skup pravila i protokola koji omogućavaju programerima da interaguju sa platformom Wikipedia. Omogućava pristup različitim funkcionalnostima, uključujući:

- pretragu članaka,
- dobijanje i čuvanje sadržaja stranica,
- uređivanje postojećih članaka,
- kao i dobijanje revizija i metapodataka.

MediaWiki je veoma moćan i skalabilan softver koji beleži sve izmene — prilikom svakog uređivanja stranice prethodna verzija se **ne briše**, već se čuva u bazi podataka. Ovo omogućava **vraćanje stranica** u slučaju vandalizma, grešaka ili spama.

Wikipedia API je implementiran po principima **RESTful arhitekture**, koristeći **HTTP zahteve** (najčešće GET i POST) za komunikaciju sa serverom. Odgovori se vraćaju u formatima kao što su **JSON** ili **XML**, što omogućava laku obradu podataka pomoću biblioteka poput requests u Pythonu.

Iako je backend MediaWiki softvera razvijen u **PHP-u** i koristi **MySQL** bazu podataka, API je nezavisan od ovih tehnologija — osmišljen je za jednostavnu i efikasnu komunikaciju između klijenta i servera.

### ⚠️ Ograničenja i izazovi

Iako API omogućava jednostavan pristup sadržaju Wikipedije, postoji niz tehničkih izazova pri njegovoj upotrebi:

- **Parsiranje Wikitext-a**: Wikipedia koristi sopstveni format za uređivanje — *Wikitext*, koji je kompleksan i teško ga je precizno parsirati.
- **Nedostatak CMS funkcionalnosti**: MediaWiki nije dizajniran kao sistem za upravljanje sadržajem (CMS) i ne pruža potpunu zaštitu osetljivih podataka, s obzirom na to da mu je primarni cilj otvorenost.
- **Nema forkovanja/spajanja istorije**: Ne podržava radne tokove slične Git-u (npr. branch-ovanje i merge-ovanje).
- **Dokumentacija ekstenzija**: Dostupnost dokumentacije ekstenzija može predstavljati izazov, jer često ekstenzije ne uključuju integrisanu dokumentaciju, već se ona može naći samo na medwiki.org.
- **Nestabilnost API-ja**: MediaWiki API se aktivno razvija i može se menjati — aplikacije koje ga koriste moraju se često ažurirati.

## 🤖 OpenAI API (ChatGPT API)

OpenAI ChatGPT API omogućava pristup GPT modelu za automatsko generisanje teksta na osnovu korisničkih upita na prirodnom jeziku. Kroz jednostavan **RESTful interfejs**, API prihvata zahteve preko **HTTP protokola** i vraća generisani tekst kao odgovor.

API je dizajniran za široku primenu u različitim programskim jezicima, uključujući Python, Node.js i druge, što ga čini veoma pristupačnim za integraciju u različite aplikacije.

### Glavne funkcionalnosti uključuju:

- automatsko odgovaranje na pitanja,  
- sažimanje tekstova,  
- pisanje eseja i kreativnih sadržaja,  
- generisanje tehničkih objašnjenja i slično.

### Prednosti

- **Visoka preciznost**  
  ChatGPT API može generisati izuzetno koherentne i informativne odgovore, što ga čini pogodnim za različite aplikacije.
  
- **Fleksibilnost**  
  Model može odgovoriti na širok spektar pitanja i zadataka, od generisanja kreativnog sadržaja do tehničkih objašnjenja.
  
- **Podrška za više jezika**  
 API podržava rad sa više jezika, što je korisno za internacionalizovane aplikacije.

### ⚠️ Ograničenja i izazovi

- **Povremena netačnost**  
  Model može generisati odgovore koji su netačni ili neadekvatni, posebno kada nema dovoljno informacija u treniranju.

- **Visoki troškovi za velike količine podataka**  
  Korišćenje API-ja na velikoj skali može biti skupo, što zahteva optimizaciju broja zahteva.

- **Ograničeno znanje**  
  API ima ograničenja u poznavanju događaja i činjenica nakon septembra 2021. godine, jer nije treniran na novijim podacima.

## 🖥️ Tkinter

Tkinter je standardna biblioteka za kreiranje grafičkih korisničkih interfejsa (GUI) u Pythonu. Ova biblioteka pruža jednostavan i intuitivan način za izradu desktop aplikacija, omogućavajući programerima da brzo razviju aplikacije sa različitim elementima interfejsa, kao što su dugmad, unosi, liste i drugi grafički elementi.

### Najčešća primena Tkinter-a:

1. **Kreiranje prozora i dijaloga**  
   Tkinter se može koristiti za kreiranje prozora i dijaloga koji omogućavaju korisnicima interakciju sa programom. Ovi elementi mogu služiti za prikaz informacija, prikupljanje korisničkih unosa ili prezentovanje opcija korisnicima.

2. **Pravljenje GUI za desktop aplikacije**  
   Tkinter omogućava kreiranje interfejsa za desktop aplikacije, uključujući dugmad, menije i druge interaktivne elemente. Sa Tkinter-om, možete brzo napraviti intuitivni interfejs za desktop aplikacije koje se izvršavaju na različitim platformama.

3. **Dodavanje GUI u command-line programe**  
  Tkinter se može koristiti za dodavanje grafičkog interfejsa u postojeće command-line programe, čime se olakšava interakcija korisnika sa programom i unos argumenata. Na ovaj način, Tkinter može transformisati jednostavne skripte u aplikacije sa grafičkim interfejsom.

4. **Kreiranje odgovarajućih widget-a**  
   Tkinter uključuje razne ugrađene widget-e, kao što su dugmad, oznake i tekstualni okviri, ali moguće je kreirati i sopstvene prilagođene widget-e. Ovo omogućava razvoj jedinstvenih komponenti koje odgovaraju specifičnim potrebama aplikacije.
   
5. **Izrada prototipova GUI-a**  
   Tkinter je odličan alat za brzu izradu prototipova korisničkog interfejsa, omogućavajući brzo testiranje i iteraciju različitih dizajnerskih ideja pre konačne implementacije.
   
### Osnovni koncepti u Tkinter aplikacijama:

- **Uključivanje Tkinter modula**  
  Tkinter je deo standardne Python instalacije, pa je njegovo uključivanje jednostavno. Provera da li je Tkinter dostupan može se uraditi ovim kratkim kodom:

  ```python
  import tkinter
  print("Tkinter je instaliran!")

## 📌 Preuzimanje i pokretanje aplikacije

### 1. Instalacija Python-a

Uverite se da imate instaliran **Python 3.8** ili noviji. Možete ga preuzeti sa zvaničnog sajta:  
🔗 https://www.python.org/downloads/

Proverite instalaciju komandom:

```bash
python --version
```
ili
```bash
python3 --version
```

### 2. Kloniranje repozitorijuma
```bash
git clone https://github.com/Bukumira/WikipediaGPTApp.git
```

### 3. Instalacija potrebnih biblioteka
```bash
pip install -r requirements.txt
```
### 4. Postavljanje API ključa
Aplikacija koristi OpenAI GPT API. Da bi radila, morate postaviti svoj OpenAI API ključ.

Koraci:
Napraviti .env fajl u root direktorijumu projekta.

Uneti sledeće u .env fajl:
```ini
OPENAI_API_KEY=ovde_ide_api_kljuc
```
### 5. Pokretanje aplikacije
Nakon što su biblioteke instalirane i .env fajl je postavljen, aplikaciju pokrenuti komandom:
```bash
python main.py
```
## 🖥️ Kako koristiti aplikaciju

1. Pokrenuti program (`python main.py`)
2. Uneti ključnu reč.
3. Izabrati željeni jezik (English, German, Serbian).
4. Kliknuti na dugme **"Fetch Revision Text"** preuzima se odgovarajući sadržaj sa Wikipedije.
5. Ako za traženi pojam postoji verzija koja je napisana ***pre početka 2021. godine***, aktivira se dugme **"Generate AI Text"**.
6. Klikom na to dugme dobija se tekst generisan pomoću OpenAI API-ja.
7. Rezultati se prikazuju u izlaznom prozoru.
>Napomena: Zbog mogućnosti da se projekat koristi za detekciju AI-generisanog sadržaja u tekstovima, koristi se verzija Wikipedia teksta koja je objavljena pre pojave ChatGPT-a. Kao referentna tačka uzeta je poslednja dostupna revizija iz 2020. godine. Ukoliko takva revizija ne postoji, preuzima se najbliža starija dostupna revizija, kako bi se osiguralo da tekst nije mogao biti generisan pomoću veštačke inteligencije.
