from smbus2 import SMBus
import time

def main():
    # TMP422 slave address
    address = 0x4C

    # Read local temperature register (0x00)
    temp_reg = 0x00

    with SMBus(1) as bus:
        for i in range(10):
            time.sleep(0.01)
            # Read a block of 2 bytes
            high_byte, low_byte = bus.read_i2c_block_data(address, temp_reg, 2)
            high_res = high_byte if not high_byte & 128 else ~(high_byte ^ 255) #Two's complement
            low_res = (low_byte >> 4) * 0.0625 #One int unit (bit shifted) corresponds with 0.0625 °C
            print(high_res + low_res, " °C")

if __name__ == "__main__":
    main()
