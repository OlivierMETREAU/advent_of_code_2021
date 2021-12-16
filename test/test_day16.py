from ..src import day16

def test_hexa_to_bin():
   assert day16.convert_hex_string_to_bit("38006F45291200") == "00111000000000000110111101000101001010010001001000000000"

def test_get_version():
   converted = day16.convert_hex_string_to_bit("38006F45291200")
   packet_version, packet_type, data = day16.get_packet_version_and_type(converted)
   assert 1 == packet_version

def test_get_type():
   converted = day16.convert_hex_string_to_bit("38006F45291200")
   packet_version, packet_type, data = day16.get_packet_version_and_type(converted)
   assert 6 == packet_type

def test_decode_literal():
   converted = day16.convert_hex_string_to_bit("D2FE28")
   packet_version, packet_type, data = day16.get_packet_version_and_type(converted)
   literal_value, data = day16.decode_version_4_packet(data)
   assert 2021 == literal_value