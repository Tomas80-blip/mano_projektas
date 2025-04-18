# Objektų katalogas naudojant Django 

Projekto pavadinimas ir trumpas aprašymas:

Django aplikaciją “katalogas”, kuris atvaizduoja knygas ir informaciją apie jas. 

I
1. Sukurkite Django projektą ir aplikaciją (pvz. katalogas). 
2. Sukurkite SQLite duomenų bazę su viena lentele, kurioje yra bent 15 objektų (įrašų). 
3. Lentelė gali turėti tokius laukus kaip: id, pavadinimas, aprasymas, kaina, 
kategorija. 
4. Duomenis galima užpildyti per Django admin sąsają arba naudojant manage.py 
shell. 
5. Sukurkite pagrindinį puslapį, kuriame naudojant views.py ir templates 
atvaizduojami visi katalogo įrašai (naudojant Django šablonų sistemą). 

II
1. Pridėkite paieškos laukelį, leidžiantį filtruoti įrašus pagal pavadinimą arba 
kategoriją. 
2. Paieška turi veikti per GET parametrus (pvz., ?kategorija=Knyga). 
3. Jei paieška neįvesta, rodomi visi įrašai. 

III
Papildomai prie aukščiau nurodytų reikalavimų: 
1. Pridėkite galimybę pridėti naują objektą naudojant Django ModelForm. 
2. Pridėkite galimybę redaguoti esamą objektą (naudojant UpdateView). 
3. Pridėkite galimybę ištrinti objektą (naudojant DeleteView). 
4. Pagrindiniame puslapyje objektų sąrašas turi būti atnaujinamas po kiekvieno 
veiksmo.

IV
Papildomai: 
1. Sukurkite antrinę lentelę, pavyzdžiui Kategorija, kuri turi ryšį su objektų lentele 
(ForeignKey). 
2. Sukurkite statistikos puslapį, kuriame būtų apskaičiuojama:
a. kiek objektų priklauso kiekvienai kategorijai; 
b. vidutinė kaina pagal kategoriją; 
c. brangiausias objektas; 
d. pigiausias objektas. 
3. Naudokite annotate(), Count(), Avg(), Max() iš Django ORM.


Technologijos, kurios buvo naudotos (Python, PyCharm Community edition, Django)


Instrukcija, kaip paleisti projektą savo kompiuteryje

1. Atsisiųsti Python   https://www.python.org/downloads/release/python-31011/
2. Atsisiųsti PyCharm Community edition
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windowsARM64&code=PCC
3. Įsidiekite Python ir PyCharm Community edition IDE.

4. Atsisiųsti Django projektą iš GitHub:
Terminale (Command Prompt, PowerShell arba macOS/Linux Terminal):
git clone https://github.com/vartotojas/projektas.git
(Pakeisk šitą nuorodą į tikrą tavo projekto GitHub nuorodą.
5. Sukurk ir aktyvuok virtualią aplinką

python -m venv env

Windows:
env\Scripts\activate
env\Scripts\activate

macOS / Linux:
source env/bin/activate

6. Įdiegti reikalingas bibliotekas: 
Jei projekte yra requirements.txt failas:
pip install -r requirements.txt

Jei nėra – įdiegti Django rankiniu būdu:

pip install django

7. Django projekto paleidimas
Sukurti duomenų bazę:

python manage.py migrate

(Pasirinktinai) – sukurti administratoriaus paskyrą:
python manage.py createsuperuser

Paleisti serverį:

python manage.py runserver

Atidaryti naršyklę ir eiti į:
http://127.0.0.1:8000/

Prideti kategorijas ir knygas per shell(terminale)
python manage.py shell

from katalogas.models import Kategorija, Knyga

k1 = Kategorija.objects.create(pavadinimas='Romanas')
k2 = Kategorija.objects.create(pavadinimas='Mokslinė')
k3 = Kategorija.objects.create(pavadinimas='Medicina')

Knyga.objects.create(pavadinimas='Knyga A', aprasymas='Aprašymas A', kaina=10.99, kategorija=k1)
exit()


