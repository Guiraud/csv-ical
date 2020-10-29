from csv_ical import Convert


convert = Convert()
convert.CSV_FILE_LOCATION = 'mg.csv'
convert.SAVE_LOCATION = 'mg.ics'

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)

convert = Convert()
convert.CSV_FILE_LOCATION = 'mg_CNAM.csv'
convert.SAVE_LOCATION = 'mg_CNAM.ics'

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)

convert = Convert()
convert.CSV_FILE_LOCATION = 'mg_CSE.csv'
convert.SAVE_LOCATION = 'mg_CSE.ics'

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)

convert = Convert()
convert.CSV_FILE_LOCATION = 'mg_DS.csv'
convert.SAVE_LOCATION = 'mg_DS.ics'

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)