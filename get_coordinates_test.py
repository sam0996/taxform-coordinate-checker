import unittest
import test_values
import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_open_file_exists(self):
        self.maxDiff = None
        filepath = 'example-data/sample.txt'
        data = get_coordinates.open_file(filepath)
        self.assertEqual(data, test_values.open_file_answer)

    def test_open_file_not_exist(self):
        filepath = 'foo/bar'
        data = get_coordinates.open_file(filepath)
        self.assertEqual(data, None)

    def test_parse_province(self):
        output = get_coordinates.parse_by_province(test_values.parse_input)
        self.assertDictEqual(output, test_values.parse_answer.copy())

    def test_get_coordinates(self):
        get_coordinates_input = test_values.parse_answer.copy()
        get_coordinates_output = get_coordinates.get_coordinates(get_coordinates_input)
        self.assertDictEqual(get_coordinates_output, test_values.get_coordinates_output)

    def test_pixels_to_pdf_points(self):
        pixels_to_pdf_points = test_values.pixels_to_pdf_points_input.copy()
        get_coordinates.pixels_to_pdf_points(pixels_to_pdf_points)
        self.assertDictEqual(pixels_to_pdf_points, test_values.pixels_to_pdf_points_output)

    def test_write_csv(self):
        file_data = test_values.pixels_to_pdf_points_output.copy()
        csv_output = get_coordinates.write_csv(file_data)
        self.assertEqual(csv_output, test_values.write_csv_output)

    # def test_save_to_csv_file(self):``



if __name__ == "__main__":
    unittest.main()