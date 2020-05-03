import csv


with open('confirmed_first_edition_2019-08-04.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, quotechar='"')
    for row in reader:
        chapter, page, description, credit, notes = row
        table_row = f'''  <tr>
    <td class="erratum-chapter">{chapter}</td>
    <td class="erratum-page">{page}</td>
    <td class="erratum-description">{description}</td>
    <td class="erratum-credit">{credit}</td>
    <td class="erratum-notes">{notes}</td>
  </tr>'''
        print(table_row)
