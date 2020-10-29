pass=`python3 main.py`
curl -u $pass https://mail.enercoop.org/SOGo/dav/mehdi.guiraud/Calendar/personal.ics > mg.ics
curl -u $pass https://mail.enercoop.org/SOGo/dav/mehdi.guiraud/Calendar/3E6B-5F899100-3-47450400.ics > mg_CNAM.ics
curl -u $pass https://mail.enercoop.org/SOGo/dav/mehdi.guiraud/Calendar/3EAE-5F899180-1-4CF4C380.ics > mg_CSE.ics
curl -u $pass https://mail.enercoop.org/SOGo/dav/mehdi.guiraud/Calendar/3EAE-5F899180-3-4CF4C380.ics > mg_DS.ics
python3 ics2csv.py
rm -f *.ics