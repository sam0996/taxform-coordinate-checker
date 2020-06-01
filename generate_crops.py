import argparse
import io
import os
from enum import Enum, auto
from PyPDF2 import PdfFileReader, PdfFileWriter

class Province(Enum):
    NONE = auto()
    AB = auto()
    BC = auto()
    MB = auto()
    NB = auto()
    NL = auto()
    NS = auto()
    NT = auto()
    NU = auto()
    ON = auto()
    PE = auto()
    QC = auto()
    SK = auto()
    YT = auto()

def read_coordinates(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except OSError:
        print(f'File {filepath} does not exist')
        return None

def csv_to_dict(csv_data):
    dict_data = {}
    with io.StringIO(csv_data) as f:
        while line := f.readline():
            coordinate = line.split(",")
            if (key := coordinate[0]) == 'All':
                for province, _ in Province.__members__.items():
                    if dict_data.get(province):
                        dict_data[province][coordinate[1]] = coordinate[2:]
                    else:
                        dict_data[province] = {coordinate[1]:coordinate[2:]}
            else:
                key = key.upper()
                if dict_data.get(key):
                    dict_data[key][coordinate[1]] = coordinate[2:]
                else:
                    dict_data[key] = {coordinate[1]:coordinate[2:]}
                
    return dict_data

def select_provinces(coordinate_data, province_selection):
    selected_provinces = {}
    province_selection = province_selection.split(",")
    for province in province_selection:
        if province in Province.__members__:
            selected_provinces[province] = coordinate_data[province]
    return selected_provinces

def convert_coordinates_to_int(coordinate_data):
    for province, coordinates in coordinate_data.items():
        for field, coordinate in coordinates.items():
            coordinate = [float(i.strip()) for i in coordinate]
            coordinate = tuple(coordinate)
            coordinate_data[province][field] = coordinate
    return coordinate_data

def create_pdf_crops(coordinate_data, output_path, pdf_file_name, page_number ,province, coordinate_file):
    try:
        for field, coordinate in coordinate_data.items():
            pdf_file = PdfFileReader(open(pdf_file_name, 'rb'))
            page = pdf_file.getPage(page_number)

            upperleft_y = float(page.mediaBox.getUpperLeft_y()) - coordinate[1]
            page.mediaBox.setUpperLeft(
                (coordinate[0], upperleft_y)
                )
            page.mediaBox.setLowerLeft(
                (coordinate[0], upperleft_y - coordinate[3])
                )
            page.mediaBox.setUpperRight(
                (coordinate[0] + coordinate[2], upperleft_y)
            )
            page.mediaBox.setLowerRight(
                (coordinate[0] + coordinate[2], upperleft_y - coordinate[3])
            )
            # pdf_file_name = os.path.basename(pdf_file_name)
            save_pdf_crops(page, field, output_path, province, pdf_file_name)
    except OSError as err:
        print(f'Error opening {pdf_file_name}: {err}')

def save_pdf_crops(page, field, output_path, province, coordinate_file):
    output_images = PdfFileWriter()
    output_images.addPage(page)

    coordinate_filename = os.path.basename(coordinate_file)
    output_filename = f'{coordinate_filename}_{province}_{field}.pdf'
    full_file_path = os.path.join(output_path, output_filename)
    print(full_file_path)
    output_stream = open(full_file_path, "wb")
    output_images.write(output_stream)
    output_stream.close()



def main():
    parser = argparse.ArgumentParser(description="Generate screen shots based on inputted coordinate")
    parser.add_argument('--cord', help='file name for the coordinates', required=True)
    parser.add_argument('--pdf', help='file name for the pdf', required=True)
    parser.add_argument('-n', help='which pdf page to check', default=0)
    parser.add_argument('-p', help='province selection', required=True)
    parser.add_argument('-o', help='output directory for images', default='./')

    args = parser.parse_args()

    coordinate_file = args.cord
    pdf_file = args.pdf
    province_selection = args.p
    output_dir = args.o
    pdf_page = int(args.n)

    csv_data = read_coordinates(coordinate_file)
    coordinate_data = csv_to_dict(csv_data)
    selected_provinces_data = select_provinces(coordinate_data, province_selection)
    convert_coordinates_to_int(selected_provinces_data)
    for province, coordinates in selected_provinces_data.items():
        create_pdf_crops(coordinates, output_dir, pdf_file, pdf_page, province, coordinate_file)


if __name__ == "__main__":
    main()
