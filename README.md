# bit-ai-algen-alg1

[![Join the chat at https://gitter.im/hawkerpl/bit-ai-algen-alg1](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/hawkerpl/bit-ai-algen-alg1?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Pierwsze laboratorium przygotowane dla kola naukowego bit-ai.
22 styczen 2015

##obsluga
 - sciagamy repozytorium wszystkimi branchami
 - przechodzimy do lev0
 - rozpoczynamy kodzenie, jezeli nie nadazamy, przechodzimy do nastepnego "lev", i ewentalnie mergujemy to co juz napisalismy.
 - testujemy napisany kod, testy nie zmieniaja sie miedzy branchami, wiec nie beda przechodzic w calosci dopoki nie zrobimy wszystkiego.
 - testy nie gwarantuja poprawnosci kodu
 
##pliki
- individual.py i population.py zawieraja klasy ktore nalezy zaimplementowac
- tools.py zawiera dodatkowa funkcje ktore powinno sie zaimplementowac samemu, ale mozna skorzystac z gotowej
- nim_tools.py zawiera dodawtkowe funkcje, funkcje symulacji gry, oraz funkcje pozwalajaca na wysyłanie osobnika do turnieju
- reszta zawiera testy jednostkowe

##tresc
- nalezy zaimplementowac prosty algorytm genetyczny SGA w celu wyłonienia gry nim
- genomem osobnika jest ciąg binarny (jako string) który implementuje strategie gry w nim
   - gra w nim: w grze jest obecnych 2 graczy, oraz stos n kamieni, każdy gracz po kolei ściąga po 1 lub 2 kamieni ze stosu,
   gracz który ostatni ściągnie kamienie tak że nie zostaju już żaden, przegrywa.
   - ciąg binarny powinien być o długoci n, miejsce w ciągu reprezentuje lcizbe kamieni na stosie,
   wartość w ciągu reprezentuje liczbe kamieni jaką bot powinien ściągnąć,
   "1" - bot ściąga 2 kamienie
   "0" - ściaga 1 kamień 
- sprawdzanie dostosowania w populacji jest robione poprzez walkę (grę w nim) par osobników
- selekcja prowadzona jest przez wybieranie tych osbników które przetrwały walki
- rozmnazanie poprzez crossing over genomow dwu osobnikow i stworzeniu nowych 4 osobnikow

##jak działać samemu
- ściągnij repo otwórz sobie lev0 bądź też od razu lev1
- rozwijaj kod klasy Population tak aby przechodził test (ind_test.py), dodatkowo:
  - stwórz odpowiednio count_fitness i selekcje tak jak opisałe powyżej i jak to wynika z testów
  - w funkcji rozradzającej użyj crossing over (jest zaimplementowana w tool)
  - następnie od razu wykonaj dla nich mutacje (z prawdopodobienstwiem odpowiadającym Individual.mutation_factor, czyli np w przypadku testowym/domyslnym 5 czyli 5%), jeżeli mutacja ma zostać wykonana zamieniamy jeden gen na losowy inny gen
- jeżeli przechodzisz przez test upewnij się że w miare wsyzstko działa w konsoli sprawdzajac samemu zachowanie klasy Individual
- przejdz do rozwijania Population
- rozwijaj kod klasy Population tak aby przechodził test (pop_test.py), dodatkowo:
  - stwórz metode evaluate tak aby lcizyła wartosc funkcji dostosowania dla każdego osbnika w populacji i tak jak to wynika z testow
  - stwórz metode selection tak aby w tablicy selected była zapisana połowa najlepszych osobników w populacji i tak jak to wynika z testow
  - stwórz metode breed tak aby z 2 osobników robiła 4 nowych (2 razy wywołujesz breed with) i zapisywała ich do nowej populacji _(uwaga, przez to najprawdopodobniej liczba osobników w populacji musi być pdozielna przez 4)_
  - metode evolve stwórz tak jak to wynika z testów
- jeżeli przechodzisz przez test upewnij się że w miare wsyzstko działa w konsoli sprawdzajac samemu zachowanie klasy Population
- o ile wszystko się zgadza, powinieneś mieć działający algorytm genetyczny :)

##zrobiłem i co dalej
Pobaw się ;) 
Przede wszystkim stwórz sobie nową populacje, wywołaj na niej metodę evolve, wypisując osobników wedle uznania i obserwój jak tworzy się optymalna strategia gry.
Jeżeli tak się dzieje możesz się pobawić w inny sposób:
 * Pobaw się długościami genomu
 * Liczbą osobników
 * Prawdopodobieństwem mutacji
 * Funkcją dostosowania
 * Spróbuj co sie stanie jeżeli będziesz zawsze zostawiał najlepszego osbnika
 * Zmień sposób selekcji
 * zmień sposób przeprowadzania sprawdzania dostosowania

###Pytania i odpowiedzi:
Pytania mozesz zadawac na tym repo, przez mojego uzytkownika znajdziesz rowniez kontakt do mnie.


#### Quick guide gita
wchodzim do jakiegokolwiek katalogu, 
robimy
```
git clone https://github.com/hawkerpl/bit-ai-algen-alg1.git
```
wchodzimy do brancha:
```
git checkout lev0
```
stwierdzilismy ze costam zrobilismy i przechodzimy do innego brancha wiec
zapisujemy to oco zrobilismy
```
git add . 
git commit -m "wiadomosc"
```
i przechodzimy 
`git checkout lev0`
