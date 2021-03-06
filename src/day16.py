import math

packets = [
   "D2FE28",
   "8A004A801A8002F478", 
   "620080001611562C8802118E34", 
   "C0015000016115A2E0802F182340",
   "A0016C880162017C3686B18A3D4780",
   "C200B40A82",
   "04005AC33890",
   "880086C3E88112",
   "CE00C43D881120",
   "D8005AC2A8F0",
   "F600BC2D8F",
   "9C005AC2F8F0",
   "9C0141080250320F1802104A08",
   "A20D5CECBD6C061006E7801224AF251AEA06D2319904921880113A931A1402A9D83D43C9FFCC1E56FF29890E00C42984337BF22C502008C26982801009426937320124E602BC01192F4A74FD7B70692F4A74FD7B700403170400F7002DC00E7003C400B0023700082C601DF8C00D30038005AA0013F40044E7002D400D10030C008000574000AB958B4B8011074C0249769913893469A72200B42673F26A005567FCC13FE673004F003341006615421830200F4608E7142629294F92861A840118F1184C0129637C007C24B19AA2C96335400013B0C0198F716213180370AE39C7620043E0D4788B440232CB34D80260008645C86D16C401B85D0BA2D18025A00ACE7F275324137FD73428200ECDFBEFF2BDCDA70D5FE5339D95B3B6C98C1DA006772F9DC9025B057331BF7D8B65108018092599C669B4B201356763475D00480010E89709E090002130CA28C62300265C188034BA007CA58EA6FB4CDA12799FD8098021400F94A6F95E3ECC73A77359A4EFCB09CEF799A35280433D1BCCA666D5EFD6A5A389542A7DCCC010958D85EC0119EED04A73F69703669466A048C01E14FFEFD229ADD052466ED37BD8B4E1D10074B3FF8CF2BBE0094D56D7E38CADA0FA80123C8F75F9C764D29DA814E4693C4854C0118AD3C0A60144E364D944D02C99F4F82100607600AC8F6365C91EC6CBB3A072C404011CE8025221D2A0337158200C97001F6978A1CE4FFBE7C4A5050402E9ECEE709D3FE7296A894F4C6A75467EB8959F4C013815C00FACEF38A7297F42AD2600B7006A0200EC538D51500010B88919624CE694C0027B91951125AFF7B9B1682040253D006E8000844138F105C0010D84D1D2304B213007213900D95B73FE914CC9FCBFA9EEA81802FA0094A34CA3649F019800B48890C2382002E727DF7293C1B900A160008642B87312C0010F8DB08610080331720FC580"]

version_sum = 0
version_function = ["sum", "prod", "min", "max", None, "is_greater", "is_less", "is_equal"]

def prod(list_of_values):
   result = 1
   for x in list_of_values:
      result *= x
   return result

def is_greater(list_of_values):
   return 1 if list_of_values[0] > list_of_values[1] else 0

def is_less(list_of_values):
   return 1 if list_of_values[0] < list_of_values[1] else 0

def is_equal(list_of_values):
   return 1 if list_of_values[0] == list_of_values[1] else 0

def convert_hex_string_to_bit(hex_string):
   binary_string = [format(int(x,16), "04b") for x in hex_string]
   return "".join(binary_string)

   
def get_the_next_n_bits(data, number_of_bits):
   return data[:number_of_bits], data[number_of_bits:]

def analyze_next_packet(data):
   packet_version, packet_type, data = get_packet_version_and_type(data)
   if packet_type == 4:
      literal_value, data = decode_version_4_packet(data)
   else:
      literal_value, data = decode_version_non_4_packet(data, packet_type)
   return literal_value, data
   
def get_packet_version_and_type(packet):
   global version_sum
   packet_version, packet = get_the_next_n_bits(packet, 3)
   packet_type, packet = get_the_next_n_bits(packet, 3)
   version_sum += int(packet_version, 2)
   return int(packet_version, 2), int(packet_type,2), packet

def decode_version_4_packet(packet):
   new_data = "1111"
   literal_value = ""
   while new_data[0] == "1":
      new_data, packet = get_the_next_n_bits(packet, 5)
      literal_value += new_data[1:]
   return int(literal_value, 2), packet

def decode_version_non_4_packet(packet, packet_type):
   global version_function
   packet_values = []
   length_type, packet = get_the_next_n_bits(packet, 1)
   if length_type == "0":
      length, packet = get_the_next_n_bits(packet, 15)
      length = int(length, 2)
      final_len = len(packet) - length
      while len(packet) > final_len:
         literal, packet = analyze_next_packet(packet)
         packet_values.append(literal)
   else:
      number_of_packets, packet = get_the_next_n_bits(packet, 11)
      number_of_packets = int(number_of_packets, 2)
      for _ in range(number_of_packets):
         literal, packet = analyze_next_packet(packet)
         packet_values.append(literal)
   literal = eval(f"{version_function[packet_type]}({packet_values})")
   return literal, packet

def first_star(packet):
   global version_sum
   while len(packet) > 10:
      literal_value, packet = analyze_next_packet(packet)
   return version_sum

def second_star(packet):
   while len(packet) > 10:
      literal_value, packet = analyze_next_packet(packet)
   return literal_value

def run_two_stars(packet):
   bin_packet = convert_hex_string_to_bit(packet)
   result = first_star(bin_packet)
   print(f"DATA: {packet[:6]}, first_star: {result}")
   result = second_star(bin_packet)
   print(f"DATA: {packet[:6]}, second_star: {result}")

def main():
   global version_sum
   for packet in packets:
      version_sum = 0
      run_two_stars(packet)
      

if __name__ == "__main__":
   main()

