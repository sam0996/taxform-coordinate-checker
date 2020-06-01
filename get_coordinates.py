import argparse
import io
import csv
import os

def write_csv(data):
    # with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['province', 'field_name', 'x', 'y', 'width', 'height']
    csv_data_stream = io.StringIO('')
    writer = csv.DictWriter(csv_data_stream, fieldnames=fieldnames)

    for province, coordinate_data in sorted(data.items()):
        for field, coordinates in coordinate_data.items():
            writer.writerow({'province': province, 'field_name': field,
                                'x': coordinates[0], 'y': coordinates[1],
                                'width': coordinates[2], 'height': coordinates[3]})

    csv_data = csv_data_stream.getvalue()
    csv_data_stream.close()
    return csv_data.strip()

def save_to_csv_file(filename, csv_data):
    try:
        with open(filename, 'w', newline='') as csvfile:
            csvfile.writelines(csv_data)
    except OSError:
        print(f"Something went wrong saving {filename}")
        return None


def parse_coordinates(coordinates):
    fields = {}
    with io.StringIO(coordinates) as f:
        while coordinate_line := f.readline():
            field = coordinate_line.split(" ")[1].split('.')[2].split('_', 1)[1][:-2]
            coordinate = coordinate_line.split(" ", 3)[3].split('(')[1].strip()[:-3]
            fields[field] = coordinate
    f.close()
    return fields


def get_coordinates(coordinates_data):
    for province, coordinates in coordinates_data.items():
        coordinates_data[province] = parse_coordinates(coordinates)
    return coordinates_data

def parse_by_province(raw_coordinates):
    provinces = {}
    coordinate = ''

    with io.StringIO(raw_coordinates) as f:
        while line := f.readline():
            provinces_line = line

            line = f.readline()
            while line and line != "\n":
                coordinate += line
                line = f.readline()
                
            for province in provinces_line.split(','):
                provinces[province.strip()] = coordinate.strip()
            coordinate = ''
    
    f.close()
    return provinces

def pixels_to_pdf_points(coordinates):
    # print(coordinates.keys())
    for _, coordinate_line in coordinates.items():
        for field, coordinate in coordinate_line.items():
            coordinate_values = coordinate.replace(' ', '').split(',')
            coordinate_values = [float(i)/4.16666 for i in coordinate_values]
            coordinate_line[field] = tuple([format(i, '.5f') for i in coordinate_values])

        
def open_file(filepath):

    try:
        with open(filepath) as f:
            return f.read()
    except OSError:
        print(f'File {filepath} does not exist')
        return None


def main():
    parser = argparse.ArgumentParser(description="Process the coordinates from multiple file")
    parser.add_argument('-f', help='filename(s) containing coordinates', required=True, nargs='+')
    parser.add_argument('-o', help='output path for csv output', default="./")
    args = parser.parse_args()
    filenames = args.f
    output_path = args.o


    files_data = {}
    for filename in filenames:
        if (file_data := open_file(filename)) is not None:
            files_data[filename] = file_data

    for key, value in files_data.items():
        files_data[key] = parse_by_province(value)
        files_data[key] = get_coordinates(files_data[key])
        pixels_to_pdf_points(files_data[key])
        output_name = os.path.basename(key)
        output_name = f'{output_name}.out.csv'
        pathname = os.path.join(output_path, output_name)
        # write_csv(pathname, files_data[key])
        csv_data = write_csv(files_data[key])
        save_to_csv_file(pathname, csv_data)
        # TODO: Save csv file and then test it

if __name__ == "__main__":
    main()
