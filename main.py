import qrcode
import vobject
import pandas as pd
import snakecase


def get_str_codigo_or_empty(value):
    try:
        return int(value)
    except ValueError:
        return ''


def save_qrcode_image_file(**kwargs):
    lst_required_keys = ['fn', 'path']
    if any([False if value in kwargs.keys() else True for value in lst_required_keys]):
        print(f'The values of "{lst_required_keys}" is required')
        return

    # Create a vCard object with contact information
    contact = vobject.vCard()
    for key, value in kwargs.items():
        if key=='path':
            continue

        contact.add(key)

        if key == 'fn':
            lst_split_name = value['value'].split()

            contact.add('n')
            contact.n.value = vobject.vcard.Name(
                family=lst_split_name[-1],
                given=lst_split_name[0]
            )

        getattr(contact, key).value = value['value']
        if 'type_param' in value.keys():
            getattr(contact, key).type_param = value['type_param']

    # Generate QR code for vCard
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(contact.serialize())
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(kwargs['path'])


def read_excel_make_dct(excel_path):
    df_excel = pd.read_excel(excel_path)

    lst_excel_contacts = []

    for index, row in df_excel.iterrows():
        print(index, row)

        str_phone =  f'+{row["codigo_pais"]}-{row["ddd"]}-{row["celular"]}'
        snake_name = snakecase.convert(row["nome"]).replace(' ', '')

        dct_contact = {
            'path': f'./files/{snake_name}.png',
            'fn': {
                    'value': row["nome"]
                },
            'tel': {
                'value': str_phone,
                'type_param': 'CELL'
            },
            'email': {
                'value': row['email'],
                'type_param': 'INTERNET'
            },
        }

        lst_excel_contacts.append(dct_contact)

    return lst_excel_contacts


if __name__ == '__main__':

    lst_all_contacts = read_excel_make_dct('data.xlsx')
    for dct_contact in lst_all_contacts:
        save_qrcode_image_file(**dct_contact)
