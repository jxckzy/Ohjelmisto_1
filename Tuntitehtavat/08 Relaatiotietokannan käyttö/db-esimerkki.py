import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='illia',
         password='salasana3',
         autocommit=True
         )
    
def hae_lentokentat():
    sql = f"SELECT ident, name FROM airport LIMIT 5"
    print(sql)
    kursori = yhteys.cursor()
    
    kursori.execute(sql)

    yksi = kursori.fetchone()
    print(yksi)

    kaikki = kursori.fetchall()
    print(kaikki)

    # tulostetaan kyseiset alkiot
    print(kaikki[0]) # ensimmäinen
    print(kaikki[1]) # toinen
    print(kaikki[-1]) # viimeinen

    # tulostetaan kyseinen alkion merkintä (nimi - 1, ident - 0), ensin sijainti, sitten merkintä
    viimeinen_kentän_nimi = kaikki[-1][1]
    (ident, nimi) = kaikki[-1]
    print(viimeinen_kentän_nimi)
    print(f"ident: {ident}, nimi: {nimi}")

    for arvo in kaikki:
        print(arvo)
        print(arvo[0])
        print(arvo[-1])

    print(kursori.rowcount)

def hae_kentta_ident_koodilla(ident):
    sql = f"SELECT * FROM airport WHERE ident = '{ident}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    data = kursori.fetchall()
    print(data)

def muokkaa_kentan_nimea(ident, uusi_nimi):
    sql = f"UPDATE airport SET name = '{uusi_nimi}' WHERE ident = '{ident}' LIMIT 1"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    if kursori.rowcount == 1:
        print('Update toimii.')

# hae_lentokentat()
hae_kentta_ident_koodilla('00AA')
muokkaa_kentan_nimea("00KS", "Kivä kenttä")