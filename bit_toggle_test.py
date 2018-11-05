import numpy as np

def read_img():
    img = np.memmap('imglib_inputdump_4.yuv', dtype='uint16', mode='r').reshape(240, 320)
    return img


def bit_toggle(img, num_bits):
    toggle_0 = [0 for i in range(num_bits)]
    toggle_1 = [1 for i in range(num_bits)]
    for col in range(np.shape(img)[0]):
        for row in range(np.shape(img)[1]):
            for i in range(num_bits):
                if toggle_0[i] == 0:
                    set_bit = (img[col, row] & (1 << i)) >> i
                    toggle_0[i] = set_bit
                if toggle_1[i] == 1:
                    set_bit = (img[col, row] & (1 << i)) >> i
                    toggle_1[i] = set_bit

    return toggle_0, toggle_1

if __name__ == '__main__':
    img = read_img()
    t0, t1 = bit_toggle(img, 14)
    print("t0 = ", t0)
    print("t1 = ", t1)